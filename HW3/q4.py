import random


def insertionSort(A):
    length = len(A)
    count_is = 0
    for i in range(0,length):
        temp = A[i]
        j = i - 1
        while j >= 0 and temp < A[j]:
            A[j+1] = A[j]
            j = j - 1
            count_is = count_is + 1               ## due to swap, increase count_is
        A[j+1] = temp
    return count_is

count_qs = 0

def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    global count_qs
    for j in range(low , high):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            count_qs+=1
    arr[i+1],arr[high] = arr[high],arr[i+1]
    count_qs+=1
    return ( i+1 )
def quickSort(A,l,h):
    if l < h :
        index  = partition(A,l,h)
        quickSort(A,l,index-1)
        quickSort(A, index+1,h)


def test():
    ### Create unsorted same 2 list
    global count_qs
    arr_1 = []
    arr_2=[]
    item_count = 1018
    for i in range(item_count):
        temp_rand=random.randint(0,1000)
        arr_1.append(temp_rand)
        arr_2.append(temp_rand)
    print("Unsorted List: ", arr_1)
    countIns = insertionSort(arr_1)
    print("Insertionsort... ")
    print(arr_1)
    print("Quicksort... ")
    quickSort(arr_2, 0, len(arr_2) - 1)
    print(arr_2)
    print("Number of swaps in insertion sort algorithm: ", countIns)
    print("Number of swaps in quick: ", count_qs)

    if count_qs > countIns:
        print("Insertion Sort has less number of swaps")
    elif count_qs < countIns:
        print("Quick Sort has less number of swaps")
    else:
        print("Quick Sort and Insertion Sort has the same number of swaps")

    print()
    print()
    print()
    count_qs = 0
    ## Small Array

    A=[3,7,2,1,5,9,11,34,6]
    print("Unsorted List: ", A)
    countIns=insertionSort(A)
    print("Insertionsort... ")
    print(A)
    B=[3,7,2,1,5,9,11,34,6]
    print("Quicksort... ")
    quickSort(B,0,len(B)-1)
    print(B)
    print("Number of swaps in insertion sort algorithm: ", countIns)
    print("Number of swaps in quick: ", count_qs)

    if count_qs > countIns:
        print("Insertion Sort has less number of swaps")
    elif count_qs < countIns:
        print("Quick Sort has less number of swaps")
    else:
        print("Quick Sort and Insertion Sort has the same number of swaps")


test()
