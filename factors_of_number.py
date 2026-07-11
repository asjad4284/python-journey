from math import sqrt

#Better solution(TC:O(N)) than Brute force
n=20
result=[]

for i in range(1,(n//2)+1):
    if (n%i==0):
        result.append(i)
result.append(n)
print(result)

#Optimal Solution

num=36
result=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if num//i != i:
            result.append(num//i)

result.sort()
print(result)
