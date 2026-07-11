num=153
n=num
count=len(str(num))
total=0

while n>0:
    r=n%10
    total=total+(r**count)
    n=n//10

print(total)

