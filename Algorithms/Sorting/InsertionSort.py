def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    list: The sorted array.
    """

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        # Store the current element in a variable
        key = arr[i]

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key element at its correct position
        arr[j + 1] = key

    # Return the sorted array
    return arr

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array: ", arr)
    print("Sorted array: ", insertion_sort(arr))    
    

if __name__ == "__main__":
    main()