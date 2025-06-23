
Iteration is the construct used to repeat sections of code. It's commonly called looping.

<img src="images/loop.png" width="400">
<br>


## Code in English (psudo-code)
```python
loop i equals 1 to 10
	output i
end loop
```
<br>


## Definite Loops
Definite iteration uses the FOR loop.

- This uses a variable to act as a counter for the loop.
- The program will assign this variable a starting value.
- Automatically increment the variable by one every time the code repeats.
- When this counter equals the final value, the loop stops.
<br><br>


```python
for i in range(1, 10):
	print(i)
 
# 1 2 3 4 5 6 7 8 9
```

```python
for i in range(10):
	print(i)
 
# 0 1 2 3 4 5 6 7 8 9
```

```python
for i in range(1, 11, 2):
	print(i)
 
# 1 3 5 7 9
```
<br><br>

## Indefinite Loops
Indefinite iteration checks a condition each time around the loop to decide whether to repeat the loop again or continue.

### WHILE loop

```python
total = 0
while total < 20:
	num = int(input("enter number"))
	total = total + num
print ("done!")
```
<br>

### Nested selection and iteration
```python
for a in range(1, 5):
	print("a = " + str(a))
		for b in range(1, 3):
			print(str(a) + " X " + str(b) + " = " + str(a * b))
 
a = 1
1 X 1 = 1
1 X 2 = 2
a = 2
2 X 1 = 2
2 X 2 = 4
a = 3
3 X 1 = 3
3 X 2 = 6
a = 4
4 X 1 = 4
4 X 2 = 8
```

```python
# Even numbers upto 20
for i in range(1, 21):
	if i % 2 == 0 :
		print(i)
# 2 4 6 8 10 12 14 16 18 20
```
<br>


## Control Statement
Python supports the following control statements:

- break statement : Terminates the loop statement and transfers execution to the statement immediately following the loop.
- continue statement : Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
- pass statement : The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

<br>
#### break statement

It terminates the current loop and resumes execution at the next statement, just like the traditional break statement in C.

The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops.

If you are using nested loops, the break statement stops the execution of the innermost loop and start executing the next line of code after the block.
 
```python
for letter in 'Python': # First Example
if letter == 'h':
	break
	print 'Current Letter :', letter

var = 10 # Second Example
while var > 0:
	print('Current variable value :', var)
	var = var -1
	if var == 5:
		break
```
 
<br>
#### continue statement
It returns the control to the beginning of the while loop.. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.

The continue statement can be used in both while and for loops.
```python 
for letter in 'Python': # First Example
if letter == 'h':
	continue
	print('Current Letter :', letter)

 
var = 10 # Second Example
while var > 0:
	var = var -1
	if var == 5:
		continue
		print('Current variable value :', var)
		
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : o
Current Letter : n
Current variable value : 9
Current variable value : 8
Current variable value : 7
Current variable value : 6
Current variable value : 4
Current variable value : 3
Current variable value : 2
Current variable value : 1
Current variable value : 0
```

<br>
#### pass statement

It is used when a statement is required syntactically but you do not want any command or code to execute.

The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet.
```python 
for letter in 'Python':
	if letter == 'h':
		pass
	print 'This is pass block'
	print 'Current Letter :', letter
 
Current Letter : P
Current Letter : y
Current Letter : t
This is pass block
Current Letter : h
Current Letter : o
Current Letter : n
```



<br><br>