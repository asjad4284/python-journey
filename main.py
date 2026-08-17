lst=[3,2,5,6,1,9]

n=len(lst)

for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]

print(lst)