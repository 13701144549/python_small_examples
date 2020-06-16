# coding=utf-8
# -*- coding:utf-8 -*-
# @Time         : 2020/6/11 10:48 AM
# @Description  : 

from base import decorate_division

@decorate_division
def test_divide():
    """列表等分"""
    from math import ceil
    def divide(lst, size):
        if size <= 0:
            return [lst]
        return [lst[i * size: (i + 1) * size] for i in range(ceil(len(lst) / size))]
    print('divide([1, 3, 5, 7, 9]): ', divide([1, 3, 5, 7, 9], 2))


@decorate_division
def test_filter_false():
    """列表压缩"""
    def filter_false(lst):
        return list(filter(bool, lst))

    print("filter_false([None, 0, False, '', [], 'ok', [1, 2]]): ", filter_false([None, 0, False, '', [], 'ok', [1, 2]]))

@decorate_division
def test_max_length():
    """取最长的列表"""
    def max_length(*lst):
        return max(*lst, key=lambda v: len(v))
    print('更长的列表是: ', max_length([1], [1, 2, 3], [4, 5, 7, 2, 3]))

@decorate_division
def test_top1():
    """求列表中出现频率最多的元素"""
    def top1(lst):
        return max(lst, default='列表为空', key=lambda v: lst.count(v))
    lst = [1, 3, 2, 5, 6, 7, 5, 3, 5, 8, 5]
    print('{}出现最多的元素是：{}'.format(lst, top1(lst)))


@decorate_division
def test_max_lists():
    """求多个列表中的最大元素"""
    def max_lists(*lst):
        print(max(*lst, key=lambda v: max(v)))
        return max(max(*lst, key=lambda v: max(v)))
    print('最大数是：', max_lists([1, 2, 3], [1, 1, 8], [4, 5, 5]))

@decorate_division
def test_reverse():
    """列表反转"""
    def reverse(lst):
        return lst[::-1]
    print('反转后：', reverse([1, -2, 3, 4, 1, 2]))

@decorate_division
def test_range():
    """浮点数等差数列"""
    def range(start, stop, n):
        start, stop, n = float('%.2F' % start), float('%.2F' % stop), int('%.d' %n )
        step = (stop - start) / n
        lst = [start]
        while n > 0:
            start , n = start + step, n - 1
            lst.append(round((start), 2))
        return lst

    print(range(1, 8, 10))

@decorate_division
def test_bif_by():
    ''''按条件分组'''
    def bif_by(lst, f):
        return [[x for x in lst if f(x)], [x for x in lst if not f(x)]]
    records = [25, 89, 31, 34]

    print(bif_by(records, lambda x: x<80))

@decorate_division
def test_map():
    '''使用map实现向量运算'''
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = [3, 4, 5, 6, 3, 2]
    ret_lst = list(map(lambda x, y: x*y+1, lst1, lst2))
    print(ret_lst)

@decorate_division
def test_max_pairs():
    '''值最大的字典'''
    def max_pairs(dic):
        if not dic:
            return dic
        max_val = max(map(lambda v: v[1], dic.items()))
        return [item for item in dic.items() if item[1] == max_val]

    ret = max_pairs({'a': 10, 'b': 5, 'c': 10, 'd': 9})
    print(ret)

@decorate_division
def test_merge_dict():
    '''合并两个字典'''
    def merge_dict(dict1, dict2):
        return {**dict1, **dict2}

    ret = merge_dict({'a': 1, 'b': 2}, {'c': 3})
    print(ret)

@decorate_division
def test_topn_dict():
    '''topn字典'''
    from heapq import nlargest
    def topn_dict(d, n):
        return nlargest(n, d, key=lambda k: d[k])
    ret = topn_dict({'a': 1, 'b': 2, 'c': 3, 'd': 10, 'e': 12}, 3)
    print(ret)

@decorate_division
def test_namedtuple():
    '''命名元祖'''
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y', 'z'])
    lst = [Point(1.5, 2, 3.0), Point(-0.3, -1.0, 2.1), Point(1.3, 2.8, -2.5)]
    print(lst)
    print(lst[0].x)

@decorate_division
def test_sample():
    '''样本抽样'''
    from random import randint, sample
    lst = [randint(0, 50) for _ in range(100)]
    print(lst[:5])
    lst_sample = sample(lst, 10)
    print(lst_sample)

@decorate_division
def test_shuffle():
    '''重洗数据'''
    from random import shuffle, randint
    lst = [randint(0, 50) for _ in range(100)]
    print(lst[:5])
    shuffle(lst)
    print(lst[:5])

@decorate_division
def test_chain():
    '''chain函数串联a、b和c，兼顾内存效率同时写法更加优美'''
    from itertools import chain
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    for i in chain(a, b, c):
        print(i)

@decorate_division
def test_product():
    def product(*args, repeat=1):
        pools = [tuple(pool) for pool in args] * repeat
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)
    rtn = product('xyz', '12', repeat=3)
    print(list(rtn))



if __name__ == '__main__':
    # test_divide()             # 1
    # test_filter_false()             # 2
    # test_max_length()             # 3
    # test_top1()             # 4
    # test_max_lists()             # 5
    # test_reverse()             # 6
    # test_range()             # 7
    # test_bif_by()             # 8
    # test_map()             # 9
    # test_max_pairs()             # 10
    # test_merge_dict()             # 11
    # test_topn_dict()             # 12
    # test_namedtuple()             # 13
    # test_sample()             # 14
    # test_shuffle()             # 15
    # test_chain()             # 16
    test_product()             # 17

