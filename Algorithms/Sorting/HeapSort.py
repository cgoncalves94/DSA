
def heapify(arr, n, i):
    """
    This function is used to heapify the subtree rooted at index i.
    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left child
    r = 2 * i + 2  # right child

    # See if left child of root exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    This function sorts an array using Heap Sort algorithm.
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array: ", arr)
    print("Sorted array: ", heap_sort(arr))
    

if __name__ == "__main__":
    main()