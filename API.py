# -*- coding:utf-8 -*
import requests
import json


def test():
    url = "http://api.app1.snail.com:88/backend/platform/identity/balance"  #测试的接口url
    payload = {'nUserId': '1502464001'}
    r = requests.get(url=url, params=payload)
    print(r.url)
    print(r.json())
    return r.json()


def test1():
    url = "http://api.app1.snail.com:88/backend/platform/identity/login"
    payload = {'cAccount': 'wntest560', 'cPassword': 'a123456'}
    r = requests.post(url=url, params=payload)
    print(r.url)
    print(r.json())

if __name__ == "__main__":
    test1()
