import random

def randomized_quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = randomized_partition(arr, low, high)
        
        # Recursively sort the subarrays
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    # Choose a random pivot index
    pivot_index = random.randint(low, high)
    
    # Swap the chosen pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    # Partition the array around the pivot
    return partition(arr, low, high)

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

# Example usage:
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    
    randomized_quick_sort(arr, 0, len(arr) - 1)
    
    print("Sorted array:", arr)
