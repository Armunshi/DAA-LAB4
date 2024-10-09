# Brute force method to count the number of inversions in a list
def count_inversions_brute_force(arr):
    inversions = 0
    n = len(arr)
    
    # Compare each pair (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
                
    return inversions

# Divide and conquer (merge sort) method to count the number of inversions in a list
def count_inversions_divide_and_conquer(arr):
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    inversions = merge_sort(arr, left, mid)
    inversions += merge_sort(arr, mid + 1, right)
    inversions += merge_and_count(arr, left, mid, right)
    
    return inversions

def merge_and_count(arr, left, mid, right):
    # Left and right subarrays
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    inversions = 0
    
    # Merge while counting inversions
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            inversions += (mid - i + 1 - left)  # Count inversions
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1
    
    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1
        
    return inversions


# The provided nested list
students_random_numbers = []

# Check if the list is empty
if not students_random_numbers:
    print("ERROR: The list of course code is empty, so the inversion count cannot be found by neither brute force nor divide and conquer approach.")
else:
    # Calculate the inversion count for each sublist using brute force
    brute_force_inversion_counts = [count_inversions_brute_force(sublist) for sublist in students_random_numbers]

    # Calculate the inversion count for each sublist using divide and conquer
    divide_and_conquer_inversion_counts = [count_inversions_divide_and_conquer(sublist[:]) for sublist in students_random_numbers]

    # Calculate the total inversion count across all students for both methods
    total_inversion_count_brute_force = sum(brute_force_inversion_counts)
    total_inversion_count_divide_and_conquer = sum(divide_and_conquer_inversion_counts)

    # Function to categorize inversion counts
    def categorize_inversion_counts(inversion_counts):
        categories = {}
        for index, count in enumerate(inversion_counts):
            if count not in categories:
                categories[count] = []
            categories[count].append(index + 1)  # Storing student index (1-based)
        return categories

    # Categorize inversion counts for both brute force and divide and conquer methods
    brute_force_categories = categorize_inversion_counts(brute_force_inversion_counts)
    divide_and_conquer_categories = categorize_inversion_counts(divide_and_conquer_inversion_counts)

    # Display the results
    print("Total inversion count (Brute Force) across all students:", total_inversion_count_brute_force)
    print("Total inversion count (Divide and Conquer) across all students:", total_inversion_count_divide_and_conquer)

    print("\nCategorized Inversion Counts (Brute Force):")
    for count, students in sorted(brute_force_categories.items()):
        print(f"Inversion Count {count}: Students {students}")

    print("\nCategorized Inversion Counts (Divide and Conquer):")
    for count, students in sorted(divide_and_conquer_categories.items()):
        print(f"Inversion Count {count}: Students {students}")
