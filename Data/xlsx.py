import pandas as pd

from config import logger


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
                         os.path.splitext(x)[1] in ('.xls', '.xlsx', '.ods')]  # Ищем только Excel файлы
            filenames = [x for x in filenames if
                         not os.path.split(x)[1].startswith('~')]  # Убираем файлы, начинающиеся с '~'
        return filenames


class ExcelValidator:
    def __init__(self, workdir):
        self.workdir = workdir
        self.filenames = None
        self.required_sheets = ["Products", "AdditionalImages", "ProductAttributes"]
        self.required_columns = {
            "Products": ["product_id", "name", "categories", "sku", "model", "quantity", "manufacturer", "image_name",
                         "shipping", "price", "date_added", "description", "meta_title", "meta_description",
                         "meta_keywords", "stock_status_id", "store_ids"],
            "AdditionalImages": ["product_id", "image", "sort_order"],
            "ProductAttributes": ["product_id", "attribute_group_id", "attribute_id", "text"]
        }
        self.data = None

    def read_excel(self):
        try:
            # Создайте пустой DataFrame, чтобы объединить данные из всех файлов
            self.data = pd.DataFrame()
            excel_file_work = ExcelFileWork(self.workdir)
            self.filenames = excel_file_work.get_filenames()
            for filename in self.filenames:
                sheet_data = pd.read_excel(filename, sheet_name=self.required_sheets)
                if isinstance(sheet_data, dict):  # Проверка, что данные успешно загружены как dict
                    for sheet_name, columns in sheet_data.items():


        except Exception as e:
            logger.error(f"An error occurred while reading the Excel file: {e}")
            self.data = None

        return self.data

    def validate_file(self):
        if self.data is None:
            logger.error("Data is not loaded. Please call 'read_excel' method first.")
            return False

        for sheet_name in self.required_sheets:
            if sheet_name not in self.data:
                logger.error(f"Sheet '{sheet_name}' is missing in the Excel file.")
                return False

            sheet_data = self.data[sheet_name]
            missing_columns = [col for col in self.required_columns[sheet_name] if col not in sheet_data.columns]

            if missing_columns:
                logger.error(f"Missing columns in sheet '{sheet_name}': {missing_columns}")
                return False

        logger.success("All required sheets and columns are present in the Excel file.")
        return True


class ExcelParser:
    def __init__(self, workdir):
        self.workdir = workdir
        self.data = None

    def parse_excel(self):
        logger.info("Work with Excel")
        try:
            validator = ExcelValidator(self.workdir)  # Создайте объект ExcelValidator
            self.data = validator.read_excel()  # Сохраняем данные из Excel в self.data
            if validator.validate_file():
                if self.data is not None:
                    if isinstance(self.data, pd.DataFrame):
                        df = self.data
                        logger.success("Data loaded")
                        df.info()
                    else:
                        logger.error("Data is not a DataFrame.")
        except Exception as e:
            logger.error(f"An error occurred while parsing the Excel file: {e}")