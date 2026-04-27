def my_generators():
    yield 1
    yield 2
    yield 3


for value in my_generators():
    print(value)