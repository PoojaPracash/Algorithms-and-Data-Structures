# This program shows binary search implementation(Decrease & conquer)
# Time complexity: O(Log n).
# Auxiliary Space: O(1) in case of iterative implementation.
#                  O(Logn) in case of recursive implementation.


def binarySearch(arr, low, high, X):

    while(low <= high):
        # calculate mid of the given input array
        mid = low + (high - low) // 2

        # Check if mid element in array is an element to be searched
        if arr[mid] == X:
            return X
        # check if the element to be found is less than mid
        # change low to mid + 1
        elif arr[mid] < X:
            low = mid + 1
        # check if the element to be found is greater than mid
        # change high to mid - 1
        elif arr[mid] > X:
            high = mid - 1
    return -1


if __name__ == '__main__':
    # Sorted array as input
    a = [3, 6, 19, 26, 34, 58, 75, 97]
    # Element to be searched
    x = 75
    result = binarySearch(a, 0, len(a) - 1, x)

    if result != -1:
        print("Element found")
    else:
        print("Element not in array")
