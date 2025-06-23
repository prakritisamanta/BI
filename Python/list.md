
Variable is used to store a single item of data. List allows to store multiple items of data.<br>
It contains items separated by commas, enclosed in square brackets ([]).

To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.
<br><br>

```python
arr = ["Apple", "Orange", "Banana", "Pears", "Grapes"]
for i in range(0, 4):
	print(arr[i])
```
<br>

```python
scores = [5,7,0,10,8,3,7,3]
total = 0
for x in range(8):
	total = total + scores[x]
print(total)
```
<br>

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0.

```python
list1 = ['abc',123,2.2,'def',2]
print(list1)
print(list1[0])
print(list1[1:3])
print(list1[3:])
print(list1[:3])
print(list1*2)
list2 = ['a','b']
print(list1 + list2)
list1[1] = 456
print(list1)
del list1[1]
print(list1)

['abc', 123, 2.2, 'def', 2]
abc
[123, 2.2]
['def', 2]
['abc', 123, 2.2]
['abc', 123, 2.2, 'def', 2, 'abc', 123, 2.2, 'def', 2]
['abc', 123, 2.2, 'def', 2, 'a', 'b']
['abc', 456, 2.2, 'def', 2]
['abc', 2.2, 'def', 2]
```
<br>

```python
list1 = ['abc',123,2.2,'def',2]
print(len(list1))
print(['hi']*4)
print('def' in list1)
for i in list1: print(i) - List Comprehesion

5
['hi', 'hi', 'hi', 'hi']
True
abc
123
2.2
def
2
```
<br>

```python
list1 = ['abc',123,2.2,'def',2]
list2 = [1,2,3]
# print(cmp(list1,list2))
print(len(list1))
print(max(list2))

5
3
```
<br>

```python
l1 = ['abc',123,2.2,'def',2]
l1.append(2)
print(l1)
print(l1.count(2))
print(l1.index(2))
l1.insert(2,10)
print(l1)
l1.remove(10)
print(l1)
l1.reverse()
print(l1)
l2 = [2,3,1,2,3]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)

['abc', 123, 2.2, 'def', 2, 2]
2
4
['abc', 123, 10, 2.2, 'def', 2, 2]
['abc', 123, 2.2, 'def', 2, 2]
[2, 2, 'def', 2.2, 123, 'abc']
[1, 2, 2, 3, 3]
[3, 3, 2, 2, 1]
```
<br>

```python
l1=['a','b','c']
# str = ''.join("z." + str(s) + "," for s in l1).strip(',')
str = ''.join(s+',' for s in l1)
print(str)

a,b,c,
```
<br>

```python
l1=['a','b','c']
l2=['1','2','3']
l3=[]
for i in range(len(l1)):
    a=l1[i]
    l3.append([l1[i]+','+l2[i]])
print(l3)

[['a,1'], ['b,2'], ['c,3']]
```
<br>

```python
l1=[['aaa'], ['bbb'],['ccc', 'ddd']]
for i in l1:
    for j in i:
        if j.find('ccc') != -1:
            print('present')

present
```

<br><br>
<b>List Functions</b>

*	cmp(list1, list2)
*	len(list)
*	max(list)
*	min(list)
*	list(seq)
*	list.append(obj)
*	list.count(obj)
*	list.extend(seq)
*	list.index(obj)
*	list.insert(index, obj)
*	list.pop(obj=list[-1])
*	list.remove(obj)
*	list.reverse()
*	list.sort([func])

<br><br>
