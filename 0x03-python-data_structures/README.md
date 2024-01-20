# 0x03-python-data_structures

## Resources
> Read or watch
  - Lists
  - Tuples
  - Sets
  - Strings
  - dictionary
  - Sequences

## Learning Objectives
> At the end of this project, I should know:
  - What are lists and how to use them
  - What are the difference and similarities betweeen strings and lists
  - What are the most common methods of lists and how to use them
  - How to use lists as stacks and queues
  - What are list comprehensions and how to use them
  - What are tuples and how to use them
  - When to use tuples versus lists
  - What is a sequence
  - What is tuple packing
  - What is sequence unpacking
  - What is the `del` statement and how to use it

# `Mandatory Tasks`

## [0-print_list_integer.py](./0-print_list_integer.py)
> Write a function that prints all integers of a list.

  - Prototype: def print_list_integer(my_list=[]):
  - Format: one integer per line. See example
  - You are not allowed to import any module
  - You can assume that the list only contains integers
  - You are not allowed to cast integers into strings
  - You have to use str.format() to print integers
```
gamachu@ubuntu:~$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

gamachu@ubuntu:~$ ./0-main.py
1
2
3
4
5
gamachu@ubuntu:~$ 
```
  - *Tip*: Observe the following bytecode of my implemention of 0-print_list_integer.py
```
gamachu@ubuntu:~$ python3 -c "from dis import dis as d; plist = __import
__('0-print_list_integer'); d(plist)"
Disassembly of print_list_integer:
  3           0 LOAD_FAST                0 (my_list)
              2 GET_ITER
        >>    4 FOR_ITER                18 (to 24)
              6 STORE_FAST               1 (i)

  4           8 LOAD_GLOBAL              0 (print)
             10 LOAD_CONST               1 ('{:d}')
             12 LOAD_METHOD              1 (format)
             14 LOAD_FAST                1 (i)
             16 CALL_METHOD              1
             18 CALL_FUNCTION            1
             20 POP_TOP
             22 JUMP_ABSOLUTE            4
        >>   24 LOAD_CONST               0 (None)
             26 RETURN_VALUE
gamachu@ubuntu:~$ cat -n 0-print_list_integer.py
     1  #!/usr/bin/python3
     2  def print_list_integer(my_list=[]):
     3      for i in my_list:
     4          print('{:d}'.format(i))
gamachu@ubuntu:~$
```

## [1-element_at.py](./1-element_at.py)
> Write a function that retrieves an element from a list like in C.

  - Prototype: def element_at(my_list, idx):
  - If idx is negative, the function should return None
  - If idx is out of range (> of number of element in my_list), the function should return None
  - You are not allowed to import any module
  - You are not allowed to use try/except
```
gamachu@ubuntu:~$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

gamachu@ubuntu:~$ ./1-main.py
Element at index 3 is 4
gamachu@ubuntu:~$
```
  - *Tip*: Observe the following bytecode of my implementation of 1-element_at.py
```
gamachu@ubuntu:~$ python3 -c "from dis import dis as d; e = __import__("1-element_at"); d(e)"
Disassembly of element_at:
  3           0 LOAD_FAST                1 (idx)
              2 LOAD_CONST               1 (0)
              4 COMPARE_OP               0 (<)
              6 POP_JUMP_IF_TRUE        20
              8 LOAD_FAST                1 (idx)
             10 LOAD_GLOBAL              0 (len)
             12 LOAD_FAST                0 (my_list)
             14 CALL_FUNCTION            1
             16 COMPARE_OP               5 (>=)
             18 POP_JUMP_IF_FALSE       24
        >>   20 LOAD_CONST               0 (None)
             22 RETURN_VALUE
        >>   24 LOAD_FAST                0 (my_list)
             26 LOAD_FAST                1 (idx)
             28 BINARY_SUBSCR
             30 RETURN_VALUE
gamachu@ubuntu:~$ cat 1-element_at.py -n
     1  #!/usr/bin/python3
     2  def element_at(my_list, idx):
     3      return None if idx < 0 or idx >= len(my_list) else my_list[idx]
gamachu@ubuntu:~$
```
 

## [2-replace_in_list.py](./2-replace_in_list.py)
> Write a function that replaces an element of a list at a specific position (like in C).

  - Prototype: def replace_in_list(my_list, idx, element):
  - If idx is negative, the function should not modify anything, and returns the original list
  - If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
  - You are not allowed to import any module
  - You are not allowed to use try/except
