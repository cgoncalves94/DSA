def quicksort(arr):
    """
    This function implements the QuickSort algorithm to sort an array of integers in ascending order.
    It uses the divide-and-conquer approach to recursively partition the array into smaller subarrays,
    and then sorts each subarray by selecting a pivot element and rearranging the elements around it.
    The pivot element is chosen as the last element of the subarray, and the partitioning is done in-place.
    The function returns the sorted array.
    """
    # Base case: if the array has only one element or is empty, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Select the pivot element as the last element of the array
    pivot = arr[-1]
    
    # Initialize two pointers to partition the array
    i = 0
    j = len(arr) - 2
    
    # Partition the array by rearranging the elements around the pivot
    while i <= j:
        # Find the first element from the left that is greater than the pivot
        while i <= j and arr[i] <= pivot:
            i += 1
        # Find the first element from the right that is less than or equal to the pivot
        while i <= j and arr[j] > pivot:
            j -= 1
        # Swap the two elements if they are not in the correct partition
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the first element from the right that is less than or equal to it
    arr[i], arr[-1] = arr[-1], arr[i]
    
    # Recursively sort the left and right subarrays
    left = quicksort(arr[:i])
    right = quicksort(arr[i+1:])
    
    # Concatenate the sorted subarrays and the pivot element to form the final sorted array
    return left + [arr[i]] + right

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array: ", arr)
    print("Sorted array: ", quicksort(arr))
    

if __name__ == "__main__": 
    main()