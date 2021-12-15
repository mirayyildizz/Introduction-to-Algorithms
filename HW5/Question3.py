######################################
### CSE 321 Homework 5  Question 3 ###
###         Miray Yıldız          ####
###          161044023            ####
######################################

# Python program that finds the
# most valuable subset of the items that fit into the knapsack.

# Returns the maximum value
# with knapsack of W capacity
def Knapsack(W, n, val, w):

    ## dp helps store maximum value with knapsack capacity
    dp = [0 for i in range(W + 1)]

    # fill dp
    for i in range(W + 1):
        for j in range(n):
            if (w[j] <= i):
                dp[i] = max(dp[i], dp[i - w[j]] + val[j])

    return dp[W]


if __name__ == "__main__":
    W = 9
    val = [10, 4, 3]
    w = [5, 4, 2]
    n = len(val)
    print("Solution is: ")
    print(Knapsack(W, n, val, w))
