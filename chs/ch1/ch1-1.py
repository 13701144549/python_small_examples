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

@decorate_division
def test_callable():
    # 是否可调用
    print('callable(int):', callable(int))    # callable(int): True
    print("callable('wo')", callable('wo'))   # callable('wo') False
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name

        def __call__(self, *args, **kwargs):
            print('I can be called')
            print(f'my name is {self.name}')
    t = Student('001', 'xiaoming')
    t()

@decorate_division
def test_chr():
    """十进制数转ascii"""
    print('chr(65)', chr(65))

@decorate_division
def test_ord():
    """ascii转化成十进制数"""
    print('ord("A")', ord('A'))

@decorate_division
def test_classmethod():
    """类方法 classmethod 不需要实例化，不需要self参数"""
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name

        def __call__(self, *args, **kwargs):
            print('I can be called')
            print(f'my name is {self.name}')

        @classmethod
        def f(cls):
            print('classmethod')
            print(cls)
    Student.f()

@decorate_division
def test_exec():
    """将字符串编译成pytho能识别或可执行的代码"""
    s = "print('hello world')"
    r = compile(s, "<string>", "exec")
    print(r)
    exec(r)

@decorate_division
def test_complex():
    """创建一个复数"""
    c = complex(1, 2)
    print("复数：", c)

@decorate_division
def test_attr():
    """动态删除对象的属性"""
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name

        def __call__(self, *args, **kwargs):
            print('I can be called')
            print(f'my name is {self.name}')
    t = Student('001', 'xiaoming')
    print("t is id:", hasattr(t, 'id'))
    delattr(t, 'id')
    print("t is id:", hasattr(t, 'id'))

@decorate_division
def test_dict():
    """创建字典"""
    print('dict 1:',dict())
    print('dict 2:',dict(a='a', b='b'))
    print('dict 3:',dict(zip(['a', 'b'], [1, 2])))
    print('dict 4:',dict([('a', 1), ('b', 2)]))

@decorate_division
def test_dir():
    """查看对象的所有方法"""
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name

        def __call__(self, *args, **kwargs):
            print('I can be called')
            print(f'my name is {self.name}')
    t = Student('001', 'xiaoming')
    print('dir t:', dir(t))

@decorate_division
def test_divmod():
    """取余数和商"""
    print('divmod(10, 3)', divmod(10, 3))

@decorate_division
def test_enumerate():
    # l = ['a', 'b', 'c']
    l = dict(a='1', b='2')
    for i, v in enumerate(l):
        print(i, v)

if __name__ == '__main__':
    # test_abs()    # 1
    # test_all()    # 2
    # test_any()    # 3
    # test_repr()   # 4
    # test_bin()    # 5
    # test_oct()    # 6
    # test_hex()    # 7
    # test_int()    # 8
    # test_bytes()  # 9
    # test_callable()    # 10
    # test_chr()           # 11
    # test_ord()           # 12
    # test_classmethod()           # 13
    # test_exec()           # 14
    # test_complex()           # 15
    # test_attr()           # 16
    # test_dict()           # 17
    # test_dir()           # 18
    # test_divmod()           # 19
    test_enumerate()           # 20