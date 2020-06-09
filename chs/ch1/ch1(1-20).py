# coding=utf-8
# -*- coding:utf-8 -*-
# @Time         : 2020/6/9 11:05 AM
# @Description  : Python基础

# 装饰器
def decorate_division(func):
    def _(*args, **kwargs):
        print('=========%s start=========' % func.__name__)
        ret = func(*args, **kwargs)
        print('=========%s finish=========' % func.__name__)
        return ret
    return _

@decorate_division
def test_abs():
    # 求绝对值 绝对值或复数的摸
    print('abs(-5):', abs(-5))    # abs(-5): 5

@decorate_division
def test_all():
    # 元素都为真，如果可迭代对象的所有元素都为真，那么返回True，否则返回False
    print('all([1, 2, 0, 5])', all([1, 2, 0, 5]))   # all([1, 2, 0, 5]) False
    print('all([1, 2, '', 5])', all([1, 2, '', 5]))  # all([1, 2, , 5]) False
    print('all([1, 2, 5])', all([1, 2, 5]))   # all([1, 2, 5]) True

@decorate_division
def test_any():
    # 元素至少一个为真　接受一个可迭代对象，如果可迭代对象里至少有一个元素为真，
    # 那么返回True，否则返回False
    print('any([0, 0, ''])', any([0, 0, '']))   # any([0, 0, ]) False
    print('any([1, 2, 0])', any([1, 2, 0]))  # any([1, 2, 0]) True

@decorate_division
def test_repr():
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name
    james = Student('001', 'james')
    print(james)   # id = 001, name = james

@decorate_division
def test_bin():
    # 十进制转二进制
    print('bin(10):', bin(10))    # bin(10): 0b1010

@decorate_division
def test_oct():
    # 十进制转八进制
    print('oct(10):', oct(10))    # oct(10): 0o12

@decorate_division
def test_hex():
    # 十进制转十六进制
    print('hex(10):', hex(10))    # hex(10): 0xa

@decorate_division
def test_int():
    # 十六进制转十进制
    print("int('0xa', 16):", int('0xa', 16))    # int('0xa', 16): 10
    # 八进制转十进制
    print("int('0o12', 8):", int('0o12', 8))    # int('0o12', 8): 10
    # 二进制转十进制
    print("int('0b1010', 2):", int('0b1010', 2))  # int('0b1010', 2): 10

@decorate_division
def test_bytes():
    # 字符串转化成字节类型
    s = 'apple'
    print('bytes(apple): ', bytes(s, encoding='utf-8'))    # bytes(apple):  b'apple'

# def test_callable
if __name__ == '__main__':
    # test_abs()
    # test_all()
    # test_any()
    # test_repr()
    # test_bin()
    # test_oct()
    # test_hex()
    # test_int()
    test_bytes()
