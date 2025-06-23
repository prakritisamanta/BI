
Operators are the constructs which can manipulate the value of operands.
Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
 
Types of Operator

- Arithmetic Operators
- Comparison (Relational) Operators
- Boolean Operators
- Assignment Operators
- Membership Operators
<br>


## Arithmetic Operators
Assume variable a holds 10 and variable b holds 20, then
```python
+ Addition: a + b = 30
- Subtraction: a – b = -10
* Multiplication: a * b = 200
/ Division: b / a = 2
% Modulus: b % a = 0
** Exponent: a**b = 10 to the power 20
// Floor Division: 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
```
Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero.

### Operator Precedence
The order of arithmetic operations matters.<br>
Brackets, Indices, Division and Multiplication, Addition and Substraction

8 + 2 * 5 (Answer is 18)<br>
(30 - 5 * 3) / 5 (Answer is 3)
<br><br>


## Comparison Operators
These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators. Assume variable a holds 10 and variable b holds 20, then:

```python
== : (a == b) is not true.
!= : not equal
> : (a > b) is not true.
< : (a < b) is true.
>= : (a >= b) is not true.
<= : (a <= b) is true.
```
<br>


## Boolean Operators
If multiple conditions need to be evaluated, the Boolean operators (or Logical operators)<br>
AND and OR can be used.

AND operator requires both conditions to be True for the overall condition to be True.
```python
x = 6
x > 0 and x < 7
True
```

OR operator requires one or the other (or both) of the conditions to be True for the overall condition to be True.
```python
x = 5
y = 8
x/2==2 or y/4==2
True
```

A condition can be reversed using the NOT operator.
```python
x = 5
y = 8
not (x>y)
True
```
<br>


## Assignment Operators
```python
= equals: c = a + b
+= Add AND: c += a is equivalent to c = c + a
-= Subtract AND: c -= a is equivalent to c = c - a
*= Multiply AND: c *= a is equivalent to c = c * a
/= Divide AND: c /= a is equivalent to c = c / a
%= Modulus AND: c %= a is equivalent to c = c % a
**= Exponent AND: c **= a is equivalent to c = c ** a
//= Floor Division: c //= a is equivalent to c = c // a
``` 
<br>


## Membership Operators
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below
```python
in: x in y
not in: x not in y
```


<br><br>
