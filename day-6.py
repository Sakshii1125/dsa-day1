from collections import defaultdict

def find_zero_sum_subarrays(arr):
    n = len(arr)
    prefix_sum = 0
    seen = defaultdict(list)
    seen[0].append(-1)  
    result = []

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum in seen:
            
            for j in seen[prefix_sum]:
                result.append((j + 1, i))

        seen[prefix_sum].append(i)

    return result

print(find_zero_sum_subarrays([1, 2, -3, 3, -1, 2]))    
print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1])) 
print(find_zero_sum_subarrays([1, 2, 3, 4]))           
print(find_zero_sum_subarrays([0, 0, 0]))       
print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))  
