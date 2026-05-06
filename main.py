# List Comprehensions - Concise way to create lists

# Basic list comprehension
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition (if)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# With condition (if-else)
nums = [x if x % 2 == 0 else -x for x in range(5)]
print(nums)  # [0, -1, 2, -3, 4]

# Nested list comprehension (flatten 2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Nested loops (create 2D list)
table = [[i + j for j in range(3)] for i in range(3)]
print(table)  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# String operations
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Extract specific property
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6]

# Dictionary comprehension
square_dict = {x: x ** 2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Swap key-value pairs
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# Set comprehension (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}

# Complex filtering
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x * 2 for x in data if x > 5 and x % 2 == 1]
print(result)  # [12, 14, 18]

# Multiple conditions
words = ["apple", "banana", "cherry", "date"]
filtered = [w for w in words if len(w) > 4 and 'a' in w]
print(filtered)  # ['apple', 'banana', 'cherry']

# List comprehension with functions
def double(x):
    return x * 2

doubled = [double(x) for x in range(5)]
print(doubled)  # [0, 2, 4, 6, 8]

# Comparison: Loop vs List Comprehension
# Using loop
result_loop = []
for x in range(5):
    result_loop.append(x ** 2)

# Using list comprehension
result_comp = [x ** 2 for x in range(5)]
print(result_loop == result_comp)  # True

# Generator expression (memory efficient, lazy)
gen = (x ** 2 for x in range(5))
print(gen)  # <generator object...>
print(list(gen))  # [0, 1, 4, 9, 16]

# Nested dictionary/list
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]
names = [s['name'] for s in students]
high_scorers = [s['name'] for s in students if s['score'] > 80]
print(names)  # ['Alice', 'Bob', 'Charlie']
print(high_scorers)  # ['Alice', 'Bob']

# Transform list of tuples
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums_only = [num for num, _ in pairs]
chars_only = [char for _, char in pairs]
print(nums_only)  # [1, 2, 3]
print(chars_only)  # ['a', 'b', 'c']
