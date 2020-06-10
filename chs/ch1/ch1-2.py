# coding=utf-8
# -*- coding:utf-8 -*-
# @Time         : 2020/6/10 11:09 AM
# @Description  : 

from base import decorate_division

@decorate_division
def test_eval():
    s = '1 + 2 * 2'
    print('eval(s): ', eval(s))

@decorate_division
def test_size():
    import sys
    a = {'a': 1, 'b': 2.3}
    print('a is size: ', sys.getsizeof(a))

@decorate_division
def test_filter():
    fil = filter(lambda x: x > 10, [1, 2, 12, 5, 17, 20])
    print('fil: ', fil)
    print('fil: ', list(fil))

@decorate_division
def test_frozenset():
    """创建一个不可修改的集合"""
    f = frozenset([1, 2, 3, 5, 6])
    print('f: ', f)

@decorate_division
def test_getattr():
    """动态获取对象属性"""
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name
    james = Student('001', 'james')
    print('james name: ', getattr(james, 'name'))

@decorate_division
def test_hasattr():
    """判断对象是否有这个属性"""
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name
    james = Student('001', 'james')
    print('Do james has the name?', hasattr(james, 'name'))
    print('Do james has the address?', hasattr(james, 'address'))

@decorate_division
def test_hash():
    """返回对象的哈希值"""
    print('hash: ', hash('123'))
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name
    james = Student('001', 'james')
    print('james hash: ', hash(james))

@decorate_division
def test_help():
    """返回对象的帮助文档"""
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name
    james = Student('001', 'james')
    print(help(james))

@decorate_division
def test_id():
    """返回对象的内存地址"""
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name
    james = Student('001', 'james')
    print('the id: ', id(james))

@decorate_division
def test_isinstance():
    """判断object是否是某个类的实例"""
    print('isinstance 1:', isinstance(1, int))
    print('isinstance 2:', isinstance([1, 2, 3], list))
    print('isinstance 3:', isinstance([1, 2, 3], dict))

@decorate_division
def test_issubclass():
    """父子类关系鉴定"""
    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = ' + self.id + ', name = ' + self.name

    print(issubclass(Student, object))
    print(issubclass(object, Student))

@decorate_division
def test_pow():
    """取幂运算"""
    print('2的3次方：', pow(2, 3))
    print('2的3次方再取余', pow(2, 3, 4))

@decorate_division
def test_range():
    """创建range序列"""
    print(range(10))
    print(list(range(1, 11)))

@decorate_division
def test_reversed():
    """反向迭代器"""
    l = [1, 2, 5, 0, 3, 6, 13, 11, 25]
    print(reversed(l))
    print(list(reversed(l)))

@decorate_division
def test_round():
    """四舍五入"""
    print(round(10.0222222, 3))
    print(round(10.0252222, 2))

@decorate_division
def test_slice():
    l = [1, 2, 5, 0, 3, 6, 13, 11, 25]
    my_slice_mean = slice(0, 10, 2)
    print(l[my_slice_mean])

@decorate_division
def test_calculator():
    """不使用if else 实现计算器"""
    from operator import add, sub, truediv, mul, pow
    def calculator(a, b, k):
        return {
            '+': add,
            '-': sub,
            '*': mul,
            '/': truediv,
            '**': pow,
        }[k](a, b)

    print(calculator(1, 2, '+'))
    print(calculator(4, 5, '*'))

@decorate_division
def test_swap():
    def swap(a, b):
        return b, a
    print(swap(2, 5))

@decorate_division
def test_99table():
    """打印99乘法表"""
    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d*%d=%d' % (j,i, j * i), end='\t')
        print()
    print('\n'.join(['  '.join(['%d*%d=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))
    print('\n'.join(['  '.join(['%d*%d=%-2s' % (j, i, j * i) for j in range(1, i + 1)]) for i in range(1, 10)]))

@decorate_division
def test_flatten():
    """全展开数组"""
    from collections.abc import Iterable
    def flatten(lst, out_lst = None):
        if out_lst is None:
            out_lst = []
        for i in lst:
            if isinstance(i, Iterable):
                flatten(i, out_lst)   # 递归
            else:
                out_lst.append(i)
        return out_lst

    print(flatten([[[1,2,3],[4,5]]]))


if __name__ == '__main__':
    # test_eval()      # 1
    # test_size()      # 2
    # test_filter()      # 3
    # test_frozenset()      # 4
    # test_getattr()      # 5
    # test_hasattr()      # 6
    # test_hash()      # 7
    # test_help()      # 8
    # test_id()      # 9
    # test_isinstance()      # 10
    # test_issubclass()      # 11
    # test_pow()      # 12
    # test_range()      # 13
    # test_reversed()      # 14
    # test_round()      # 15
    # test_slice()      # 16
    # test_calculator()      # 17
    # test_swap()      # 18
    # test_99table()      # 19
    test_flatten()      # 20