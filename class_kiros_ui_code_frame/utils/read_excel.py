# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 10:50
@Auth:kirosbaby
@QQ:308902181
"""
import xlrd
from conf.config import get_path


class Read_Excel():
    def __init__(self, num,*args):
        book = xlrd.open_workbook(get_path(*args))
        self.sheets = book.sheet_by_index(num)

    def read_data(self, row, col):
        return self.sheets.cell_value(row, col)


if __name__ == '__main__':
    r_excel = Read_Excel(0,'data', 'Data.xlsx')
    print(r_excel.read_data(1, 0))