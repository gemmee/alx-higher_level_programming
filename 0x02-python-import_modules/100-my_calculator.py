#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    op = argv[2]
    if op not in "+-*/":
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    else:
        result = div(a, b)
    print(f'{a} {op} {b} = {result}')
