import os

from Data import xlsx
from config import configure_tortoise, logger

logger.info("Starting OCImporter")

db_conf = configure_tortoise()


class OCImporter:
    def __init__(self):
        self.workdir = os.getcwd()

    def work_with_excel(self):
        workdir = self.workdir
        excel_parser = xlsx.ExcelParser(workdir)
        excel_parser.parse_excel()
        for file in excel_parser.files():
            for item in excel_parser.items_from_file(file):
                print(item)
            pass


def main():
    logger.info("test")
    oc_importer = OCImporter()
    oc_importer.work_with_excel()


if __name__ == '__main__':
    main()
