## Binary Search
array = [1,5,32,54,74,78,98,140,150,190,500,700]

def binary_search(array,target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        
        if array[mid] == target:
            return mid
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
    return -1
    
binary_search(array=array,target=700)
