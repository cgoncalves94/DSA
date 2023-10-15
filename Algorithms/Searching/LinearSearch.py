def linear_search(arr, x):
    """
    This function takes an array and a value to search for, and returns the index of the first occurrence of the value
    in the array. If the value is not found, it returns -1.
    """
    n = len(arr) # get the length of the array
    for i in range(n): # loop through each element in the array
        if arr[i] == x: # if the current element is equal to the value we're searching for
            return i # return the index of the current element
    return -1 # if the value is not found, return -1


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    x = 12
    result = linear_search(arr, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

if __name__ == "__main__":
    main()