def merge_sort(arr):
    """
    This function implements the Merge Sort algorithm to sort an array of integers in ascending order.
    It works by recursively dividing the input array into two halves, sorting each half, and then merging the two sorted halves.
    :param arr: The input array to be sorted.
    :return: The sorted array.
    """
    # Base case: If the input array has only one element or is empty, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    # Recursive case: Divide the input array into two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the two sorted halves.
    return merge(left_half, right_half)

def merge(left_half, right_half):
    """
    This function merges two sorted arrays into a single sorted array.
    :param left_half: The first sorted array.
    :param right_half: The second sorted array.
    :return: The merged sorted array.
    """
    # Initialize variables to keep track of the indices of the left and right arrays.
    left_index = 0
    right_index = 0
    
    # Initialize an empty list to store the merged array.
    merged_arr = []
    
    # Merge the two arrays by comparing the elements at the current indices and appending the smaller one to the merged array.
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged_arr.append(left_half[left_index])
            left_index += 1
        else:
            merged_arr.append(right_half[right_index])
            right_index += 1
    
    # Append any remaining elements from the left or right array to the merged array.
    merged_arr += left_half[left_index:]
    merged_arr += right_half[right_index:]
    
    # Return the merged array.
    return merged_arr

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array: ", arr)
    print("Sorted array: ", merge_sort(arr))
    
    
if __name__ == "__main__":
    main()