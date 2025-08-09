
# Variables
Variable is a temporary memory location in which you can store data (text or numbers). 
<br>
It's like an empty box. You can put any value. Change it's content. 
<br>
This means that when you create a variable you reserve some space in memory. 

<br>

## Assigning Values to Variables
Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. For example −
```python
name = "Tom" # A string
age = 10 # An integer assignment
price = 10.50 # A floating point

print(name)
print(age)
print(price)
```

<br>

## Variable Naming Rules
- Can contain only letters[A-Z][a-z], numbers[0-9] and underscores. eg. Max_Score1
- Cannot start with a number.
- Cannot use a Python "Reserved Words" eg. print, if, class etc.
- Use meaningful names, such as "firstName" instead of "var".

<br>

## Identifiers

A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, Manpower and manpower are two different identifiers in Python.
 
Here are naming conventions for Python identifiers:

- Class names start with an uppercase letter. All other identifiers start with a lowercase letter
- Starting an identifier with a single leading underscore indicates that the identifier is private
- Starting an identifier with two leading underscores indicates a strongly private identifier
- If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

<br>

## Reserved Words

The following list shows the Python keywords. These are reserved words and you cannot use them as constant or variable or any other identifier names. All the Python keywords contain lowercase letters only.

```python
and, assert, break, class, continue, def, del, elif, else, except, exec, 
finally, for, from, global, if, import, in, is, lambda, not, or, pass, 
print, raise, return, try, while, with, yield
```

<br>

# Data Types
The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.
 
Python has few standard data types:

- Character
- String
- Integer
- Float
- Boolean
- List
- Dictionary

<br>

## Character
Character data type is able to store a single letter, number or symbol such as<br>
"A" , "b" , "$" , "3"

<br>

## String
String is a group of characters to form words or sentences

```python
name = "Harry Potter"
phone = '+44 123456789'
address = """29 Craft Avenue
Bradford, UK"""
```

<br>

## Integer
Integer is whole number, positive or negative, without decimal point. It is used for counting or storing quantities
```python
1234 is an integer
1234.0 is not an integer
```
 
<br>

## Float
Float (Real) is used for numbers, positive or negative, that have a decimal or fractional part

987.234

<br>

## Boolean
Boolean can store True or False value. It is used to indicate the result of a condition.

isRaining = False<br>
sorted = True

<br>

## List
Variable is used to store a single item of data. List allows to store multiple items of data.<br>
It contains items separated by commas, enclosed in square brackets ([]).

```python
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
``` 

<br>

## Dictionary
Python's dictionaries are kind of hash table type. Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([])

```python
dict = {'name': 'john', 'code':6734, 'dept': 'sales'}
``` 


<br><br>

