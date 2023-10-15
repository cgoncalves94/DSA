def binary_search(arr, target):
    """
    This function implements the binary search algorithm to find the index of a target value in a sorted array.

    Parameters:
    arr (list): A sorted list of integers.
    target (int): The value to search for in the array.

    Returns:
    int: The index of the target value in the array, or -1 if it is not found.
    """

    # Set the left and right pointers to the start and end of the array, respectively.
    left = 0
    right = len(arr) - 1

    # While the left pointer is less than or equal to the right pointer:
    while left <= right:
        # Calculate the middle index between the left and right pointers.
        mid = (left + right) // 2

        # If the middle value is equal to the target, return its index.
        if arr[mid] == target:
            return mid

        # If the middle value is greater than the target, move the right pointer to the left of the middle index.
        elif arr[mid] > target:
            right = mid - 1

        # If the middle value is less than the target, move the left pointer to the right of the middle index.
        else:
            left = mid + 1

    # If the target value is not found in the array, return -1.
    return -1


def main():
    arr = [11, 12, 22, 25, 34, 64, 90]
    target = 34

    print("Original array: ", arr)
    print("Target value: ", target)
    print("Index of target value: ", binary_search(arr, target))
    
if __name__ == "__main__":
    main()