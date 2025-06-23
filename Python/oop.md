
## Topics

- Class
- Object
- Constructor
- Inheritance
- Encapsulation
- Polymorphism
- Data Abstraction
- Overriding
- Overloading
- Interfaces
<br><br>

<b>Object-oriented programming (OOP)</b> is a programming paradigm based on the concept of objects. The object contains both data in the form of attributes (properties) and methods (actions or behavior).

For example, A Car is an object, as it has the following properties:

- brand, price, color as attributes
- breaking, acceleration as behavior
<br><br>


## Class and Objects

<b>A class is a blueprint for the object.</b>

For example, you are creating a vehicle according to the Vehicle blueprint (template). Based on these descriptions, we can construct a car, truck, bus, or any vehicle as objects of Vehicle class.

<b>Object is an instance of a class.</b> In other words, the object is an entity that has a state and behavior.

```python
class Car:
	color = ‘Black’

obj_car = Car()
print(obj_car.color)
# Black
```
<br>


## Constructor(\__init__)

In Python, a constructor is a special type of method used to initialize the object of a Class. The constructor will be executed automatically when the object is created.

```python
class Car:
	def __init__(self, brand, color):
       	self. brand = brand
		self.color = color      

obj_car = Car(‘Honda’, ‘Black’)
print(obj_car. brand)
print(obj_car.color)
print(obj_car)
# <__main__.Person object at 0x15039e602100>
```
<br>


## \__str__() Function

The \__str__() function controls what should be returned when the class object is represented as a string.

```python
class Car:
	def __init__(self, brand, color):
       	self. brand = brand
		self.color = color      

def __str__(self):
return f"{self.brand}({self.color})"
obj_car = Car(‘Honda’, ‘Black’)
print(obj_car.color)   
#Honda(Black)
```
<br>


## Attributes

```python
class Car:
    car_type = "Sedan"                 #class attribute
    def __init__(self, brand, color):
        self. brand = brand            #instance attribute   
        self.color = color             #instance attribute
```
<br>


## Methods

So far, we’ve added the properties of the car. Now it’s time to add some behavior. Methods are the functions we use to describe the behaviour of objects.

```python
class Car:
	def __init__(self, brand, mileage):
		self.brand = brand 
		self.mileage = mileage

    def max_speed(self, speed):
        return f"The {self.name} runs at the maximum speed of {speed} miles/hr"
		
Honda = Car("Honda City", 21)
print(Honda.max_speed(150))

Skoda = Car("Skoda Octavia",13)
print(Skoda.max_speed(210))
```
<br>


## Inheritance

Inheritance is the procedure in which child class inherits the attributes and methods of parent class.  Along with the inherited properties and methods, a child class can have its own properties and methods.

```python
class Car:          #parent class
    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage} miles/l"

class BMW(Car):     #child class
    pass

class Audi(Car):     #child class
    def audi_desc(self):
        return "This is description method of class Audi."
		
obj1 = BMW("BMW", 20)
print(obj1.description())
# BMW car gives the mileage of 20 mile/l

obj2 = Audi("Audi", 15)
print(obj2.description())
print(obj2.audi_desc())
# Audi car gives the mileage of 20 mile/l
# This is description method of class Audi.
```


### Types of Inheritance

- Single Inheritance: Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
- Multilevel Inheritance: Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class. 
- Hierarchical Inheritance: Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
- Multiple Inheritance: Multiple-level inheritance enables one derived class to inherit properties from more than one base class.
<br><br>


## Encapsulation

Encapsulation is a way to ensure security. It hides the data from the access of outsiders. Such as, if an organization wants to protect an object/information from unwanted access by clients or any unauthorized person, then encapsulation is the way to ensure this.

```python
class Car:
    def __init__(self, name, mileage):
        self.__name = name              #private variable        
        self.mileage = mileage 

    def description(self):                
        return f"The {self.__name} car gives the mileage of {self.mileage} miles/l"

obj = Car("BMW", 20)

#accessing private variable via class method 
print(obj.description())

#accessing private variable directly from outside
print(obj.mileage)
print(obj.__name)  #Error accessing protected variable
```


### Name Mangling

You can still access this attribute directly using its mangled name. Name mangling is a mechanism we use for accessing the class members from outside, using "__var" as "_ClassName__var".

