n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

f_map=dict()
length=len(n)

for i in range(0,length):
    if n[i] in f_map:
        f_map[n[i]]+=1
    else:
        f_map[n[i]]=1

for num in m:
    if num in f_map:
        print(num,f_map[num])
    else:
        print(num,0)