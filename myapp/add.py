# myapp/add.py

import argparse


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


def main():
    parser = argparse.ArgumentParser(
        description="一个简单的计算器 CLI 工具")
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="操作类型"
    )
    parser.add_argument("a", type=float, help="第一个数")
    parser.add_argument("b", type=float, help="第二个数")
    args = parser.parse_args()

    ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    result = ops[args.operation](args.a, args.b)
    print(f"结果: {result}")


if __name__ == "__main__":
    main()
