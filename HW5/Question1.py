######################################
### CSE 321 Homework 5  Question 1 ###
###         Miray Yıldız          ####
###          161044023            ####
######################################

def FindSubsets(array, n, index = 0, sum = 0,  subset = [], dp = [], all_subsets = []):
    if not(len(dp)):
        ## Create dynamic programming table
        dp = [[0 for i in range(500)] ## 500 is random number, it is changeable.
              for j in range(n)]

    ## If sum of subsets elements equals zero return 1, else return 0
    if(index == n):
        if(sum == 0):
            all_subsets.append(subset)
            return 1

        else:
            return 0

    ##Copy subsets
    subs1 = subset.copy()
    subs2 = subset.copy()
    subs1.append(array[index])

    ## Recursive calls
    rec1 = FindSubsets(array, n, index+1, sum + array[index], subs1, dp, all_subsets)
    rec2 = FindSubsets(array, n, index+1, sum, subs2, dp, all_subsets)

    dp[index][sum + n] = rec1 + rec2

    return all_subsets

def SumZeroSubsets(array):
    n = len(array)
    subset = FindSubsets(array, n)
    subset_count = len(subset)

    print("Original Array:", array)

    m = 0
    if(subset_count > 1):
        print("Subsets: ")
        for m in range(subset_count -1):
            print( subset[m])

    else:
        print("Array has not any subset !\n")

if __name__ == "__main__":
    array = [2,3,-5,-8,6,-1]
    SumZeroSubsets(array)


