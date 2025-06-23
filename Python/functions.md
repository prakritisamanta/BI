
When programs grow in size, they can become hard to manage. Ideally, larger programs should be broken down into functions.
<br>

![Subroutines](images/function.png){: style="height:300px"}
<br>

When a function is called, control passes from the main program to the function. Once the function has completed, control is passed back to the main program.
<br><br>


## Defining Function
A function is a section of code that is defined outside the main body. It can be called as many times as required.

```python
# function to produce a printed times table
def TimesTable():
	for i in range(1, 11):
		print(str(i) + " X 5 = " + str(i * 5))

# Calling
TimesTable()

# Output
1 X 5 = 5
2 X 5 = 10
3 X 5 = 15
4 X 5 = 20
5 X 5 = 25
6 X 5 = 30
7 X 5 = 35
```
<br>


## Passing parameters
In the last example, the brackets were empty but they can be used to pass parameters into the function.

We can rewrite the previous function with parameters to control which times table to produce.

```python
def TimesTable(tt):
  for i in range(1, 11):
    print(str(i) + " X " + str(tt) + " = " + str(i * tt))

TimesTable(8)

1 X 8 = 8
2 X 8 = 16
3 X 8 = 24
4 X 8 = 32
5 X 8 = 40
6 X 8 = 48
7 X 8 = 56
8 X 8 = 64
9 X 8 = 72
10 X 8 = 80
```
<br>


## Return Values
A function can return value back to the main program when it returns control. This value can then be used in the main program.

```python
def circle_area(radius):
 PI = 3.14159
 area = PI * radius**2
 return area

area = circle_area(5)
print(area)
```
<br>


## Local variables
Variables which only exist within the function and cannot be accessed by the main program are called local variables.

In the circle_area() subroutine, the values area and pi are both used within the subroutine definition. These variables have local scope.

```python
def circle_area(radius):
 PI = 3.14159
 area = PI * (radius**2)
 return area

print(circle_area(10))
print(area)
```
<br>


## Global variable
A variable declared outside any function is often global by default, but it can usually be declared explicitly with a keyword such as 'global'.

It can be accessed, changed or updated by any part of the code. On the other hand, a 'local' variable can only be accessed by the function in which it is declared. This means that the same variable name can be used in different function and modules without any issues.
<br><br>


## Advantages of the structured approach
Splitting programs down into multiple functions rather than one large program is known as modularised or structured programming.

Advantages of structured approach:

- It reduces the overall size of the program.
- It makes the code much easier to maintain.
- It reduces development and testing.
- It allows reuse of code between programs


<br><br><br>