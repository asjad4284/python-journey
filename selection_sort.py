def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]


lst=[5,4,1,7,8,2,3]
selection_sort(lst)
print(lst)