```python
class Car:
    def __init__(self, name, mileage):
        self.__name = name              #private variable        
        self.mileage = mileage 

    def description(self):                
        return f"The {self.__name} car gives the mileage of {self.mileage} miles/l"

obj = Car("BMW", 20)

#accessing private variable via class method 
print(obj.description())

#accessing private variable directly from outside
print(obj.mileage)
print(obj._Car__name)      #mangled name
```
<br>

__Note__: the mangling rule’s design mostly avoids accidents. But it is still possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

__Note__: protected variable (_name or _method)
Private variable (__name or __method)
<br><br>


## Polymorphism

Poly means many and morph means forms. So, Polymorphism means having many forms. In OOP it refers to the functions having the same names but carrying different functionalities.

```python
class Audi:
  def description(self):
    print("This the description function of class AUDI.")

class BMW:
  def description(self):
    print("This the description function of class BMW.")
	
audi = Audi()
bmw = BMW()
for car in (audi,bmw):
  car.description()
```
 
```python
class Bird:   
    def intro(self):
        print("There are many types of birds.")
 
    def flight(self):
        print("Most of the birds can fly but some cannot.")
 
class sparrow(Bird):
   
    def flight(self):
        print("Sparrows can fly.")
 
class ostrich(Bird):
 
    def flight(self):
        print("Ostriches cannot fly.")
 
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()
```
<br>



## Abstraction

We use Abstraction for hiding the internal details or implementations of a function and showing its functionalities only. This is similar to the way you know how to drive a car without knowing the background mechanism. Or you know how to turn on or off a light using a switch, but you don’t know what is happening behind the socket.

Any class with at least one abstract function is an abstract class. To create an abstraction class, first, you need to import the ABC class from abc module. This lets you create abstract methods inside it. ABC stands for Abstract Base Class.

You cannot create an object for the abstract class with the abstract method. For example-

```python
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self,name):
        self.name = name 

 @abstractmethod
    def price(self,x):
        pass
		
obj = Car("Honda City") 
# abstraction error
```

Now the question is, how do we use this abstraction exactly? The answer is, by using inheritance.

```python
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self,name):
        self.name = name

    def description(self):
        print("This the description function of class car.")

    @abstractmethod
    def price(self,x):
        pass
class new(Car):
    def price(self,x):
        print(f"The {self.name}'s price is {x} lakhs.")
obj = new("Honda City")

obj.description()
obj.price(25)
```
<br>


## Overriding

You can always override your parent class methods. One reason for overriding parent's methods is that you may want special or different functionality in your subclass.

```python
class Employee:
   def __init__(self,nm, sal):
      self.name=nm
      self.salary=sal
   def getName(self):
      return self.name
   def getSalary(self):
      return self.salary

class SalesOfficer(Employee):
   def __init__(self,nm, sal, inc):
      super().__init__(nm,sal)
      self.incnt=inc
   def getSalary(self):
      return self.salary+self.incnt

e1=Employee("Rajesh", 9000)
print ("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('Kiran', 10000, 1000)
print ("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))
```
<br>


## Overloading

Method overloading is an important feature of object-oriented programming. Java, C++, C# languages support method overloading, but in Python it is not possible to perform method overloading.

When you have a class with method of one name defined more than one but with different argument types and/or return type, it is a case of method overloading.

```python
class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))  #Error
```

To simulate method overloading, we can use a workaround by defining default value to method arguments as None, so that it can be used with one, two or three arguments.

```python
class example:
   def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))
```
<br>


## Interfaces

In software engineering, an interface is a software architectural pattern. An interface is like a class but its methods just have prototype signature definition without any body to implement. The recommended functionality needs to be implemented by a concrete class.

In languages like Java, there is interface keyword which makes it easy to define an interface. Python doesn't have it or any similar keyword. Hence the same ABC class and @abstractmethod decorator is used as done in an abstract class.

An abstract class and interface appear similar in Python. The only difference in two is that the abstract class may have some non-abstract methods, while all methods in interface must be abstract, and the implementing class must override all the abstract methods.

```python
from abc import ABC, abstractmethod
class demoInterface(ABC):
   @abstractmethod
   def method1(self):
      print ("Abstract method1")
      return

   @abstractmethod
   def method2(self):
      print ("Abstract method1")
      return
```

The above interface has two abstract methods. As in abstract class, we cannot instantiate an interface.

```python
class concreteclass(demoInterface):
   def method1(self):
      print ("This is method1")
      return
   
   def method2(self):
      print ("This is method2")
      return
      
obj = concreteclass()
obj.method1()
obj.method2()

# This is method1
# This is method2
```


<br><br>
