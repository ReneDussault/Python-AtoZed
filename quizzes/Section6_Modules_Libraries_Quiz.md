# Section 6: Modules and Libraries Quiz
**Time Limit: 15 minutes | Total Points: 20**

---

## Multiple Choice Questions (12 points)

### 1. Which statement imports the entire math module?
a) from math import *  
b) import math  
c) include math  
d) Both a and b

### 2. How do you import only the sqrt function from the math module?
a) import math.sqrt  
b) from math import sqrt  
c) import sqrt from math  
d) include sqrt

### 3. What file must be present in a directory to make it a Python package?
a) package.py  
b) __init__.py  
c) module.py  
d) index.py

### 4. Which statement imports the random module with an alias?
a) import random as rnd  
b) from random import rnd  
c) import random = rnd  
d) alias random as rnd

## Code Analysis Questions (8 points)

### 5. What will this code output?
```python
import math
print(math.pi)
```
a) 3.14  
b) 3.141592653589793  
c) pi  
d) Error

### 6. What will this code do?
```python
from datetime import datetime
now = datetime.now()
```
a) Create a datetime object with current time  
b) Print current time  
c) Import the time  
d) Error

### 7. If you have a module my_module.py with a function hello(), how do you call it after import my_module?
a) hello()  
b) my_module.hello()  
c) my_module->hello()  
d) call my_module.hello()

### 8. What's the purpose of if __name__ == "__main__": in a module?
a) Define the main function  
b) Code runs only when file is executed directly  
c) Import other modules  
d) Create a class

---

## Answer Key
1. d) Both a and b
2. b) from math import sqrt
3. b) __init__.py
4. a) import random as rnd
5. b) 3.141592653589793
6. a) Create a datetime object with current time
7. b) my_module.hello()
8. b) Code runs only when file is executed directly