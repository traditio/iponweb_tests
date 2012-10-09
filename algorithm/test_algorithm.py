from nose.tools import eq_

import algorithm


def test_change_priority_for_existing_item():
    q = [[1, 'item']]
    algorithm._change_priority(q, 2, 'item')
    eq_(q, [[2, 'item']])


def test_change_priority_for_non_existing_item_in_empty_q():
    q = []
    algorithm._change_priority(q, 2, 'item')
    eq_(q, [[2, 'item']])

def test_change_priority_for_non_existing_item_in_filled_q():
    q = [[2, 'item']]
    algorithm._change_priority(q, 2, 'item2')
    eq_(q, [[2, 'item'], [2, 'item2']])


def test_priority_for_existing_item():
    eq_(algorithm._priority([[1, '1']], '1'), 1)


def test_priority_for_non_existing_item():
    eq_(algorithm._priority([], '1'), None)


def test_traverse_path():
    eq_(algorithm._traverse_path({'2': {'1': 1}}, {'2': '1', '1': '1'}, '2'), '2 -> 1 = 1')


def test_shortest_path():
    eq_(algorithm.shortest_path({'1': {'2': 1}, '2': {'1': 1}}, '1', '2'), '2 -> 1 = 1')


if __name__ == '__main__':
    import subprocess
    import os.path
    subprocess.call(['nosetests', os.path.dirname(__file__)])