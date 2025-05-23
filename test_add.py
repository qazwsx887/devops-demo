# test_add.py
# 这是测试文件，pytest 会自动识别 test_ 开头的文件和函数

from add import add  # 导入我们写的 add 函数

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
