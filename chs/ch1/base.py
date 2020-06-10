# coding=utf-8
# -*- coding:utf-8 -*-
# @Time         : 2020/6/10 11:18 AM
# @Description  : 

# 装饰器
def decorate_division(func):
    def _(*args, **kwargs):
        print('=========%s start=========' % func.__name__)
        ret = func(*args, **kwargs)
        print('=========%s finish=========' % func.__name__)
        return ret
    return _