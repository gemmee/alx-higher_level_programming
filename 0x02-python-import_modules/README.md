# 0x02-python-import_modules

## Resources
`Read or watch`
  - [Modules](https://docs.python.org/3/tutorial/modules.html)
  - [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)

## Learning Objectives
  - Why Python programming is awesome
  - How to import functions from another file
  - How to use imported functions
  - How to create a module
  - How to use the built-in function `dir()`
  - How to prevent code in your script from being executed when imported
  - How to use command line arguments with your Python programs

## `Tasks`

## [0-add.py](./0-add.py)
> Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition `1 + 2 = 3`
  - You have to use print function with string format to display integers
  - You have to assign:
      - the value 1 to a variable called a
      - the value 2 to a variable called b
      - and use those two variables as arguments when calling the functions add and print
  - a and b must be defined in 2 different lines: a = 1 and another b = 2
  - Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
  - You can only use the word add_0 once in your code
  - You are not allowed to use * for importing or `__import__`
  - Your code should not be executed when imported - by using `__import__`, like the example below

```
gamachu@ubuntu:~$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

gamachu@ubuntu:~$ ./0-add.py
1 + 2 = 3
gamachu@ubuntu:~$ cat 0-import_add.py
__import__("0-add")
gamachu@ubuntu:~$ python3 0-import_add.py 
gamachu@ubuntu:~$ 
```

## [1-calculation.py](./1-calculation.py)
Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

  - Do not use the function print (with string format to display integers) more than 4 times
  - You have to define:
      - the value 10 to a variable a
      - the value 5 to a variable b
      - and use those two variables only, as arguments when calling functions (including print)
  - a and b must be defined in 2 different lines: a = 10 and another b = 5
  - Your program should call each of the imported functions. See example below for format
  - the word calculator_1 should be used only once in your file
  - You are not allowed to use * for importing or `__import__`
  - Your code should not be executed when imported

```
gamachu@ubuntu:~$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

gamachu@ubuntu:~$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
gamachu@ubuntu:~$
```

## [2-args.py](./2-args.py)
> Write a program that prints the number of and the list of its arguments.
  - The output should be:
    - Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
    - `:` (or `.` if no arguments were passed) followed by
    - a new line, followed by (if at least one argument),
    - one line per argument:
        - the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
  - Your code should not be executed when imported
  - The number of elements of argv can be retrieved by using: len(argv)
  - You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
```
gamachu@ubuntu:~$ ./2-args.py 
0 arguments.
gamachu@ubuntu:~$ ./2-args.py Hello
1 argument:
1: Hello
gamachu@ubuntu:~$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
gamachu@ubuntu:~$ 
```

## [3-infinite_add.py](./3-infinite_add.py)
> Write a program that prints the result of the addition of all arguments

  - The output should be the result of the addition of all arguments, followed by a new line
  - You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
  - Your code should not be executed when imported
```
gamachu@ubuntu:~$ ./3-infinite_add.py
0
gamachu@ubuntu:~$ ./3-infinite_add.py 79 10
89
gamachu@ubuntu:~$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
gamachu@ubuntu:~$ 
```
  - Remember how you did do it in C? `#pythoniscool`

## [4-hidden_discovery.py](4-hidden_discovery.py)
> Write a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc) (please download it locally).

  - You should print one name per line, in alpha order
  - You should print only names that do not start with `__`
  - Your code should not be executed when imported
  - Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)
```
gamachu@ubuntu:~$ curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"
gamachu@ubuntu:~$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
gamachu@ubuntu:~$ 
```

## [5-variable_load.py](./5-variable_load.py)
> Write a program that imports the variable a from the file variable_load_5.py and prints its value.

  - You are not allowed to use * for importing or `__import__`
  - Your code should not be executed when imported
```
gamachu@ubuntu:~$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

gamachu@ubuntu:~$ ./5-variable_load.py
98
gamachu@ubuntu:~$
```

## `Advanced Tasks`

