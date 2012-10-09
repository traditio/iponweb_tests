from collections import defaultdict
from StringIO import StringIO

from nose.tools import eq_
from mock import patch, MagicMock, PropertyMock, Mock, DEFAULT

import parallel_computing


@patch('parallel_computing.os.listdir')
@patch('parallel_computing.os.path.isfile')
def test_data_sources(isfile, listdir):
    listdir.return_value = ['1', '2']
    isfile.return_value = True
    eq_(parallel_computing.data_sources('.'), ['./1', './2'])


@patch('__builtin__.open')
def test_thread(open):
    open.return_value.__enter__.return_value = StringIO('A,1\nA,1\nB,1\n')
    open.return_value.__exit__.return_value = False
    q = MagicMock()
    parallel_computing.thread('', q)
    q.put.assert_called_once_with(defaultdict(int, A=2, B=1))


@patch.multiple('parallel_computing', data_sources=DEFAULT, thread=DEFAULT, Queue=DEFAULT)
def test_parallel_computing(data_sources, thread, Queue):
    data_sources.return_value = ['1', '2']
    m = Mock(name='Queue')
    type(m).maxsize = PropertyMock(return_value=2)
    m.get = Mock(return_value={'A': 1,'B': 1})
    Queue.return_value = m
    eq_(dict(parallel_computing.parallel_computing()), {'A': 2, 'B': 2})
    eq_(m.get.call_count, 2)


if __name__ == '__main__':
    import subprocess
    import os.path
    subprocess.call(['nosetests', os.path.dirname(__file__)])