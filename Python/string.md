
String is a set of characters represented in the quotation marks.

```python
String: p   r   o   g   r   a   m   m   i   n   g
Index:  0   1   2   3   4   5   6   7   8   9   10
```

- has 11 characters
- 4th character is g
- g has index 3
- Index start at 0 not 1
- "gram" is found from index 3 to 6
<br><br>


## Substring
To extract characters from a string
```python
H	e	l	l	o		P	y	t	h	o	n
0	1	2	3	4	5	6	7	8	9	10	11

welcome = "Hello Python"
print(welcome[0:3]) --> Hel
print(welcome[6]) --> P
print(welcome[6:]) --> Python
print(welcome[-1]) --> n
```
<br>


## Concatenation
Concatenation of strings means to join multiple strings together.

This is done using the "+" Operator
```python
print("Hello" + "Python") --> HelloPython

print("Hello", "Python") --> Hello Python
```

### Formatting
```python
print("Hello {}").format("Python") --> Hello Python
```
<br>


## Quotation
Python accepts single ('), double (") and triple (''' or """) quotes to denote string. 
The triple quotes are used to span the string across multiple lines. For example, all the following are legal −

```python
print("Hello World!")
print('Hello World!') 
print("""Hello
World!""")
```
<br>


## Escape Character
```python
print("Hello! Welcome to\n Python world.")
```

Following table is a list of escape or non-printable characters that can be represented with backslash notation.

- \a : Bell or alert
- \b : Backspace
- \e : Escape
- \f : Formfeed
- \n : Newline
- \r : Carriage return
- \s : Space
- \t : Tab
<br><br>


## String Special Operators
Assume string variable a holds 'Hello' and variable b holds 'Python', then −

```python
+ : Concatenation - a + b will give HelloPython
* : Repetition - a*2 will give -HelloHello
a[1] : will give e
a[1:4] : will give ell
in : Membership - H in a will give 1
not in : Membership - M not in a will give 1
% : Format - Performs String formatting
```
<br>


## Type Conversion (Casting)
String conversion means converting another data type to or from the string data type
```python
x = 10
str_x = str(x)

y = "10"
int_y = int(y)

z = int("Python")
```
<br>


## String Functions

*	capitalize()
*	center(width, fillchar)
*	count(str, beg= 0,end=len(string))
*	decode(encoding='UTF-8',errors='strict')
*	encode(encoding='UTF-8',errors='strict')
*	endswith(suffix, beg=0, end=len(string))
*	expandtabs(tabsize=8)
*	find(str, beg=0 end=len(string))
*	index(str, beg=0, end=len(string))
*	isalnum()
*	isalpha()
*	isdigit()
*	islower()
*	isnumeric()
*	isspace()
*	istitle()
*	isupper()
*	join(seq)
*	len(string)
*	ljust(width[, fillchar])
*	lower()
*	lstrip()
*	maketrans()
*	max(str)
*	min(str)
*	replace(old, new [, max])
*	rfind(str, beg=0,end=len(string))
*	rindex( str, beg=0, end=len(string))
*	rjust(width,[, fillchar])
*	rstrip()
*	split(str="", num=string.count(str))
*	splitlines( num=string.count('\n'))
*	startswith(str, beg=0,end=len(string))
*	strip([chars])
*	swapcase()
*	title()
*	translate(table, deletechars="")
*	upper()
*	zfill (width)
*	isdecimal() 
<br><br>


```python
v = "hello world"
print(v.capitalize())
print(v.count('o'))
print(v.endswith('ld'))
print(v.find('o'))
print(v.find('oo'))
print(v.index('o'))
#isalpha(),isdigit(),isnumeric(),islower(),isupper(),lower(),upper()
print(len(v))
print(v.strip())
print(v.strip('d'))
print(v.split())
print(v.split("o"))

Hello world
2
True
4
-1
4
11
hello world
hello worl
['hello', 'world']
['hell', ' w', 'rld']
```


<br><br>