## [100-my_calculator.py](./100-my_calculator.py)
> Write a program that imports all functions from the file calculator_1.py and handles basic operations.

  - Usage: ./100-my_calculator.py a operator b
      - If the number of arguments is not 3, your program has to:
           - print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line
           - exit with the value 1
      - operator can be:
           - `+` for addition
           - `-` for subtraction
           - `*` for multiplication
           - `/` for division
      - If the operator is not one of the above:
           - print Unknown operator. Available operators: +, -, * and / followed with a new line
           - exit with the value 1
      - You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
      - The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
  - You are not allowed to use * for importing or __import__
  - Your code should not be executed when imported
```
gamachu@ubuntu:~$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

gamachu@ubuntu:~$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
gamachu@ubuntu:~$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
gamachu@ubuntu:~$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
gamachu@ubuntu:~$
```
## [101-easy_print.py](./101-easy_print.py)
> Write a program that prints #pythoniscool, followed by a new line, in the standard output.

  - Your program should be maximum 2 lines long
  - You are not allowed to use print or eval or open or import sys in your file 101-easy_print.py
```
gamachu@ubuntu:~$ ./101-easy_print.py
#pythoniscool
gamachu@ubuntu:~$ 
```

## [102-magic_calculation.py](./102-magic_calculation.py)
> Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

```
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
  - *Tip*: [Python Bytecode](https://docs.python.org/3.4/library/dis.html)

## [103-fast_alphabet.py](./103-fast_alphabet.py)
> Write a program that prints the alphabet in uppercase, followed by a new line.

  - Your program should be maximum 3 lines long
  - You are not allowed to use:
    - any loops
    - any conditional statements
    - str.join()
    - any string literal
    - any system calls
```
gamachu@ubuntu:~$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
gamachu@ubuntu:~$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
gamachu@ubuntu:~$
```
---
# `JUST FOR FUN`
```
>>> import os
>>> os.system('ls')
0-add.py          100-my_calculator.py  102-magic_calculation.py  3-infinite_add.py      README.md    calculator_1.py           variable_load_5.py
0-import_add.py   101-easy_print.py     103-fast_alphabet.py      4-hidden_discovery.py  __pycache__  hidden_4.pyc
1-calculation.py  101-easy_print2.py    2-args.py                 5-variable_load.py     add_0.py     magic_calculation_102.py
0
>>> os.system('cat 102-magic_calculation.py -n')
     1  #!/usr/bin/python3
     2  def magic_calculation(a, b):
     3      from magic_calculation_102 import add, sub  # LOAD_CONST((add, sub)); IMPORT_NAME(magic_calculation_102); IMPORT_FROM(add); STORE_FAST(add); IMPORT_FROM(sub); STORE_FAST(sub); POP_TOP
     4      if a < b:  # LOAD_FAST(a); LOAD_FAST(b); COMPARE_OP(<); POP_JUMP_IF_FALSE (line_10)
     5          c = add(a, b)  # LOAD_FAST(add), LOAD_FAST (a); LOAD_FAST(b); CALL_FUNCTION(add); STORE_FAST(c)
     6          for i in range(4, 6):  # SETUP_LOOP(to line_8); LOAD_GLOBAL(range); LOAD_CONST(4); LOAD_CONST(6); CALL_FUNCTION(range); GET_ITER; FOR_ITER(to line_7); STORE_FAST(i)
     7              c = add(c, i)  # LOAD_FAST(add); LOAD_FAST(c); LOAD_FAST(i); CALL_FUNCTION(add); STORE_FAST(c); JUMP_ABSOLUTE(for_iter); POP_BLOCK
     8          return c  # LOAD_FAST(c); RETURN_VALUE
     9      else:
    10          return sub(a, b)  # LOAD_FAST(sub); LOAD_FAST(a), LOAD_FAST(b); CALL_FUNCTION(sub); RETURN_VALUE;
    11
