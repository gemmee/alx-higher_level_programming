# 0x00-python-hello_world

![](./py.jpg)

## Resources

`Read or watch`:
+ [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
+ [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
+ [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt) by Derek Banas.
+ [pycodestyle](https://pypi.org/project/pycodestyle/)

## Learning Objectives

+ Why Python programming is awesome
+ Who created Python
+ Who is [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
+ Where does the name 'Python' come from
+ What is the Zen of Python
+ How to use the Python interpreter
+ How to print text and variables using print
+ How to use strings
+ What are indexing and slicing in Python
+ What is the official Python coding style and how to check your code with `pycodestyle`

## Zen
```
 The Zen of Python, by Tim Peters

 Beautiful is better than ugly.
 Explicit is better than implicit.
 Simple is better than complex.
 Complex is better than complicated.
 Flat is better than nested.
 Sparse is better than dense.
 Readability counts.
 Special cases aren't special enough to break the rules.
 Although practicality beats purity.
 Errors should never pass silently.
 Unless explicitly silenced.
 In the face of ambiguity, refuse the temptation to guess.
 There should be one-- and preferably only one --obvious way to do it.
 Although that way may not be obvious at first unless you're Dutch.
 Now is better than never.
 Although never is often better than *right* now.
 If the implementation is hard to explain, it's a bad idea.
 If the implementation is easy to explain, it may be a good idea.
 Namespaces are one honking great idea -- let's do more of those!
```

---
## Quiz questions

0. What does this command line print?
   ``` 
   >>> print(f"{98} Battery street")
   ```
- [x] 98 Battery street
- [ ] 9 Battery street
- [ ] 8 Battery street
- [ ] f"98 Battery street"

1. What does this command line print?

   ```
    >>> a = "Python is cool"
    >>> print(a[4])
   ```
- [ ] P
- [x] o
- [ ] h
- [ ] h
- [ ] n

2. What does this command line print?
   ```
    >>> print("Holberton school")
   ```
- [ ] Holberton
- [x] Holberton school
- [ ] 'Holberton school'
- [ ] "Holberton school"

3. What does this command line print?
   ```
    >>> a = "Python is cool"
    >>> print(a[7:-5])
   ```
- [ ] si
- [ ] on
- [ ] Python
- [x] is
- [ ] nohtyP

4. What does this command line print?
   ``` 
    >>> a = "Python is cool"
    >>> print(a[7:])
   ```
- [ ] Python i
- [ ] cool
- [x] is cool
- [ ] Python is

5. What does this command line print?
   ```
    >>> a = "Python is cool"
    >>>  print(a[-2])
   ```
- [ ] ol
- [x] o
- [ ] Nothing
- [ ] l

6. What does this command line print?
   ```
    >>> a = "Python is cool"
    >>> print(a[:6])
   ```
- [ ] Pytho
- [ ] Python is
- [ ] is cool
- [x] Python

7. What does this command line print?
   ```
    >>> a = "Python is cool"
    >>> print(a[0:6])
   ```
- [x] Python
- [ ] Python is
- [ ] Python is cool
- [ ] Pytho

8. What does this command line print?
   ```
    >>> a = "Python is cool"
    >>> print(f"{98} Battery street, {'San Francisco'})
   ```
- [ ] "98 Battery street, San Francisco"
- [x] 98 Battery street, San Francisco
- [ ] San Francisco Battery street, 98
- [ ] 8 Battery street, San

9. Who created Python?
- [ ] Julien Barbier
- [x] Guido van Rossum
- [ ] Yukihiro Matsumoto

---

## Tasks
#### 0-run
> Write a Shell script that runs a python script where the python file name is saved in the environment variable $PYFILE.
```
gamachu@ubuntu:~$ cat main.py
#!/usr/bin/python3
print("Best School")

gamachu@ubuntu:~$ export PYFILE=main.py
gamachu@ubuntu:~$ ./0-run
Best School
gamachu@ubuntu:~$
```

#### 1-run_inline
> Write a Shell script that runs python code where the python code will be saved in the environment variable $PYCODE.
```
gamachu@ubuntu:~$ export PYCODE='print(f"Alx SE: {90 + 11}")'
gamachu@ubuntu:~$ ./1-run_inline
Alx SE: 101
gamachu@ubuntu:~$
```

#### 2-print.py
> Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
```
gamachu@ubuntu:~$ ./2-print.py
"Programming is like building a multilingual puzzle
gamachu@ubuntu:~$
```

#### 3-print_number.py
> Complete the following source code in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
```
#!/usr/bin/python3
number = 98
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```
  - You are not allowed to cast the variable `number` into a string
  - Your code must be 3 lines long
  - You have to use f-strings.
```
gamachu@ubuntu:~$ ./3-print_number.py
98 Battery street
gamachu@ubuntu:~$
```

#### 4-print_float.py
> Complete the following source code in order to print the float stored in the variable `number` with a precision of 2 digits.
```
#!/usr/bin/python3
number = 3.14159
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```
  - You are not allowed to cast `number` to string
  - You have to use f-strings
```
gamachu@ubuntu:~$ ./4-print_float.py
Float: 3.14
gamachu@ubuntu:~$
```

#### 5-print_string.py
> Complete the following source code in order to print 3 times a string stored in the variable `str`, followed by a new line, followed by the first 9 characters of `str`, followed by a new line.
```
#!/usr/bin/python3
str = "Holberton School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```
  - You are not allowed to use any loops or conditional statement
  - Your program should be maximum of 5 lines long
```
gamachu@ubuntu:~$ ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton
gamachu@ubuntu:~$
```

#### 6-Concat.py
> Complete the following source code to print `Welcome to Holberton School!`
```
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"Welcome to {str1}!")
```
  - You are not allowed to use any loops or conditional statements.
  - You have to use the variables `str1` and `str2` in your new line of code
  - Your program should be exactly 5 lines long
```
gamachu@ubuntu:~$ ./6-concat.py
Welcome to Holberton School!
gamachu@ubuntu:~$ wc -l 6-concat.py
5 6-concat.py
gamachu@ubuntu:~$
```

#### 7-edges.py
> Complete the following source code:
```
#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```
  - You are not allowed to use any loops or conditional statements.
  - Your program should be exactly 8 lines long.
  - `word_first_3` should contain the first 3 letters of the variable `word`
  - `word_last_2` should contain the last 2 letters of the variable `word`
  - `middle_word` should contain the value of the varable `word` without the first and the last letters.

```
gamachu@ubuntu:~$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
gamachu@ubuntu:~$ wc -l 7-edges.py
8 7-edges.py
gamachu@ubuntu:~$
```

#### 8-concat_edges.py
> Complete the following source code to print `object-oriented programming with Python`, followed by a new line.
```
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(str)
```
  - You are not allowed to use any loops or conditional statements
  - Your program should be exactly 5 lines long
  - You are not allowed to create new variables
  - You are not allowed to use string literals

```
gamachu@ubuntu:~$ ./8-concat_edges.py
object-oriented programming with Python
gamachu@ubuntu:~$ wc -l 8-concat_edges.py
5 8-concat_edges.py
gamachu@ubuntu:~$
```

#### 9-easter_egg.py
> Write a Python script that prints "The Zen of Python", by Tim Peters, followed by a new line.
  - Your script should be maximum of 98 characters long.

```
gamachu@ubuntu:~$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
gamachu@ubuntu:~$ wc -l 9-easter_egg.py
98 9-easter_egg.py
gamachu@ubuntu:~$
```

## Advanced tasks (Optional)

### 101-compile
> Write a script that compiles a Python script file. The Python file name will be stored in the environment variable `$PYFILE`. The output filename has to be `PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

```
gamachu@ubuntu:~$ cat main.py
#!/usr/bin/python3
print("Best School")

gamachu@ubuntu:~$ export PYFILE=main.py
gamachu@ubuntu:~$ ./101-compile
Compiling main.py ...
gamachu@ubuntu:~$ ls
101-compile main.py main.pyc  [...]
gamachu@ubuntu:~$ cat main.pyc | zgrep -c "Best School"
1
gamachu@ubuntu:~$ od -t x1 main.pyc # OUTPUT ON MY MACHINE; IT'S SYSTEM DEPENDENT => SO IT CAN BE DIFFERENT
0000000 55 0d 0d 0a 00 00 00 00 2d 46 a9 65 28 00 00 00
0000020 e3 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0000040 00 02 00 00 00 40 00 00 00 73 0c 00 00 00 65 00
0000060 64 00 83 01 01 00 64 01 53 00 29 02 7a 0b 42 65
0000100 73 74 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72
0000120 69 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa
0000140 07 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c
0000160 65 3e 02 00 00 00 f3 00 00 00 00
0000173
gamachu@ubuntu:~$
```
  - **Tip**: [py_compile, compileall](https://docs.python.org/3/library/py_compile.html)


### 102-magic_calculation.py
> Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
  - **Tip**: [Python bytecode](https://docs.python.org/3.4/library/dis.html)


## Just for fun
```
kiit@Ubuntu:~$ python3
Python 3.8.10 (default, Nov 22 2023, 10:22:35)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> name = 'Gamachu'
>>> print(f"{name = }")
name = 'Gamachu'
>>> print(f"{name }")
Gamachu
>>> import sys
>>> sys.stdout.write("Hello Gamachu")
Hello Gamachu13
>>> sys.stdout.write("Hello Gamachu\n")
Hello Gamachu
14
>>> sys.stderr.write("How do you do?")
14
How do you do?>>>
>>> sys.stderr.write("How do you do?\n")
How do you do?
15
>>> sys.stderr.write("How do you do?")
14
How do you do?>>>
>>> name = sys.stdin.read(8)
Gamachu Abara
>>> name
'Gamachu '
>>> def magic(a, b):
...   b = a ** b
...   return (b + 9)
...
>>> import dis
>>> dis.dis(magic)
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_POWER
              6 STORE_FAST               1 (b)

  3           8 LOAD_FAST                1 (b)
             10 LOAD_CONST               1 (9)
             12 BINARY_ADD
             14 RETURN_VALUE
>>> def magic_calculation(a, b):
...
...    return 98 + a ** b
...
>>> dis.dis(magic_calculation)
  3           0 LOAD_CONST               1 (98)
              2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 BINARY_POWER
              8 BINARY_ADD
             10 RETURN_VALUE
>>> def magic2(a, b):
...   result = 98
...   result += a ** b
...   return result
...
>>> dis.dis(magic2)
  2           0 LOAD_CONST               1 (98)
              2 STORE_FAST               2 (result)

  3           4 LOAD_FAST                2 (result)
              6 LOAD_FAST                0 (a)
              8 LOAD_FAST                1 (b)
             10 BINARY_POWER
             12 INPLACE_ADD
             14 STORE_FAST               2 (result)

  4          16 LOAD_FAST                2 (result)
             18 RETURN_VALUE
>>> 
>>> def magic_calculation(a, b):
...   return (
...       98 + (a ** b))
...
>>> dis.dis(magic_calculation)
  3           0 LOAD_CONST               1 (98)
              2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 BINARY_POWER
              8 BINARY_ADD

  2          10 RETURN_VALUE
>>> def magic_calculation(a, b):
...
...   return (98 + (a ** b))
...
>>> dis.dis(magic_calculation)
  3           0 LOAD_CONST               1 (98)
              2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 BINARY_POWER
              8 BINARY_ADD
             10 RETURN_VALUE
>>> quit()
gamachu@ubuntu:~$ cat 102-magic_calculation.py
#!/usr/bin/python3
def magic_calculation(a, b):
    return 98 + a ** b
gamachu@ubuntu:~$ python3
Python 3.8.10 (default, Nov 22 2023, 10:22:35)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import importlib
>>> magic = importlib.import_module('102-magic_calcul
ation')
>>> import dis
>>> dis.dis(magic)
Disassembly of magic_calculation:
  3           0 LOAD_CONST               1 (98)
              2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 BINARY_POWER
              8 BINARY_ADD
             10 RETURN_VALUE

>>> exit() # or quit() or Ctrl + D i.e EOF
gamachu@ubuntu:~$ 
```

---
Author: Gamachu

