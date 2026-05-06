# Generators - yield produces values one at a time (lazy)

def simple_gen():
    yield 1
    yield 2
    yield 3

# Use in a loop
for val in simple_gen():
    print(val)

# Or call next() manually
gen = simple_gen()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# Generator expression (like list comprehension with parentheses)
squares_gen = (x ** 2 for x in range(5))
squares_list = [x ** 2 for x in range(5)]

print(list(squares_gen))  # [0, 1, 4, 9, 16]
print(squares_list)       # [0, 1, 4, 9, 16]

# Practical example - Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
