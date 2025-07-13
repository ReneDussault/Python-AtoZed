# Python A-to-Z Final Comprehensive Quiz
**Time Limit: 60 minutes | Total Points: 100**

---

## PART A: Basic Syntax & Data Types (15 points)

### 1. What will this code output? (3 points)
```python
x = "5"
y = 3
print(x + str(y))
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

### 3. What's the result of 10 // 3 * 2? (2 points)
a) 6  
b) 6.67  
c) 6.0  
d) 7

### 4. Which comparison returns True? (3 points)
a) 5 == "5"  
b) 5 != "5"  
c) "hello" > "world"  
d) None == False

### 5. What's the correct f-string syntax? (5 points)
```python
name = "Python"
age = 30
```
a) f"Hello {name}, you are {age} years old"  
b) "Hello {name}, you are {age} years old".format()  
c) "Hello " + name + ", you are " + str(age) + " years old"  
d) All are correct

---

## PART B: Data Structures (20 points)

### 6. What will this code output? (5 points)
```python
data = [1, [2, 3], 4]
print(data[1][1])
```
a) 1  
b) 2  
c) 3  
d) Error

### 7. Which list comprehension creates squares of even numbers 0-10? (5 points)
a) [x**2 for x in range(11) if x % 2 == 0]  
b) [x for x in range(11) if x**2 % 2 == 0]  
c) [(x**2) % 2 == 0 for x in range(11)]  
d) [x**2 % 2 == 0 for x in range(11)]

### 8. What will this code output? (5 points)
```python
my_dict = {"a": 1, "b": 2}
my_dict.update({"c": 3, "a": 10})
print(my_dict)
```
a) {"a": 1, "b": 2, "c": 3}  
b) {"a": 10, "b": 2, "c": 3}  
c) Error  
d) {"a": [1, 10], "b": 2, "c": 3}

### 9. Which operation removes duplicates from a list? (5 points)
a) list(set(my_list))  
b) my_list.unique()  
c) remove_duplicates(my_list)  
d) my_list.distinct()

---

## PART C: Flow Control (20 points)

### 10. What will this code output? (8 points)
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

### 11. What will this code output? (7 points)
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

### 12. Which exception handling is correct? (5 points)
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

---

## PART D: Functions (15 points)

### 13. What will this code output? (8 points)
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

### 14. What's equivalent to this lambda? (4 points)
```python
func = lambda x: x**2 if x > 0 else 0
```
a) ```python
   def func(x):
       return x**2 if x > 0 else 0
   ```
b) ```python
   def func(x):
       if x > 0:
           return x**2
       else:
           return 0
   ```
c) Both a and b  
d) Neither

### 15. What happens with this function call? (3 points)
```python
def divide(a, b):
    return a / b

result = divide(b=10, a=20)
```
a) Error  
b) 2.0  
c) 0.5  
d) 200

---

## PART E: Object-Oriented Programming (20 points)

### 16. What will this code output? (10 points)
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

### 17. What's the purpose of @property decorator? (5 points)
a) Makes method private  
b) Makes method static  
c) Allows method to be accessed like an attribute  
d) Makes method abstract

### 18. Which demonstrates composition? (5 points)
a) class Car(Vehicle): pass  
b) class Car: def __init__(self): self.engine = Engine()  
c) class Car: @staticmethod def info(): pass  
d) class Car: pass

---

## PART F: Modules and Libraries (10 points)

### 19. What will this code output? (5 points)
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

### 20. Which import statement is most specific and recommended? (5 points)
a) from math import *  
b) import math  
c) from math import sqrt, pi  
d) import math.sqrt

---

## BONUS QUESTIONS (10 points)

### 21. What will this advanced code output? (5 points)
```python
numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
print(result)
```
a) [4, 16]  
b) [2, 4]  
c) [1, 9, 25]  
d) [1, 4, 9, 16, 25]

### 22. What design pattern does this represent? (5 points)
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

---

## Answer Key

**PART A:** 1-b, 2-c, 3-a, 4-b, 5-d  
**PART B:** 6-c, 7-a, 8-b, 9-a  
**PART C:** 10-b, 11-b, 12-d  
**PART D:** 13-a, 14-c, 15-b  
**PART E:** 16-b, 17-c, 18-b  
**PART F:** 19-b, 20-c  
**BONUS:** 21-a, 22-b

---

## Grading Scale
- 90-100: Excellent (A)
- 80-89: Good (B)  
- 70-79: Satisfactory (C)
- 60-69: Needs Improvement (D)
- Below 60: Needs Significant Review (F)

## Study Recommendations by Score:
- **Below 60:** Review all sections, practice basic concepts
- **60-69:** Focus on weak areas identified in quiz
- **70-79:** Practice advanced problems and real-world applications  
- **80-89:** Explore Python libraries and frameworks
- **90-100:** Ready for advanced Python topics and projects!