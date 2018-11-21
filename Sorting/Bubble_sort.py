# This program shows Bubble sort implementation
# Time complexity: O(n^2)
# Auxiliary Space: O(1)


# set a flag to reduce number of iterations after the array is sorted
A = [7, 1, 45, 23, 99, 62]
Sorted = False

for i in range(len(A)):
    if not Sorted:
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                Sorted = True

for i in range(len(A)):
    print("%d" % A[i])

# Runs i iterations irrespective of the condition, if array is sorted or not
A = [17, 11, 145, 123, 199, 162]

for i in range(len(A)):
    for j in range(len(A) - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

for i in range(len(A)):
    print("%d" % A[i])
