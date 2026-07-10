from math import *



num=123001

n=0;
while num>0:
    digit=num%10;
    num=num//10
    n=n+1;

print(n)

#Logarithmic Approach

def count_digits(number):
    return int(log10(number)+1)

print(count_digits(1234))

