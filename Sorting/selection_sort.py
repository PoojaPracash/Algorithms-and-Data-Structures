# This program implements the Selection sort algorithm
# Time complexity: O(n^2)
# Auxiliary Space: O(1)


A = [99, 8, 38, 22, 1, 55]

for i in range(len(A)):

    min_idx = i

    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

for i in range(len(A)):
    print("%d" % A[i])
