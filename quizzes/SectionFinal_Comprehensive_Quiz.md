# Python A-to-Z Final Comprehensive Quiz

**Time Limit: 100 minutes | Total Points: 180**

---

## PART A: Basic Syntax & Data Types (30 points)

### 1. What will this code output? (3 points)

```python
x = "5"
y = 3
print(x + y)
```

a) 8  
b) "53"  
c) 53  
d) Error

### 2. Which of these creates a multi-line string? (2 points)

a) "line1\nline2"  
b) """line1\nline2"""  
c) Both a and b  
d) Only b

### 3. What's the result of 10 // 3 \* 2? (2 points)

a) 6  
b) 6.67  
c) 6.0  
d) 7

### 4. Which comparison returns True? (3 points)

a) 5 == "5"  
b) 5 != "5"  
c) "hello" > "world"  
d) None == False

### 5. What's the correct f-string syntax? (3 points)

```python
name = "Python"
age = 30
```

a) f"Hello {name}, you are {age} years old"  
b) "Hello {name}, you are {age} years old".format()  
c) "Hello " + name + ", you are " + str(age) + " years old"  
d) All are correct

### 6. What will this string operation output? (4 points)

```python
text = "Python Programming"
print(text[7:].upper().replace("G", "X"))
```

a) "PROXRAMMINX"  
b) "PROXRAMMIXIN"  
c) "PXOGRAMMINX"  
d) "PROGRAMMXNX"

### 7. What's the result of this boolean operation? (3 points)

```python
result = (True and False) or (not False and True)
print(result)
```

a) True  
b) False  
c) Error  
d) None

### 8. Which variable name follows Python conventions? (2 points)

a) myVariable  
b) my_variable  
c) MyVariable  
d) myvariable

### 9. What will this type conversion output? (3 points)

```python
values = [1, 0, "hello", "", None]
print([bool(x) for x in values])
```

a) [True, False, True, False, False]  
b) [True, True, True, True, True]  
c) [1, 0, 1, 0, 0]  
d) Error

### 10. What are comments used for in Python? (2 points)

a) To execute code faster  
b) To explain code and make it readable  
c) To create variables  
d) To import modules

### 11. Which of these is a valid Python comment? (3 points)

a) // This is a comment  
b) /_ This is a comment _/  
c) # This is a comment  
d) <!-- This is a comment -->

---

## PART B: Data Structures (35 points)

### 12. What will this code output? (5 points)

```python
data = [1, [2, 3], 4]
print(data[1][1])
```

a) 1  
b) 2  
c) 3  
d) Error

### 13. Which list comprehension creates squares of even numbers 0-10? (5 points)

a) [x**2 for x in range(11) if x % 2 == 0]  
b) [x for x in range(11) if x**2 % 2 == 0]  
c) [(x**2) % 2 == 0 for x in range(11)]  
d) [x**2 % 2 == 0 for x in range(11)]

### 14. What will this code output? (5 points)

```python
my_dict = {"a": 1, "b": 2}
my_dict.update({"c": 3, "a": 10})
print(my_dict)
```

a) {"a": 1, "b": 2, "c": 3}  
b) {"a": 10, "b": 2, "c": 3}  
c) Error  
d) {"a": [1, 10], "b": 2, "c": 3}

### 15. Which operation removes duplicates from a list? (5 points)

a) list(set(my_list))  
b) my_list.unique()  
c) remove_duplicates(my_list)  
d) my_list.distinct()

### 16. What will this tuple operation output? (5 points)

```python
t1 = (1, 2, 3)
t2 = (4, 5)
result = t1 + t2
print(result[3])
```

a) 3  
b) 4  
c) 5  
d) Error

