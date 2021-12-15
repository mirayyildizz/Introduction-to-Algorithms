######################################
### CSE 321 Homework 5  Question 2 ###
###         Miray Yıldız          ####
###          161044023            ####
######################################

# Python program that find the smallest sum path
# from the triangle apex to its base through a sequence of
# adjacent numbers

def SmallestSumPath(myarr):
    # For storing the result in array
    arr = [None] * len(myarr)
    n = len(myarr) - 1

    # For the bottom row
    for i in range(len(myarr[n])):
        arr[i] = myarr[n][i]

    # Calculation of the
    # remaining rows,
    # in bottom up manner.
    for i in range(len(myarr) - 2, -1, -1):
        for j in range(len(myarr[i])):
            arr[j] = myarr[i][j] + min(arr[j], arr[j + 1]);


    return arr


if __name__ == "__main__":
    myarr = [[2],  [5, 4],  [1, 4, 7],  [8, 6, 9, 6]]
    arr =  SmallestSumPath(myarr)
    print("Smallest path is : ")
    print(arr[0])
