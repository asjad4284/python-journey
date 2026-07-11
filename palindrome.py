num=32123
n=num
result=0

while n>0:
    r=n%10
    result=(result*10)+r
    n=n//10

if(num==result):
    print("Palindrome")
else:
    print("Not Palindrome")