
## Print

### Quotation
```python
print('Hello World!')
print("Hello World!")
print("""Hello 
		World!""")
```
<br>

### Concatenation
Concatenation of strings means to join multiple strings together.<br>
This is done using the "+" Operator
```python
print("Hello" + "Python") --> HelloPython

print("Hello", "Python") --> Hello Python
```
<br>


### Escape Character
```python
print("Hello! Welcome to\n Python world.")

# \t(Tab), \"(print double quote), \'(print single quote)
```
<br>


### Arguments

#### Argument END
```python
print("My name is ", end="")
print("Monty Python.")
# My name is Monty Python
```

#### Argument SEP
```python
print("My", "name", "is", "Monty", "Python.", sep="-")
# My_name_is_Monty_Python
```
<br><br><br>


## INPUT
```python
marks = input('Enter Marks')
print(marks)
```

#### Type Casting
```python
marks = input('Enter Marks')
print(marks + 10)

# Try again
marks = int(input('Enter Marks'))
print(marks + 10)
```
<br><br>


## Comments
```python
# First comment
print('Hello World!') # second comment
```


<br><br>