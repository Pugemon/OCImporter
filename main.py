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


def main():
    logger.info("test")
    ocimporter = OCImporter()
    ocimporter.work_with_excel()


if __name__ == '__main__':
    main()