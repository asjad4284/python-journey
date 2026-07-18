#Print 1 to N using Head recursion

def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)


func(1,5)

#Print 1 to N using tail recursion

def new_func(n):
    if n<1:
        return
    new_func(n-1)
    print(n)

new_func(3)
