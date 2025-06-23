
Selection (IF) is the construct used to make decisions in a program. These decisions are based on Boolean conditions (True or False).

<img src="images/condition.png" width="400">
<br><br>

## IF Condition
```python
age = int(input("Enter Age"))
if age < 10 :
	print("You are below 10 years")
```
<br>

## IF ELSE Condition
```python
age = int(input("Enter Age"))
if age < 10 :
	print("You are below 10 years")
else:
	print("You are 10 years or above")
```
<br>

## IF ELIF ELSE Condition
```python
age = int(input("Enter Age"))
if age < 10 :
	print("You are below 10 years")
elif age < 20:
	print("You are below 20 years")
else :
	print("You are 20 years or above")
```
<br>

## NESTED Condition
```python
age = int(input("Enter Age"))
if age < 10 :
	print("You are below 10 years")
else :
	if age < 20:
		print("You are below 20 years")
	else :
		print("You are 20 years or above")
```


<br><br>