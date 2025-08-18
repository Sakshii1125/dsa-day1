def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)
    i, j = m - 1, 0

    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1

   
    arr1.sort()
    arr2.sort()
    return arr1, arr2

print(merge([1, 3, 5], [2, 4, 6]))  
print(merge([10, 12, 14], [1, 3, 5]))  
print(merge([2, 3, 8], [4, 6, 10]))    
print(merge([1], [2]))    
