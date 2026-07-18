#Print 1 to N using Head recursion

def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)


func(1,5)
