#############################################################
#### CSE-321 Introduction to Algorithm Design, Fall 2020 ####
####            Homework 2  Part 3                       ####
####                Miray Yıldız                         ####
#############################################################


def merge(Array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    # temp arrays
    L = [0] * (n1)
    R = [0] * (n2)


    for i in range(0, n1):
        L[i] = Array[left + i]

    for j in range(0, n2):
        R[j] = Array[middle + 1 + j]


    i = 0  # index first subarray
    j = 0  # index second subarray
    k = left  # index  merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            Array[k] = L[i]
            i += 1
        else:
            Array[k] = R[j]
            j += 1
        k += 1

    # Copy
    while i < n1:
        Array[k] = L[i]
        i += 1
        k += 1

    # Copy
    while j < n2:
        Array[k] = R[j]
        j += 1
        k += 1



def mergeSort(Array, left, right):
    if left < right:

        middle = (left + (right - 1)) // 2

        # Sort first and second halves
        mergeSort(Array, left, middle)
        mergeSort(Array, middle + 1, right)
        merge(Array, left, middle, right)

## It is actually binary search
def findMultiYields(Array, desired, n):
    mergeSort(Array, 0, n - 1)
    ##print("Array is ")
    ##print(Array)
    right = len(Array) - 1
    left = 0

    while left < right  and left < len(Array) and right >= 0 :
        value = Array[right] * Array[left]
        if value == desired:
            print("Found!")
            print("(", Array[left], ",", Array[right], ")")
            left += 1
        elif value <  desired :
            left += 1
        elif value > desired :
            right -= 1



# Test
Array = [1, 2, 3, 6, 5, 4]
n = len(Array)
desired = 6
findMultiYields(Array, desired, n)
