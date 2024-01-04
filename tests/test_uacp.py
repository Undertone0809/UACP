import uacp
import pytest
from uacp import function1, function2, Class1, Class2


def test_function1():
    assert uacp.function1('test') == 'expected_result'

def test_function2():
    assert uacp.function2(1, 2) == 3

def test_class1():
    obj = uacp.Class1()
    assert obj.method1('test') == 'expected_result'
    assert obj.method1('test') == 'expected_result'
    assert obj.method1("test") == "expected_result"

def test_class2():
    obj = uacp.Class2()
    assert obj.method2(1, 2) == 3
    assert obj.method2(1, 2) == 3
    assert obj.method2(1, 2) == 3