```
gamachu@ubuntu:~$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

gamachu@ubuntu:~$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
gamachu@ubuntu:~$
```
  - *Tip*: Observe the following bytecode of 2-replace_in_list.py (don't look at the code first)
```
gamachu@ubuntu:~$ python3 -c "from dis import dis as d; r = __import__('2-replace_in_list'); d(r)"
Disassembly of replace_in_list:
  3           0 LOAD_FAST                1 (idx)
              2 LOAD_CONST               1 (0)
              4 COMPARE_OP               0 (<)
              6 POP_JUMP_IF_TRUE        20
              8 LOAD_FAST                1 (idx)
             10 LOAD_GLOBAL              0 (len)
             12 LOAD_FAST                0 (my_list)
             14 CALL_FUNCTION            1
             16 COMPARE_OP               5 (>=)
             18 POP_JUMP_IF_FALSE       24

  4     >>   20 LOAD_FAST                0 (my_list)
             22 RETURN_VALUE

  5     >>   24 LOAD_FAST                2 (element)
             26 LOAD_FAST                0 (my_list)
             28 LOAD_FAST                1 (idx)
             30 STORE_SUBSCR

  6          32 LOAD_FAST                0 (my_list)
             34 RETURN_VALUE

gamachu@ubuntu:~$ cat 2-replace_in_list.py -n
     1  #!/usr/bin/python3
     2  def replace_in_list(my_list, idx, element):
     3      if idx < 0 or idx >= len(my_list):
     4          return my_list
     5      my_list[idx] = element
     6      return my_list
gamachu@ubuntu:~$
```

## [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)
> Write a function that prints all integers of a list, in reverse order.

  - Prototype: def print_reversed_list_integer(my_list=[]):
  - Format: one integer per line. See example
  - You are not allowed to import any module
  - You can assume that the list only contains integers
  - You are not allowed to cast integers into strings
  - You have to use str.format() to print integers
```
gamachu@ubuntu:~$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

gamachu@ubuntu:~$ ./3-main.py
5
4
3
2
1
gamachu@ubuntu:~$ 
```
  - *Tip*: Look at the following bytecode of 3-print_reversed_list_integer.py (please don't look at the code first)
```
gamachu@ubuntu:~$ python3 -c "from dis import dis as d; pr = __import__('3-print_reversed_list_integer'); d(pr)"
Disassembly of print_reversed_list_integer:
  3           0 LOAD_FAST                0 (my_list)
              2 LOAD_CONST               0 (None)
              4 COMPARE_OP               8 (is)
              6 POP_JUMP_IF_FALSE       12

  4           8 LOAD_CONST               1 ('None')
             10 RETURN_VALUE

  5     >>   12 LOAD_FAST                0 (my_list)
             14 LOAD_METHOD              0 (reverse)
             16 CALL_METHOD              0
             18 POP_TOP

  6          20 LOAD_FAST                0 (my_list)
             22 GET_ITER
        >>   24 FOR_ITER                18 (to 44)
             26 STORE_FAST               1 (i)

  7          28 LOAD_GLOBAL              1 (print)
             30 LOAD_CONST               2 ('{:d}')
             32 LOAD_METHOD              2 (format)
             34 LOAD_FAST                1 (i)
             36 CALL_METHOD              1
             38 CALL_FUNCTION            1
             40 POP_TOP
             42 JUMP_ABSOLUTE           24
        >>   44 LOAD_CONST               0 (None)
             46 RETURN_VALUE

gamachu@ubuntu:~$ cat 3-print_reversed_list_integer.py -n
     1  #!/usr/bin/python3
     2  def print_reversed_list_integer(my_list=[]):
     3      if my_list is None:
     4          return 'None'
     5      my_list.reverse()
     6      for i in my_list:
     7          print('{:d}'.format(i))
gamachu@ubuntu:~$
```


## [4-new_in_list.py](./4-new_in_list.py)
> Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

   - Prototype: def new_in_list(my_list, idx, element):
   - If idx is negative, the function should return a copy of the original list
   - If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
   - You are not allowed to import any module
   - You are not allowed to use try/except
```
gamachu@ubuntu:~$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

gamachu@ubuntu:~$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
gamachu@ubuntu:~$ 
```
  - *Tip*: Observe the following bytecode of 4-new_in_list.py
```
gamachu@ubuntu:~$ python3 -c "from dis import dis as d; copy = __import__('4-new_in_list'); d(copy)"
Disassembly of new_in_list:
 11           0 LOAD_FAST                0 (my_list)
              2 LOAD_CONST               1 (None)
              4 LOAD_CONST               1 (None)
              6 BUILD_SLICE              2
              8 BINARY_SUBSCR
             10 STORE_FAST               3 (copy_list)

 12          12 LOAD_CONST               2 (0)
             14 LOAD_FAST                1 (idx)
             16 DUP_TOP
             18 ROT_THREE
             20 COMPARE_OP               1 (<=)
             22 POP_JUMP_IF_FALSE       36
             24 LOAD_GLOBAL              0 (len)
             26 LOAD_FAST                0 (my_list)
             28 CALL_FUNCTION            1
             30 COMPARE_OP               0 (<)
             32 POP_JUMP_IF_FALSE       48
             34 JUMP_FORWARD             4 (to 40)
        >>   36 POP_TOP
             38 JUMP_FORWARD             8 (to 48)

 13     >>   40 LOAD_FAST                2 (element)
             42 LOAD_FAST                3 (copy_list)
             44 LOAD_FAST                1 (idx)
             46 STORE_SUBSCR

 14     >>   48 LOAD_FAST                3 (copy_list)
             50 RETURN_VALUE

gamachu@ubuntu:~$ cat -n 4-new_in_list.py
     1  #!/usr/bin/python3
     2  def new_in_list(my_list, idx, element):
     3      """
     4      Replaces an element in a list at a specific position without modifying
     5      the original list(like in C).
     6
     7      my_list: reference to the original list
     8      idx: index of at which element is replaced
     9      element: new element for replace
    10      """
    11      copy_list = my_list[:]  # same as my_list.copy()
    12      if 0 <= idx < len(my_list):
    13          copy_list[idx] = element
    14      return copy_list
gamachu@ubuntu:~$
```

## [5-no_c.py](./5-no_c.py)
> Write a function that removes all characters c and C from a string.

  - Prototype: def no_c(my_string):
  - The function should return the new string
  - You are not allowed to import any module
  - You are not allowed to use str.replace()
```
gamachu@ubuntu:~$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

gamachu@ubuntu:~$ ./5-main.py
Best Shool
hiago
 is fun!
gamachu@ubuntu:~$ 
```
  - *Tip*: Observe the following bytecode for my implementation of 5-no_c.py

```
gamachu@ubuntu:~$  python3 -c "from dis import dis as d; noc = __import__('5-no_c'); d(noc)"
Disassembly of no_c:
  9           0 LOAD_CONST               1 ('')
              2 STORE_FAST               1 (str)

 10           4 LOAD_FAST                0 (my_string)
              6 GET_ITER
        >>    8 FOR_ITER                20 (to 30)
             10 STORE_FAST               2 (x)

 11          12 LOAD_FAST                2 (x)
             14 LOAD_CONST               2 ('cC')
             16 COMPARE_OP               7 (not in)
             18 POP_JUMP_IF_FALSE        8

 12          20 LOAD_FAST                1 (str)
             22 LOAD_FAST                2 (x)
             24 INPLACE_ADD
             26 STORE_FAST               1 (str)
             28 JUMP_ABSOLUTE            8

 13     >>   30 LOAD_FAST                1 (str)
             32 RETURN_VALUE
gamachu@ubuntu:~$ cat 5-no_c.py -n
     1  #!/usr/bin/python3
     2  def no_c(my_string):
     3      '''
     4      Removes all characters c and C from a string.
     5      Without using str.replace()
     6
     7      my_string: the string to be modified
     8      '''
     9      str = ''
    10      for x in my_string:
    11          if x not in "cC":
    12              str += x
    13      return str
gamachu@ubuntu:~$
```

## [6-print_matrix_integer.py](./6-print_matrix_integer.py)
> Write a function that prints a matrix of integers.

  - Prototype: def print_matrix_integer(matrix=[[]]):
  - Format: see example
  - You are not allowed to import any module
  - You can assume that the list only contains integers
  - You are not allowed to cast integers into strings
  - You have to use str.format() to print integers
```
gamachu@ubuntu:~$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

gamachu@ubuntu:~$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
gamachu@ubuntu:~$ 
```
  - *Tip*: Observe the following bytecode:
```
gamachu@ubuntu:~$

gamachu@ubuntu:~$
```


