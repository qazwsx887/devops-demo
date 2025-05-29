# tests/test_add.py

from myapp.add import add, subtract, multiply, divide
import pytest  #使用了一个叫 pytest 的第三方测试框架，它可以自动执行以 test_ 开头的函数，并判断里面写的 assert 是否为真。

def test_add():
    assert add(2, 3) == 5  #assert 的意思是“断言”——如果 add(2, 3) 不是 5，测试就会失败，提示你函数出错。

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():  #这个测试专门就是为了确认程序是否会在出错时正确地抛出 ValueError。如果没抛出，或者抛出了别的错误，测试也会失败。
    with pytest.raises(ValueError):
        divide(5, 0)

