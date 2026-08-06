def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
            


lst=[4,3,5,1,7,2]
bubble_sort(lst)
print(lst)