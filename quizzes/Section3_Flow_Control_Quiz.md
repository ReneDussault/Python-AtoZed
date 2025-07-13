# Section 3: Flow Control Quiz
**Time Limit: 25 minutes | Total Points: 30**

---

## Multiple Choice Questions (15 points)

### 1. Which statement is used to exit a loop prematurely?
a) continue
b) break
c) pass
d) return

### 2. What does the continue statement do in a loop?
a) Exits the loop  
b) Skips the current iteration  
c) Does nothing  
d) Restarts the loop

### 3. What will this code generate?
```python
range(1, 5)
```
a) [1, 2, 3, 4]
b) [1, 2, 3, 4, 5]
c) [0, 1, 2, 3, 4]
d) [2, 3, 4, 5]

### 4. Which loop is best when you don't know how many iterations you need?
a) for loop  
b) while loop  
c) do-while loop  
d) foreach loop

### 5. What is the purpose of try-except blocks?
a) To repeat code  
b) To handle errors  
c) To define functions  
d) To create loops

## Code Output Questions (10 points)

### 6. What will this code output?
```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```
a) 0, 1, 2  
b) 0, 2  
c) 1, 2  
d) 0, 1

### 7. What will this code output?
```python
x = 0
while x < 3:
    print(x)
    x += 1
```
a) 0, 1, 2  
b) 0, 1, 2, 3  
c) 1, 2, 3  
d) Infinite loop

### 8. What will this code output?
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```
a) 0, 1, 2, 3  
b) 0, 1, 2  
c) 0, 1, 2, 3, 4  
d) 1, 2, 3

### 9. What will this code output?
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error caught")
```
a) 10  
b) 0  
c) "Error caught"  
d) Program crashes

### 10. What will this code output?
```python
numbers = [1, 2, 3]
for i, num in enumerate(numbers):
    print(f"{i}: {num}")
```
a) 1: 1, 2: 2, 3: 3  
b) 0: 1, 1: 2, 2: 3  
c) 1, 2, 3  
d) 0, 1, 2

## Problem Solving Questions (5 points)

### 11. Which exception would you catch for invalid user input when converting to int?
a) ValueError
b) TypeError
c) IndexError
d) KeyError

### 12. What's the difference between range(5) and range(1, 5)?
a) No difference  
b) First includes 0, second starts from 1  
c) First generates 5 numbers, second generates 4  
d) Both b and c

---

## Answer Key
1. b) break
2. b) Skips the current iteration
3. a) [1, 2, 3, 4]
4. b) while loop
5. b) To handle errors
6. b) 0, 2
7. a) 0, 1, 2
8. b) 0, 1, 2
9. c) "Error caught"
10. b) 0: 1, 1: 2, 2: 3
11. a) ValueError
12. d) Both b and c