arr=[5,7,3,2,6,1,5,9]

def reverse_specific_part(arr,left,right):
    if left>right:
        return
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    reverse_specific_part(arr,left+1,right-1)


reverse_specific_part(arr,0,7)
print(arr)