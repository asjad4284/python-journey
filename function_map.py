#method 1

nums=[1,3,4,6,1,4,2,7,9,6,3,8,9]
f_map=dict()

for i in range(0,len(nums)):
    if nums[i] in f_map:
        f_map[nums[i]]+=1
    else:
        f_map[nums[i]]=1
    

print(f_map)

#method 2

# number=[1,3,4,6,1,4,2,7,9,6,3,8,9]
# n=len(number)
# h_map=dict()

# for i in range(0,n):
#     h_map[number[i]]=h_map.get(number[i],0)+1

# print(h_map)

number=[1,3,4,6,1,4,2,7,9,6,3,8,9]
check=dict()

for i in range(0,len(number)):
    if number[i] in check:
        check[number[i]]+=1
    else:
        check[number[i]]=1

print(check)