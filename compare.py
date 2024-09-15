import random
import time

# Deterministic QuickSort (using the first element as the pivot)
def deterministic_quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition_deterministic(arr, low, high)
        deterministic_quick_sort(arr, low, pivot_index - 1)
        deterministic_quick_sort(arr, pivot_index + 1, high)

def partition_deterministic(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Randomized QuickSort
def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        return partition_deterministic(arr, low, high)
    return low

# Generate different types of arrays
def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(size))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def generate_repeated_elements_array(size):
    return [random.randint(0, 10) for _ in range(size)]

# Measure time taken for sorting
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Compare the performance of both sorts
def compare_sorts(sizes):
    for size in sizes:
        print(f"Array size: {size}")
        
        # Generate arrays
        random_array = generate_random_array(size)
        sorted_array = generate_sorted_array(size)
        reverse_sorted_array = generate_reverse_sorted_array(size)
        repeated_elements_array = generate_repeated_elements_array(size)
        
        # Create copies for both sorts
        random_array_det = random_array[:]
        random_array_rand = random_array[:]
        sorted_array_det = sorted_array[:]
        sorted_array_rand = sorted_array[:]
        reverse_sorted_array_det = reverse_sorted_array[:]
        reverse_sorted_array_rand = reverse_sorted_array[:]
        repeated_elements_array_det = repeated_elements_array[:]
        repeated_elements_array_rand = repeated_elements_array[:]
        
        # Measure time for Deterministic QuickSort
        time_det_random = measure_time(deterministic_quick_sort, random_array_det)
        time_det_sorted = measure_time(deterministic_quick_sort, sorted_array_det)
        time_det_reverse_sorted = measure_time(deterministic_quick_sort, reverse_sorted_array_det)
        time_det_repeated = measure_time(deterministic_quick_sort, repeated_elements_array_det)
        
        # Measure time for Randomized QuickSort
        time_rand_random = measure_time(randomized_quick_sort, random_array_rand)
        time_rand_sorted = measure_time(randomized_quick_sort, sorted_array_rand)
        time_rand_reverse_sorted = measure_time(randomized_quick_sort, reverse_sorted_array_rand)
        time_rand_repeated = measure_time(randomized_quick_sort, repeated_elements_array_rand)
        
        # Print results
        print(f"Deterministic QuickSort (Random): {time_det_random:.5f} seconds")
        print(f"Randomized QuickSort (Random): {time_rand_random:.5f} seconds")
        print(f"Deterministic QuickSort (Sorted): {time_det_sorted:.5f} seconds")
        print(f"Randomized QuickSort (Sorted): {time_rand_sorted:.5f} seconds")
        print(f"Deterministic QuickSort (Reverse Sorted): {time_det_reverse_sorted:.5f} seconds")
        print(f"Randomized QuickSort (Reverse Sorted): {time_rand_reverse_sorted:.5f} seconds")
        print(f"Deterministic QuickSort (Repeated Elements): {time_det_repeated:.5f} seconds")
        print(f"Randomized QuickSort (Repeated Elements): {time_rand_repeated:.5f} seconds")
        print()

if __name__ == "__main__":
    sizes = [100, 1000, 5000]  # Array sizes for testing
    compare_sorts(sizes)
