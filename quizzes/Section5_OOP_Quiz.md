# Section 5: Object-Oriented Programming Quiz
**Time Limit: 30 minutes | Total Points: 35**

---

## Multiple Choice Questions (20 points)

### 1. What is the special method called when an object is created?
a) `__create__`  
b) `__new__`  
c) `__init__`  
d) `__start__`

### 2. Which principle hides internal details of a class?
a) Inheritance  
b) Polymorphism  
c) Encapsulation  
d) Abstraction

### 3. What does `super()` do in a child class?
a) Creates a new object  
b) Calls parent class methods  
c) Deletes the parent class  
d) Makes the class static

### 4. Which is the correct way to create a private attribute?
a) `private name`  
b) `_name`  
c) `__name`  
d) `#name`

### 5. What is polymorphism in OOP?
a) Having multiple classes  
b) Using the same interface for different types  
c) Creating objects  
d) Inheriting from multiple classes

## Code Analysis Questions (10 points)

### 6. What will this code output?
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())
```
a) `Dog says Woof!`  
b) `Buddy says Woof!`  
c) `name says Woof!`  
d) Error

### 7. What will this code output?
```python
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

my_cat = Cat()
print(my_cat.speak())
```
a) `Some sound`  
b) `Meow`  
c) Both  
d) Error

### 8. What will this code output?
```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

c1 = Counter()
c2 = Counter()
c1.increment()
print(c1.count, c2.count)
```
a) 0, 0  
b) 1, 1  
c) 1, 0  
d) 0, 1

## Design Questions (5 points)

### 9. When should you use inheritance?
a) When classes share common attributes/methods  
b) When you want to hide data  
c) When you need faster code  
d) Always

### 10. What's the difference between composition and inheritance?
a) No difference  
b) Composition is "has-a", inheritance is "is-a"  
c) Composition is faster  
d) Inheritance is newer

---

## Answer Key
1. c) `__init__`
2. c) Encapsulation
3. b) Calls parent class methods
4. c) `__name`
5. b) Using the same interface for different types
6. b) `Buddy says Woof!`
7. b) `Meow`
8. c) 1, 0
9. a) When classes share common attributes/methods
10. b) Composition is "has-a", inheritance is "is-a"