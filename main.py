lst=[4,6,8,1,2,3]
n=len(lst)

for i in range(0,n):
    min_index=i
    for j in range(i+1,n):
        if lst[min_index]>lst[j]:
            min_index=j

    lst[min_index],lst[i]=lst[i],lst[min_index]


print(lst)