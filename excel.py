# -*- coding: utf-8 -*-
import xlrd
import functools


def execl_rows(sheet):
    workbook = xlrd.open_workbook(r'D:\test\account.xlsx')
    index = workbook.sheet_by_index(sheet)
    rows = index.nrows
    return rows


def read_excel(rowx, colx):
    workbook = xlrd.open_workbook(r'D:\test\account.xlsx')
    index = workbook.sheet_by_index(0)
    value = index.cell_value(rowx, colx)
    return value


a = execl_rows.__name__
print(a)
