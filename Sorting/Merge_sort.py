# Program shows implementation of merge sort
# Time complexity: O(nLogn)
# Auxiliary Space: O(n)


# Function for merge sorting
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])


# driver code to test the above code
if __name__ == '__main__':
    arr = [1, 61, 53, 25, 16, 79, 99, 84]
    print ("Given array is")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is:")
    printList(arr)
