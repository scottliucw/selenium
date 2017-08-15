# -*- coding: utf-8 -*-

import requests


class ConfigHttp:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.headers = {}

    def set_header(self, headers):
        self.headers = headers

    def get(self, url, params):
        url = 'http://' + self.host + ':' + str(self.port) + url
        params = eval(params)
        request = requests.get(url=url, params=params)
        try:
            response = request.json()
            return response
        except Exception:
            print('no data returned')
            return {}

    def post(self, url, params):
        url = 'http://' + self.host + ':' + str(self.port) + url
        params = eval(params)
        request = requests.post(url=url, params=params)
        try:
            response = request.json()
            return response
        except Exception:
            print('no data returned')
            return {}
