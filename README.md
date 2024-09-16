Understanding Algorithm Efficiency and Scalability

This Assignment is for better understanding of how algorithms performs under different conditions. This will analyze and compare the efficiency and scalability of two key algorithms such as Randomized Quicksort and Hashing with Chaining.

'randomised_quicksort.py': contains randomized quicksort algorithm

'revised_randomised_quicksort.py': contains randomized quicksort algorithm that handles various edge cases such as arrays with repeated elements, empty arrays, and already sorted arrays.

'compare.py': contains the logic to empirically compare the running time of randomized quicksort with deterministic quicksort.

'hashtable.py': contains the logic to implement a hash table using chaining for collision resolution.

prerequisites:

python3.x

Run the code:

To run above files below are the commands:

python randomised_quicksort.py

python revised_randomised_quicksort.py

python compare.py

python hashtable.py

Sample output for randomised_quicksort.py:

python -u "/home/manasa/vscode_projects/quicksort_hasing/randomised_quicksort.py"

Original array: [10, 7, 8, 9, 1, 5]

Sorted array: [1, 5, 7, 8, 9, 10]

sample output for revised_randomised_quicksort.py:

python -u "/home/manasa/vscode_projects/quicksort_hasing/revised_randomised_quicksort.py"

Original array: [10, 7, 8, 9, 1, 5]
Sorted array:   [1, 5, 7, 8, 9, 10]

Original array: []
Sorted array:   []

Original array: [5]
Sorted array:   [5]

Original array: [1, 1, 1, 1, 1]
Sorted array:   [1, 1, 1, 1, 1]

Original array: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Sorted array:   [1, 2, 3, 4, 5, 6, 7, 8, 9]

Original array: [9, 8, 7, 6, 5, 4, 3, 2, 1]
Sorted array:   [1, 2, 3, 4, 5, 6, 7, 8, 9]

sample output for hashtable.py:

python -u "/home/manasa/vscode_projects/quicksort_hasing/hashtable.py"

Search 'name': Alice

Search 'city': New York

Search 'age' after deletion: None

Hash Table: [[], [], [], [('name', 'Alice')], [], [], [], [], [], [('city', 'New York')]]

This project is licensed under the MIT License.
