
Python's dictionaries are kind of hash table type. They consist of key-value pairs.
A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

```python
dict = {'age': '20', 'name': 'abc'}
```
<br>

```python
dict={}
dict['name']='abc'
dict['age']='20'
print(dict)

{'age': '20', 'name': 'abc'}
```
<br>

```python
dict = {'name':'abc','age':30,'dept':'it'}
print(dict)
print(dict['name'])
print(dict.keys())
print(dict.values())

{'age': 30, 'name': 'abc', 'dept': 'it'}
abc
dict_keys(['age', 'name', 'dept'])
dict_values([30, 'abc', 'it'])
```
<br>

```python
dict = {'name':'abc','age':30,'dept':'it'}
dict['age']=40
print(dict)
dict['add']='address1'
print(dict)
del dict['add']
print(dict)
dict.clear()
# del dict
print(dict)

{'age': 40, 'name': 'abc', 'dept': 'it'}
{'age': 40, 'add': 'address1', 'name': 'abc', 'dept': 'it'}
{'age': 40, 'name': 'abc', 'dept': 'it'}
{}
```
<br>

```python
d = {'name':'abc','age':30,'dept':'it'}
print(len(d))
print(d)
print(str(d))
print(type(d))
print(dict.items())
print(dict.keys())
print(dict.values())
d2 = {'name':'def','age':20}
d.update(d2)
print(d)

3
{'age': 30, 'name': 'abc', 'dept': 'it'}
{'age': 30, 'name': 'abc', 'dept': 'it'}
<class 'dict'>
dict_items([('age', 30), ('name', 'abc'), ('dept', 'it')])
dict_keys(['age', 'name', 'dept'])
dict_values([30, 'abc', 'it'])
{'age': 20, 'name': 'def', 'dept': 'it'}
```
<br>

```python
dict1 = {
    "market":
    {
        "name":"market1",
        "dimension1":
        {
            "table":"product",
            "fields":"product_id,product_code,product_desc",
            "keys":
            [
                {"pk":"product_id","sk":"product_id,product_code,product_desc","order":0},
                {"pk":"product_level1_id","sk":"product_level1_id","order":1},
                {"pk":"product_level2_id","sk":"product_level2_id","order":2},
                {"pk":"product_level3_id","sk":"product_level3_id","order":3}
            ]
        },
        "dimension2":
        {
            "table":"store",
            "fields":"store_id"
        }
    }
}
# print(dict1)
print(dict1.keys())
# print(dict1.values())
print(dict1.items())
```

<br><br>
```python
for key1, value1 in dict1.items():
    if dict1[key1]['name'].lower() == 'market1':
        # dimension1
        for dict2 in dict1[key1]['dimension1']['keys']: #list
            for key2, value2 in dict2.items():
                if key2 == 'sk':
                    if 'product_desc' in value2.split(','):
                        l_pk = dict2['pk']
                        l_sk = dict2['sk']
                        l_order = dict2['order']
                        l_table = dict1[key1]['dimension1']['table']
                        l_subject = 'dimension1'
                        print([l_subject, l_table, l_pk, l_sk, l_order])

['dimension1', 'product', 'product_id', 'product_id, product_code, product_desc', 0]
```

<br><br>
<b>Dictionary Functions</b>

*	dict.clear()
*	dict.copy()
*	dict.fromkeys()
*	dict.get(key, default=None)
*	dict.has_key(key)
*	dict.items()
*	dict.keys()
*	dict.setdefault(key, default=None)
*	dict.update(dict2)
*	dict.values()


<br><br>