# Section 2: Data Structures Quiz
**Time Limit: 20 minutes | Total Points: 25**

---

## Multiple Choice Questions (12 points)

### 1. Which data structure is ordered and mutable?
a) Tuple  
b) Set  
c) List  
d) Dictionary

### 2. What will this code return?
```python
my_list = [1, 2, 3]
my_list[1]
```
a) 1  
b) 2  
c) 3  
d) Error

### 3. Which method adds an element to the end of a list?
a) my_list.add()
b) my_list.insert()
c) my_list.append()
d) my_list.extend()

### 4. What is the main characteristic of a set?
a) Ordered  
b) Mutable  
c) Unique elements only  
d) Key-value pairs

### 5. How do you access the value associated with key "name" in dictionary `person`?
a) person[name]
b) person["name"]
c) person.name
d) person->name

### 6. What will `len([1, 2, 3, 4])` return?
a) 3  
b) 4  
c) 5  
d) Error

## List Comprehension Questions (8 points)

### 7. What does this list comprehension create?
```python
result = [x * 2 for x in range(5)]
```
a) [0, 2, 4, 6, 8]
b) [2, 4, 6, 8, 10]
c) [0, 1, 2, 3, 4]
d) [1, 2, 3, 4, 5]

### 8. Which list comprehension creates a list of even numbers from 0 to 10?
a) [x for x in range(11) if x % 2 == 0]
b) [x for x in range(10) if x % 2 == 1]
c) [x * 2 for x in range(5)]
d) Both a and c

## Code Analysis Questions (5 points)

### 9. What will this code output?
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 5
print(my_tuple)
```
a) (5, 2, 3)
b) (1, 2, 3)
c) Error  
d) [5, 2, 3]

### 10. What will this code output?
```python
my_dict = {"a": 1, "b": 2}
print(my_dict.get("c", "Not found"))
```
a) None
b) "Not found" 
c) Error  
d) "c"

### 11. What will this code output?
```python
my_set = {1, 2, 2, 3, 3, 3}
print(len(my_set))
```
a) 6  
b) 5  
c) 3  
d) 4

---

## Answer Key
1. c) List
2. b) 2
3. c) append()
4. c) Unique elements only
5. b) person["name"]
6. b) 4
7. a) [0, 2, 4, 6, 8]
8. d) Both a and c
9. c) Error (tuples are immutable)
10. b) "Not found"
11. c) 3