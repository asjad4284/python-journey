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

# Generator that reads lines from a file
def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

# Generator that filters even numbers
def even_numbers(iterable):
    for num in iterable:
        if num % 2 == 0:
            yield num

# Generator that multiplies each value
def multiply_by(iterable, factor):
    for val in iterable:
        yield val * factor

# Chain generators together
numbers = range(1, 11)
evens = even_numbers(numbers)
doubled = multiply_by(evens, 2)
print(list(doubled))  # [4, 8, 12, 16, 20]

# Generator with two-way communication (send)
def averager():
    total = 0
    count = 0
    while True:
        value = yield total / count if count else 0
        if value is None:
            break
        total += value
        count += 1

avg = averager()
next(avg)  # Prime the generator
print(avg.send(10))     # 10
print(avg.send(20))     # 15
print(avg.send(30))     # 20

# Generator with close() to stop early
def countdown(n):
    while n > 0:
        try:
            yield n
        except GeneratorExit:
            print("Countdown cancelled!")
            raise
        n -= 1

gen = countdown(5)
print(next(gen))  # 5
print(next(gen))  # 4
gen.close()  # Stops the generator

# Infinite generator for repeating values
def repeat(obj):
    while True:
        yield obj

counter = repeat("x")
print([next(counter) for _ in range(3)])  # ['x', 'x', 'x']

# Generator combining multiple iterables
def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

combined = chain([1, 2], [3, 4], [5, 6])
print(list(combined))  # [1, 2, 3, 4, 5, 6]
