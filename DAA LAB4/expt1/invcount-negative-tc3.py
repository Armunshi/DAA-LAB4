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

# Function to check for invalid values in the student course codes
def validate_student_codes(student_codes):
    errors = []
    for index, sublist in enumerate(student_codes):
        for code in sublist:
            if isinstance(code, bool):
                errors.append(f"ERROR: The array {index + 1} contains boolean values. Cannot process this array.")
                break
            if isinstance(code, str):
                errors.append(f"ERROR: The array {index + 1} contains string values. Cannot process this array.")
                break
            if isinstance(code, int) and code < 0:
                errors.append(f"ERROR: The array {index + 1} contains negative values. Cannot process this array.")
                break
    return errors

# The provided nested list (example student course codes)
students_random_numbers = [[5,2,3,True],[False,1,5,2],[7,6,4,1],[6,2,True,7],[2,3,8,4],[5,5,5,4]]

# Check if the list is empty
if not students_random_numbers:
    print("ERROR: The list of course codes is empty, so the inversion count cannot be found by either brute force or divide and conquer approach.")
else:
    # Validate student codes
    error_messages = validate_student_codes(students_random_numbers)

    # If any errors are found, print them and do not calculate inversions for those arrays
    for error in error_messages:
        print(error)

    # Process only valid sublists for inversion counts
    valid_inversion_counts_brute_force = []
    valid_inversion_counts_divide_and_conquer = []

    for index, sublist in enumerate(students_random_numbers):
        # Check for errors again in this loop to ensure clarity
        if isinstance(sublist, list):
            if any(isinstance(code, bool) for code in sublist):
                continue
            if any(isinstance(code, str) for code in sublist):
                continue
            if any(isinstance(code, int) and code < 0 for code in sublist):
                continue
            
            # Calculate inversion counts for valid sublists
            valid_inversion_counts_brute_force.append(count_inversions_brute_force(sublist))
            valid_inversion_counts_divide_and_conquer.append(count_inversions_divide_and_conquer(sublist[:]))

    # Calculate total inversion counts for valid arrays
    total_inversion_count_brute_force = sum(valid_inversion_counts_brute_force)
    total_inversion_count_divide_and_conquer = sum(valid_inversion_counts_divide_and_conquer)

    # Function to categorize inversion counts
    def categorize_inversion_counts(inversion_counts):
        categories = {}
        for index, count in enumerate(inversion_counts):
            if count not in categories:
                categories[count] = []
            categories[count].append(index + 1)  # Storing student index (1-based)
        return categories

    # Categorize inversion counts for both brute force and divide and conquer methods
    brute_force_categories = categorize_inversion_counts(valid_inversion_counts_brute_force)
    divide_and_conquer_categories = categorize_inversion_counts(valid_inversion_counts_divide_and_conquer)

    # Display the results
    print("\nTotal inversion count (Brute Force) across all valid students:", total_inversion_count_brute_force)
    print("Total inversion count (Divide and Conquer) across all valid students:", total_inversion_count_divide_and_conquer)

    print("\nCategorized Inversion Counts (Brute Force):")
    for count, students in sorted(brute_force_categories.items()):
        print(f"Inversion Count {count}: Students {students}")

    print("\nCategorized Inversion Counts (Divide and Conquer):")
    for count, students in sorted(divide_and_conquer_categories.items()):
        print(f"Inversion Count {count}: Students {students}")