### 17. What will this set operation output? (5 points)

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 ^ set2)
```

a) {3, 4}  
b) {1, 2, 5, 6}  
c) {1, 2, 3, 4, 5, 6}  
d) Error

### 18. Which is the correct way to create a nested dictionary? (5 points)

a) nested = {"outer": {"inner": "value"}}  
b) nested = {outer: {inner: value}}  
c) nested = [outer: [inner: value]]  
d) nested = ("outer": ("inner": "value"))

---

## PART C: Flow Control (30 points)

### 19. What will this code output? (6 points)

```python
for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i, end=" ")
```

a) 1 2 4 5  
b) 1 2 4  
c) 1 2 3 4  
d) 1 2

### 20. What will this code output? (6 points)

```python
count = 0
while count < 3:
    count += 1
    if count == 2:
        continue
    print(count, end=" ")
```

a) 1 2 3  
b) 1 3  
c) 2 3  
d) 0 1 2

### 21. Which exception handling is correct? (4 points)

```python
try:
    value = int(input("Enter number: "))
    result = 10 / value
except:
    print("Error occurred")
```

a) Too broad exception handling  
b) Perfect exception handling  
c) Should use multiple except blocks  
d) Both a and c

### 22. What will this nested loop output? (6 points)

```python
for i in range(2):
    for j in range(3):
        if i == 1 and j == 1:
            break
        print(f"{i}{j}", end=" ")
```

a) 00 01 02 10  
b) 00 01 02 10 11 12  
c) 00 01 02 10 12  
d) 00 01 10

### 23. What will this enumerate example output? (3 points)

```python
words = ["apple", "banana"]
for i, word in enumerate(words, 1):
    print(f"{i}: {word}")
```

a) 0: apple\n1: banana  
b) 1: apple\n2: banana  
c) apple: 1\nbanana: 2  
d) Error

### 24. What happens when you use zip() with lists of different lengths? (5 points)

```python
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
result = list(zip(list1, list2))
print(result)
```

a) [(1, 'a'), (2, 'b'), (3, None), (4, None)]  
b) [(1, 'a'), (2, 'b')]  
c) Error  
d) [(1, 'a'), (2, 'b'), (3, ''), (4, '')]

---

## PART D: Functions (25 points)

### 25. What will this code output? (6 points)

```python
def mystery_func(a, b=5, *args, **kwargs):
    return a + b + sum(args) + sum(kwargs.values())

result = mystery_func(1, 2, 3, 4, x=5, y=6)
print(result)
```

a) 21  
b) 26  
c) 18  
d) Error

### 26. What's equivalent to this lambda? (4 points)

```python
func = lambda x: x**2 if x > 0 else 0
```

a) ```python
def func(x):
return x\*\*2 if x > 0 else 0

````
b) ```python
def func(x):
    if x > 0:
        return x**2
    else:
        return 0
````

c) Both a and b  
d) Neither

### 27. What happens with this function call? (3 points)

```python
def divide(a, b):
    return a / b

result = divide(b=10, a=20)
```

a) Error  
b) 2.0  
c) 0.5  
d) 200

### 28. What will this recursive function return? (4 points)

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
```

a) 10  
b) 24  
c) 16  
d) Error

### 29. What will this scope example output? (3 points)

```python
x = 10
def modify_x():
    x = 20
    return x

print(modify_x(), x)
```

a) 20 20  
b) 20 10  
c) 10 10  
d) Error

### 30. What is a docstring used for? (3 points)

a) To create variables  
b) To document and describe what a function does  
c) To import modules  
d) To handle exceptions

### 31. How many expressions can a lambda function contain? (2 points)

a) Unlimited  
b) Two  
c) One  
d) None

---

## PART E: Object-Oriented Programming (30 points)

### 32. What will this code output? (8 points)

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} starting"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} starting with engine"

my_car = Car("Toyota", "Camry")
print(my_car.start())
```

a) Toyota starting  
b) Toyota Camry starting with engine  
c) Camry starting with engine  
d) Error

### 33. What's the purpose of @property decorator? (4 points)

a) Makes method private  
b) Makes method static  
c) Allows method to be accessed like an attribute  
d) Makes method abstract

### 34. Which demonstrates composition? (4 points)

a) class Car(Vehicle): pass  
b) class Car: def **init**(self): self.engine = Engine()  
c) class Car: @staticmethod def info(): pass  
d) class Car: pass

### 35. What will this encapsulation example output? (5 points)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def __secret_method(self):
        return "Secret!"

account = BankAccount(1000)
print(account.get_balance())
print(account.__balance)
```

