# Program shows implementation of insertion sort
# Time complexity: O(n^2)
# Auxiliary Space: O(1)


# Function for insertion sorting
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    A = [9, 1, 5, 2, 4, 8, 3]
    insertionSort(A)
    for i in range(len(A)):
        print("%d" % A[i])
