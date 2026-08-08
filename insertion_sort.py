def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key


lst=[4,3,5,6,1,2,9]
insertion_sort(lst)
print(lst)