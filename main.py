def changefunc(func):
    def inner():
        return func().upper()
    return inner


@changefunc
def newfunc():
    return "Hello"

print(newfunc())

