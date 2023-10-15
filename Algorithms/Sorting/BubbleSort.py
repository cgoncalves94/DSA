def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.

    :param arr: The array to be sorted.
    :return: The sorted array.
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array: ", arr)
    print("Sorted array: ", bubble_sort(arr))
    


if __name__ == "__main__":
    main()