# -*- coding: utf-8 -*-

import unittest
import confighttp
import basehttp
import xlrd
import xlwt
from xlutils.copy import copy
import configparser
import json


class DataStruct:

    pass

test_data = DataStruct()
test_data.url = ''
test_data.params = {}
test_data.expected_result = {}
test_data.result = ''


class TestInterfaceCase(unittest.TestCase):
    def setUp(self):
        base_http = basehttp.BaseHttp('config.ini')
        self.config_http = confighttp.ConfigHttp(base_http.get_host(), base_http.get_port())

    def test_get_diffcheckcode(self):
        header = {}
        self.config_http.set_header(header)

        response = self.config_http.get(url=test_data.url, params=test_data.params)
        if {} == response:
            test_data.result = 'Error'
            # error_num += 1
            return
        try:
            self.assertEqual(response['msg'], test_data.expected_result, msg='exception')
            test_data.result = 'Pass'
            # success_num += 1
        except AssertionError:
            test_data.result = 'Fail'
            # fail_num += 1

    def test_get_checkcode(self):
        header = {}
        self.config_http.set_header(header)

        response = self.config_http.post(test_data.url, test_data.params)
        if {} == response:
            test_data.result = 'Error'
            # error_num += 1
            return
        try:
            print(response['msg'])
            print(test_data.expected_result)
            self.assertEqual(response['msg'], test_data.expected_result, msg='exception')
            test_data.result = 'Pass'
            # success_num += 1
        except AssertionError:
            test_data.result = 'Fail'
            # fail_num += 1

    def tearDown(self):
        pass


def get_test_suite(index):
    test_suite = unittest.TestSuite()
    func = sheet1.row_values(index)[8]
    test_suite.addTest(TestInterfaceCase(func))
    return test_suite


def run_case(sheet, runner, config_file=''):
    # report_case_total = 0
    config = configparser.ConfigParser()
    config.read(config_file)
    try:
        run_mode = config['DEFAULT']['runmode']
        run_mode = int(run_mode)
        # report_run_mode = run_mode
    except Exception:
        print('error happened in case_config')

    if True == run_mode:
        test_case_num = sheet.nrows

        for index in range(1, test_case_num):
            test_data.url = sheet.row_values(index)[4]
            test_data.params = sheet.row_values(index)[5]
            test_data.expected_result = sheet.row_values(index)[6]
            test_suite = get_test_suite(index)
            runner.run(test_suite)

            sheet1_w.write(index, 7, test_data.result)
            excel_w.save('D:\\test\\testcase.xls')

            # sheet1.put_cell(index, 7, 1, test_data.result, 0)

            # report_case_total += 1

    else:
        try:
            case_list = config['DEFAULT']['index']
            case_list = eval(case_list)
            # report_case_list = case_list
        except Exception:
            print('error happened in case_config')

        for index in case_list:
            test_data.url = sheet.row_values(index)[4]
            test_data.params = sheet.row_values(index)[5]
            test_data.expected_result = sheet.row_values(index)[6]
            test_suite = get_test_suite(index)
            runner.run(test_suite)

            sheet1_w.write(index, 7, test_data.result)
            excel_w.save('D:\\test\\testcase.xls')
            # sheet1.put_cell(index, 7, 1, test_data.result, 0)

            # report_case_total += 1


if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    excel = xlrd.open_workbook('D:\\test\\testcase.xls')
    sheet1 = excel.sheet_by_index(0)
    excel_w = copy(excel)
    sheet1_w = excel_w.get_sheet(0)

    run_case(sheet1, runner, 'case_config.ini')
    print(test_data.result)
