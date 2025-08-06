def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
sample_list = [12, 7, 5, 3, 8, 4, 2, 15, 10, 6, 1, 9, 13, 11, 14]
sorted_list = quick_sort(sample_list)
print(sorted_list)
# To run this code interactively, you can use a Jupyter notebook.
# If you are using VS Code, switch to the Jupyter extension by opening the Command Palette (Ctrl+Shift+P) and selecting "Jupyter: Create New Blank Notebook".
# Then, copy and paste the code cells into the notebook for interactive execution.
"""
    Sorts a list of elements using the Quick Sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.

    Example:
        >>> quick_sort([3, 1, 2])
        [1, 2, 3]

    Note:
        Quick Sort is a divide-and-conquer algorithm that selects a 'pivot' element and partitions the array into two sub-arrays, according to whether elements are less than or greater than the pivot.

    """
    # Time Complexity:
    # Average case: O(n log n)
    # Worst case: O(n^2) (when the smallest or largest element is always chosen as the pivot)
    # Space Complexity:
    # O(log n) due to recursive stack space in the average case
    # O(n) in the worst case due to partitioning
    # Stability: Quick Sort is not a stable sort.   