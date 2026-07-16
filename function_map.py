#method 1

nums=[1,3,4,6,1,4,2,7,9,6,3,8,9]
f_map=dict()

for i in range(0,len(nums)):
    if nums[i] in f_map:
        f_map[nums[i]]+=1
    else:
        f_map[nums[i]]=1
    

print(f_map)

