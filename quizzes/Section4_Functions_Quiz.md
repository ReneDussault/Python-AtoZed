# Section 4: Functions Quiz
**Time Limit: 20 minutes | Total Points: 25**

---

## Multiple Choice Questions (12 points)

### 1. Which keyword is used to define a function in Python?
a) function
b) def
c) func
d) define

### 2. What does the `return` statement do?
a) Prints a value  
b) Ends function execution and sends back a value  
c) Creates a variable  
d) Starts a function

### 3. What happens if a function doesn't have a return statement?
a) Error occurs  
b) Returns None
c) Returns 0  
d) Returns empty string

### 4. Which is the correct syntax for a lambda function that adds two numbers?
a) lambda x, y: x + y
b) lambda(x, y): x + y
c) def lambda x, y: x + y
d) lambda x + y`

## Code Analysis Questions (8 points)

### 5. What will this function return?
```python
def mystery(x):
    return x * 2

result = mystery(5)
```
a) 5  
b) 10  
c) 25  
d) Error

### 6. What will this code output?
```python
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())
```
a) Hello, !
b) Hello, World!
c) Error  
d) Hello, name!

### 7. What will this code output?
```python
def add(a, b):
    print(a + b)

result = add(3, 4)
print(result)
```
a) 7, None  
b) 7, 7  
c) None, 7  
d) 7

### 8. What will this lambda function return when called with `(3, 4)`?
```python
multiply = lambda x, y: x * y
result = multiply(3, 4)
```
a) 7  
b) 12  
c) 34  
d) Error

## Function Design Questions (5 points)

### 9. Which function signature correctly accepts any number of arguments?
a) def func(args)
b) def func(*args)
c) def func(**args)
d) def func(args[])

### 10. What's the main advantage of using functions?
a) Faster execution  
b) Less memory usage  
c) Code reusability  
d) Better graphics

---

## Answer Key
1. b) def
2. b) Ends function execution and sends back a value
3. b) Returns None
4. a) lambda x, y: x + y
5. b) 10
6. b) Hello, World!
7. a) 7, None
8. b) 12
9. b) def func(*args)
10. c) Code reusability