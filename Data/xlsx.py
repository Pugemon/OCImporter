import pandas as pd
from pandas import DataFrame

from config import logger
import re

sub_locale = r"\(.*\)"

# TODO to custom Type
PRODUCTS = "Products"
ADDITIONAL_IMAGES = "AdditionalImages"
PRODUCT_ATTRIBUTES = "ProductAttributes"


class ExcelFileWork:
    def __init__(self, workdir):
        self.workdir = workdir

    def get_filenames(self):
        """ Получение списка файлов
            Список файлов можно передать в виде параметров скрипта
            Если в параметрах файлы не указаны, берутся все из директории скрипта
        """
        import sys
        import os
        import glob

        filenames = []

        if len(sys.argv) > 1:
            for filename in sys.argv[1:]:
                if os.path.exists(filename):
                    filenames.append(filename)

        if not filenames:
            filenames = glob.glob(os.path.join(self.workdir, '*.*'))
            filenames = [x for x in filenames if
                         os.path.splitext(x)[1] in (
                             '.xls', '.xlsx',
                             '.ods')]  # Ищем только Excel файлы
            filenames = [x for x in filenames if
                         not os.path.split(x)[1].startswith(
                             '~')]  # Убираем файлы, начинающиеся с '~'

        return filenames


class ExcelValidator:
    required_sheets = ["Products", "AdditionalImages",
                       "ProductAttributes"]
    required_columns = {
        "Products": ["product_id", "name", "categories", "sku", "model",
                     "quantity", "manufacturer", "image_name",
                     "shipping", "price", "date_added", "description",
                     "meta_title", "meta_description",
                     "meta_keywords", "stock_status_id", "store_ids"],
        "AdditionalImages": ["product_id", "image", "sort_order"],
        "ProductAttributes": ["product_id", "attribute_group_id",
                              "attribute_id", "text"]
    }

    def __init__(self, workdir):
        self.workdir = workdir
        self.filenames = None

        self.data = None

    def read_excel(self):
        try:
            # Создайте пустой DataFrame, чтобы объединить данные из всех файлов
            self.data = {}
            excel_file_work = ExcelFileWork(self.workdir)
            self.filenames = excel_file_work.get_filenames()
            for filename in self.filenames:
                sheet_data = pd.read_excel(filename,
                                           sheet_name=self.required_sheets,
                                           header=0)
                if isinstance(sheet_data,
                              dict):  # Проверка, что данные успешно загружены как dict
                    self.data.update({filename: sheet_data})

        except Exception as e:
            logger.error(f"An error occurred while reading the Excel file: {e}")
            self.data = None

        return self.data

    def validate_file(self):
        if self.data is None:
            logger.error(
                "Data is not loaded. Please call 'read_excel' method first.")
            return False

        for filename in self.data.keys():
            file_dataframe = self.data[filename]
            for sheet_name in self.required_sheets:
                if not sheet_name in list(file_dataframe.keys()):
                    logger.error(
                        f"Sheet '{sheet_name}' is missing in the Excel file.")
                    return False

            for sheet_name in self.required_sheets:
                missing_columns = []
                list_keys = [re.sub(sub_locale, '', value) for value in
                             file_dataframe[sheet_name].keys()]

                keys_to_check = self.required_columns[sheet_name]
                for key_to_check in keys_to_check:
                    if key_to_check not in list_keys:
                        missing_columns.append(key_to_check)

                if missing_columns:
                    logger.error(
                        f"Missing columns in sheet '{sheet_name}': {missing_columns}")
                    return False
            logger.success(
                f"All required sheets and columns are present in the {filename} Excel file.")
            return True


class ExcelParser:
    def __init__(self, workdir):
        self.workdir = workdir
        self.data = None

    def parse_excel(self):
        logger.info("Work with Excel")
        try:
            validator = ExcelValidator(
                self.workdir)
            # Создайте объект ExcelValidator
            self.data = validator.read_excel()  # Сохраняем данные из Excel в self.data
            if validator.validate_file():
                if self.data is not None:
                    if isinstance(self.data, dict):
                        logger.success("Data loaded")
                        return True
                    else:
                        logger.error("Data is not a load")
        except Exception as e:
            logger.error(f"An error occurred while parsing the Excel file: {e}")
        return False

    def files(self):
        return self.data.keys()

    def items_from_file(self, filename):

        data_frame_products: DataFrame = self.data[filename][PRODUCTS]

        data_frame_additional_images: DataFrame = self.data[filename][
            "AdditionalImages"]
        data_frame_product_attributes: DataFrame = self.data[filename][
            "ProductAttributes"]

        print(type(data_frame_products))

        keys_to_dict = list(data_frame_products.keys())
        for product in data_frame_products.itertuples():
            dict_product = {}
            list_additional_image = []
            list_product_attribute = []

            dict_product.update(product._asdict())
            dict_product.pop("Index")
            product_id = dict_product.get("product_id")  # TODO eroor handler

            for item_additional_image in data_frame_additional_images[
                data_frame_additional_images[
                    "product_id"] == product_id].itertuples():
                temp = item_additional_image._asdict()
                temp.pop("Index")
                list_additional_image.append(temp)

            for item_product_attribute in data_frame_product_attributes[

                data_frame_product_attributes[
                    "product_id"] == product_id].itertuples():
                temp = item_product_attribute._asdict()
                temp.pop("Index")
                list_product_attribute.append(temp)

            dict_product.update({"additional_image": list_additional_image,
                                 "product_attribute": list_product_attribute})

            yield dict_product
