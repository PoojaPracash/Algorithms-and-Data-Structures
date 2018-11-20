# This program shows Jump search implementation. The basic idea is to check
# elements by jumping ahead by fixed steps or skipping some elements in
# place of searching all elements.
# Time complexity : O(√n) Between Linear Search O(n) and Binary Search O(Log n)
# Auxiliary Space : O(1)
import math


def jumpSearch(arr, l, X):
    # The best step size is √n, where n is input array size
    step = math.sqrt(l)
    prev = 0

    # Check element in input array untill its less than X
    while arr[int(min(step, l) - 1)] < X:
        prev = step
        step += math.sqrt(l)
        # if step exceeds total input array size return -1
        if prev >= l:
            return -1

    # check every element after prev untill end of input array
    while arr[int(prev)] < X:
        prev += 1

        if prev == min(step, l):
            return -1

    # returns element if found
    if arr[int(prev)] == X:
        return prev

    return -1


if __name__ == '__main__':
    # Input array in sorted order
    a = [3, 5, 7, 9, 11, 15, 21, 30, 48, 50, 51, 63, 70, 75, 80]
    # Element to be searched
    x = 63

    result = jumpSearch(a, len(a), x)

    if result != -1:
        print("Element found")
    else:
        print("Element not fond")
