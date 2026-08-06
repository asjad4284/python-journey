def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_index=i
        for j in range(i,n):
            if nums[j]<nums[min_index]:
                min_index=j

        nums[i],nums[min_index]=nums[min_index],nums[i]


lst=[4,3,6,7,1,2,9]
selection_sort(lst)
print(lst)