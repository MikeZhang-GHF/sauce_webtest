from os.path import exists

from xlrd import open_workbook
from yaml import safe_load, safe_load_all

import settings


class File:
    """base class for different file readers"""

    def __init__(self, file_path: str):
        if not exists(file_path):
            raise FileNotFoundError
        self._file_path = file_path
        self._data = None


class YamlReader(File):

    def __init__(self, yml_path, multi=False):
        super().__init__(yml_path)
        self._multi = multi

    @property
    def data(self):
        # check data has been loaded
        if not self._data:
            with open(self._file_path, 'rb') as fp:
                # yaml data is multi-level
                if self._multi:
                    # generator to list
                    self._data = list(safe_load_all(fp))
                else:
                    self._data = safe_load(fp)

        return self._data


class ExcelReader(File):

    def __init__(self,
                 excel_path: str,
                 sheet: [str, int],
                 excel_header: bool = True):
        """
        for example:
        A    B    C
        A1  B1    C1
        A2  B2    C2
        ExcelReader(path, sheet=0).data
        [{A:A1, B:B1, C:C1}, {A:A2, B:B2, C:C2}]

        :param excel_path: Excel file path
        :param sheet: locate sheet by index or name
        :param excel_header: include header switch True: include False: exclude
        """
        super().__init__(excel_path)
        self._sheet = sheet
        self._excel_header = excel_header
        self._data = []

    @property
    def data(self):
        if not self._data:
            work_book = open_workbook(self._file_path)
            if not isinstance(self._sheet, (int, str)):
                raise TypeError(
                    f'excel sheet: {self._sheet} does not exist.'
                )
            if isinstance(self._sheet, int):
                sheet = work_book.sheet_by_index(self._sheet)
            else:
                sheet = work_book.sheet_by_name(self._sheet)

            if self._excel_header:
                header = sheet.row_values(0)
                for col in range(1, sheet.nrows):
                    self._data.append(dict(zip(header, sheet.row_values(col))))
            else:
                for col in range(0, sheet.nrows):
                    self._data.append(sheet.row_values(col))
        return self._data


if __name__ == '__main__':
    test_data = YamlReader(settings.TEST_DATA['login']).data
    pass_data = test_data.get('pass_logins')
    print(len(pass_data))
    print(pass_data)
