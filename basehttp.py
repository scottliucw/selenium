# -*- coding: utf-8 -*-

import configparser


class BaseHttp:

    def __init__(self, ini_file):
        config = configparser.ConfigParser()

        config.read(ini_file)

        self.host = config['DEFAULT']['host']
        self.port = config['DEFAULT']['port']

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port

if __name__ == '__main__':
    a = BaseHttp('config.ini')
    print(a.host)
