# 0x00-python-hello_world

![](./py.c)

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

## The Zen of Python,
#### - By Tim Peters
> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than \*right\* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those!

---
## Quiz questions

0. What does this command line print?
>  >>> print(f"{98} Battery street")

- [x] 98 Battery street
- [ ] 9 Battery street
- [ ] 8 Battery street
- [ ] f"98 Battery street"

1. What does this command line print?

> >>> a = "Python is cool"
> >>> print(a[4])

- [ ] P
- [x] o
- [ ] h
- [ ] h
- [ ] n

2. What does this command line print?
>  >>> print("Holberton school")
- [ ] Holberton
- [x] Holberton school
- [ ] 'Holberton school'
- [ ] "Holberton school"

3. What does this command line print?
>  >>> a = "Python is cool"
>  >>> print(a[7:-5])
- [ ] si
- [ ] on
- [ ] Python
- [x] is
- [ ] nohtyP

4. What does this command line print?
>  >>> a = "Python is cool"
>  >>> print(a[7:])
- [ ] Python i
- [ ] cool
- [x] is cool
- [ ] Python is

5. What does this command line print?
>  >>> a = "Python is cool"
>  >>> print(a[-2])
- [ ] ol
- [x] o
- [ ] Nothing
- [ ] l

6. What does this command line print?
>  >>> a = "Python is cool"
>  >>> print(a[:6])
- [ ] Pytho
- [ ] Python is
- [ ] is cool
- [x] Python

7. What does this command line print?
>  >>> a = "Python is cool"
>  >>> print(a[0:6])
- [x] Python
- [ ] Python is
- [ ] Python is cool
- [ ] Pytho

8. What does this command line print?
>  >>> a = "Python is cool"
>  >>> print(f"{98} Battery street, {'San Francisco'})
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

---
Author: Gamachu

