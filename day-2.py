def find_missing_number(arr):
    n = len(arr) + 1   
    total = n * (n + 1) // 2
    arr_sum = sum(arr)
    missing = total - arr_sum
    return missing


# Test Cases
print(find_missing_number([1, 2, 4, 5]))       
print(find_missing_number([2, 3, 4, 5]))    
print(find_missing_number([1, 2, 3, 4]))       
print(find_missing_number([1]))               
print(find_missing_number(list(range(1, 1000000)))) 