a) 1000\n1000  
b) 1000\nError  
c) Error\nError  
d) 1000\nSecret!

### 36. What will this polymorphism example output? (4 points)

```python
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound(), end=" ")
```

a) Woof! Meow!  
b) Dog Cat  
c) Error  
d) sound() sound()

### 37. What is the primary purpose of the `__init__` method? (5 points)

a) To delete objects from memory  
b) To initialize object attributes when an instance is created  
c) To define class variables  
d) To create static methods

---

## PART F: Modules and Libraries (20 points)

### 38. What will this code output? (5 points)

```python
import math as m
from random import randint

print(type(m.pi))
print(type(randint))
```

a) <class 'float'>, <class 'int'>  
b) <class 'float'>, <class 'function'>  
c) <class 'math'>, <class 'random'>  
d) Error

### 39. Which import statement is most specific and recommended? (4 points)

a) from math import \*  
b) import math  
c) from math import sqrt, pi  
d) import math.sqrt

### 40. What will this module example output? (6 points)

```python
# In file: my_module.py
counter = 0

def increment():
    global counter
    counter += 1
    return counter

# In main file:
import my_module
print(my_module.increment())
print(my_module.increment())
```

a) 1\n2  
b) 1\n1  
c) 0\n1  
d) Error

### 41. What file must be present to make a directory a Python package? (5 points)

a) package.py  
b) **init**.py  
c) module.py  
d) index.py

---

## BONUS QUESTIONS (25 points)

### 42. What will this advanced code output? (5 points)

```python
numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
print(result)
```

a) [4, 16]  
b) [2, 4]  
c) [1, 9, 25]  
d) [1, 4, 9, 16, 25]

### 43. What design pattern does this represent? (5 points)

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

a) Factory Pattern  
b) Singleton Pattern  
c) Observer Pattern  
d) Strategy Pattern

### 44. What will this generator function output? (5 points)

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

result = list(fibonacci(5))
print(result)
```

a) [0, 1, 1, 2, 3]  
b) [1, 1, 2, 3, 5]  
c) [0, 1, 2, 3, 5]  
d) Error

### 45. What will this decorator example output? (5 points)

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"hello, {name}!"

print(greet("world"))
```

a) hello, world!  
b) HELLO, WORLD!  
c) Hello, World!  
d) Error

### 46. What will this nested data structure operation output? (5 points)

```python
data = {
    'users': [
        {'name': 'Alice', 'scores': [85, 92, 78]},
        {'name': 'Bob', 'scores': [90, 88, 95]}
    ]
}
print(data['users'][1]['scores'][2])
```

a) 78  
b) 95  
c) 88  
d) Error

---

## Answer Key

**PART A:** 1-d, 2-c, 3-a, 4-b, 5-d, 6-a, 7-a, 8-b, 9-a, 10-b, 11-c  
**PART B:** 12-c, 13-a, 14-b, 15-a, 16-b, 17-b, 18-a  
**PART C:** 19-b, 20-b, 21-d, 22-a, 23-b, 24-b  
**PART D:** 25-a, 26-c, 27-b, 28-b, 29-b, 30-b, 31-c  
**PART E:** 32-b, 33-c, 34-b, 35-b, 36-a, 37-b  
**PART F:** 38-b, 39-c, 40-a, 41-b  
**BONUS:** 42-a, 43-b, 44-a, 45-b, 46-b

---

## Grading Scale

- 162-180: Excellent (A) - 90-100%
- 144-161: Good (B) - 80-89%
- 126-143: Satisfactory (C) - 70-79%
- 108-125: Needs Improvement (D) - 60-69%
- Below 108: Needs Significant Review (F) - Below 60%

## Study Recommendations by Score:

- **Below 108:** Review all sections, practice basic concepts daily
- **108-125:** Focus on weak areas identified in quiz, revisit fundamentals
- **126-143:** Practice advanced problems and real-world applications
- **144-161:** Explore Python libraries, frameworks, and advanced topics
- **162-180:** Ready for professional Python development and complex projects!
