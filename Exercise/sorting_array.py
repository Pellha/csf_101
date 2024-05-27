def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    arr = [replacement if x == target else x for x in arr]
    return arr

print("Enter an array of integers separated by spaces:")
arr = list(map(int, input().split()))

sorted_arr = quick_sort(arr)
print("Sorted array:")
print(sorted_arr)

print("Enter a target element to search for in the sorted array:")
target = int(input())

if target in sorted_arr:
    print(f"Enter a replacement element for {target}:")
    replacement = int(input())
    modified_arr = replace_elements(sorted_arr, target, replacement)
    print("Modified array:")
    print(modified_arr)
else:
    print(f"{target} not found in the array.")