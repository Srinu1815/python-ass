def add_array_elements(arr):
    return sum(arr)
array = [1, 2, 3, 4, 5]
print("Sum of array elements:", add_array_elements(array))



def average_array(arr):
    return sum(arr) / len(arr) if len(arr) > 0 else 0
array = [1, 2, 3, 4, 5]
print("Average of array elements:", average_array(array))



def find_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return -1
array = [10, 20, 30, 40, 50]
value_to_find = 30
print("Index of value:", find_index(array, value_to_find))



def contains_value(arr, value):
    return value in arr
array = [10, 20, 30, 40, 50]
value_to_check = 30
print("Array contains value:", contains_value(array, value_to_check))



def remove_element(arr, value):
    try:
        arr.remove(value)
    except ValueError:
        pass
    return arr  
array = [10, 20, 30, 40, 50]
value_to_remove = 30
print("Array after removing value:", remove_element(array, value_to_remove))



def copy_array(arr):
    return arr.copy()
array = [1, 2, 3, 4, 5]
new_array = copy_array(array)
print("Original array:", array)
print("Copied array:", new_array)



def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr
array = [10, 20, 30, 40, 50]
index_to_insert = 2
value_to_insert = 25
print("Array after insertion:", insert_element(array, index_to_insert, value_to_insert))




def find_min_max(arr):
    return min(arr), max(arr)
array = [10, 20, 30, 40, 50]
minimum, maximum = find_min_max(array)
print("Minimum value:", minimum)
print("Maximum value:", maximum)




def reverse_array(arr):
    return arr[::-1]
array = [10, 20, 30, 40, 50]
print("Reversed array:", reverse_array(array))



def find_duplicates(arr):
    return list(set([x for x in arr if arr.count(x) > 1]))
array = [10, 20, 30, 20, 40, 50, 30]
print("Duplicate values:", find_duplicates(array))



def find_common_values(arr1, arr2):
    return list(set(arr1).intersection(arr2))
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
print("Common values:", find_common_values(array1, array2))



def remove_duplicates(arr):
    return list(set(arr))
array = [10, 20, 30, 20, 40, 50, 30]
print("Array after removing duplicates:", remove_duplicates(array))



def find_second_largest(arr):
    unique_sorted = sorted(set(arr), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None
array = [10, 20, 30, 40, 50]
print("Second largest value:", find_second_largest(array))




def count_even_odd(arr):
    even_count = len([x for x in arr if x % 2 == 0])
    odd_count = len(arr) - even_count
    return even_count, odd_count
array = [1, 2, 3, 4, 5, 6]
even_count, odd_count = count_even_odd(array)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)



def difference_largest_smallest(arr):
    return max(arr) - min(arr)
array = [1, 2, 3, 4, 5]
print("Difference between largest and smallest value:", difference_largest_smallest(array))



def contains_two_elements(arr, val1, val2):
    return val1 in arr and val2 in arr
array = [10, 20, 30, 12, 23, 40]
print("Array contains both 12 and 23:", contains_two_elements(array, 12, 23))



def remove_duplicates(arr):
    return list(set(arr))
array = [10, 20, 30, 20, 40, 50, 30]
print("Array after removing duplicates:", remove_duplicates(array))
