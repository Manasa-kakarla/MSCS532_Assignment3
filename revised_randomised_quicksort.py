import random

def randomized_quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = randomized_partition(arr, low, high)
        
        # Recursively sort the subarrays
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    if low < high:
        # Choose a random pivot index
        pivot_index = random.randint(low, high)
        
        # Swap the chosen pivot with the last element
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # Partition the array around the pivot
        return partition(arr, low, high)
    return low

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element to its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1

def quick_sort(arr):
    # Public method to start the sort
    if not arr:
        return
    randomized_quick_sort(arr, 0, len(arr) - 1)

# Example usage:
if __name__ == "__main__":
    # Test cases for different edge cases
    test_arrays = [
        [10, 7, 8, 9, 1, 5],          # Normal case
        [],                            # Empty array
        [5],                            # Single element
        [1, 1, 1, 1, 1],                # Repeated elements
        [1, 2, 3, 4, 5, 6, 7, 8, 9],    # Already sorted
        [9, 8, 7, 6, 5, 4, 3, 2, 1]     # Reverse sorted
    ]
    
    for arr in test_arrays:
        print(f"Original array: {arr}")
        quick_sort(arr)
        print(f"Sorted array:   {arr}\n")
