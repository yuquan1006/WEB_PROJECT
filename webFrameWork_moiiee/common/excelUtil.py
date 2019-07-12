#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
# 读取excel文件传入ddt 进行数据驱动
import config.globalConfig as gc
import xlrd
class ExcelUtil(object):
    def __init__(self):
        self.book = xlrd.open_workbook(gc.login_testdata)
        self.sheet = self.book.sheet_by_name(gc.login_sheet)
        self.rowNum = self.sheet.nrows
        self.colNum = self.sheet.ncols
        self.keys = self.sheet.row_values(0)


    def get_data(self):
        if self.rowNum <= 1:
            print("excel文件总行数不得小于等于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                value = self.sheet.row_values(j)
                # print(value)
                for k in range(self.colNum):
                    s[self.keys[k]] = value[k]
                r.append(s)
                j += 1
        print(r)
        return r


if __name__ == '__main__':
    a = ExcelUtil()

    a.get_data()