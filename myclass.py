#!/usr/bin/env python
# encoding: utf-8
import os

# def sum(x, y):
#    return x + y


# def sub(x, y):
#    return x - y
s_value = 'abc\ts\tdevice\n'
a = s_value.strip()
print(a)
b = a[:a.find('device')].strip()
print(b)
