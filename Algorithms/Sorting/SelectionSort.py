def selection_sort(arr):
    """
    Sorts an array using the Selection Sort algorithm.

    Args:
    arr (list): The array to be sorted.

    Returns:
    list: The sorted array.
    """

    # Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array: ", arr)
    print("Sorted array: ", selection_sort(arr))
    

if __name__ == "__main__":
    main()