0
>>> magic = __import__('102-magic_calculation')
>>> magic
<module '102-magic_calculation' from '/home/kiit/Desktop/alx/alx-higher_level_programming/0x02-python-import_modules/102-magic_calculation.py'>
>>> import dis
>>> dis.dis(magic)
Disassembly of magic_calculation:
  3           0 LOAD_CONST               1 (0)
              2 LOAD_CONST               2 (('add', 'sub'))
              4 IMPORT_NAME              0 (magic_calculation_102)
              6 IMPORT_FROM              1 (add)
              8 STORE_FAST               2 (add)
             10 IMPORT_FROM              2 (sub)
             12 STORE_FAST               3 (sub)
             14 POP_TOP

  4          16 LOAD_FAST                0 (a)
             18 LOAD_FAST                1 (b)
             20 COMPARE_OP               0 (<)
             22 POP_JUMP_IF_FALSE       64

  5          24 LOAD_FAST                2 (add)
             26 LOAD_FAST                0 (a)
             28 LOAD_FAST                1 (b)
             30 CALL_FUNCTION            2
             32 STORE_FAST               4 (c)

  6          34 LOAD_GLOBAL              3 (range)
             36 LOAD_CONST               3 (4)
             38 LOAD_CONST               4 (6)
             40 CALL_FUNCTION            2
             42 GET_ITER
        >>   44 FOR_ITER                14 (to 60)
             46 STORE_FAST               5 (i)

  7          48 LOAD_FAST                2 (add)
             50 LOAD_FAST                4 (c)
             52 LOAD_FAST                5 (i)
             54 CALL_FUNCTION            2
             56 STORE_FAST               4 (c)
             58 JUMP_ABSOLUTE           44

  8     >>   60 LOAD_FAST                4 (c)
             62 RETURN_VALUE

 10     >>   64 LOAD_FAST                3 (sub)
             66 LOAD_FAST                0 (a)
             68 LOAD_FAST                1 (b)
             70 CALL_FUNCTION            2
             72 RETURN_VALUE
             74 LOAD_CONST               0 (None)
             76 RETURN_VALUE

>>> magic.magic_calculation(4, 2)
2
>>> magic.magic_calculation(2, 4)
15
>>>
>>> # Let's remove the comments from 102-magic_calculation.py
>>> os.system('vi 102-magic_calculation.py')
0
>>> os.system('cat -n 102-magic_calculation.py') # after removing the comment part
     1  #!/usr/bin/python3
     2  def magic_calculation(a, b):
     3      from magic_calculation_102 import add, sub
     4      if a < b:
     5          c = add(a, b)
     6          for i in range(4, 6):
     7              c = add(c, i)
     8          return c
     9      else:
    10          return sub(a, b)
    11
0
>>> os.system('cat -n magic_calculation-102.py') # I created this file for testing
cat: magic_calculation-102.py: No such file or directory
256
>>> os.system('cat -n magic_calculation_102.py') # I created this file for testing
     1  #!/usr/bin/python3
     2  def add(a, b):
     3      return a + b
     4  def sub(a, b):
     5      return a - b
     6  if __name__ == '__main__':
     7      print(add(1, 2))
     8      print(sub(2, -1))
     9
0
>>> import magic_calculation_102 as magic2 # note that it's not executed when imported
>>> magic2.add(4, 2)
6
>>> magic2.sub(2, -1)
3
>>> dis.dis('magic2')
  1           0 LOAD_NAME                0 (magic2)
              2 RETURN_VALUE
>>> dis.dis(magic2)
Disassembly of add:
  3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE

Disassembly of sub:
  5           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_SUBTRACT
              6 RETURN_VALUE

>>> os.system('python3 -c "import dis as d; d.dis(magic_calculation_102)"')
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'magic_calculation_102' is not defined
256
>>> os.system('python3 -c "import dis as d; import magic_calculation_102 as m;  d.dis(m)"')
Disassembly of add:
  3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE

Disassembly of sub:
  5           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_SUBTRACT
              6 RETURN_VALUE

0
>>> os.system('git add 102-magic_calculation.py')
0
>>> os.system('git commit -m "Debytecode:) the python bytecode"')
[master f2d1d88] Debytecode:) the python bytecode
 1 file changed, 11 insertions(+)
 create mode 100755 0x02-python-import_modules/102-magic_calculation.py
0
>>> os.system('git push')
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 498 bytes | 498.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:GEMMEE/alx-higher_level_programming.git
   23b1294..f2d1d88  master -> master
0
>>>
>>> quit()
gamachu@ubuntu:~$
```
---
Author: g**A**m**A**ch**U**
