def nthPoint(n):
    # base condition
    if n <= 1:
        return n
    

    # now the ways to initialize to reach each point
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2


    # calculating the number of ways to reach the value
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i -2]

    return ways[n]


# N = 4
# result = nthPoint(N)
# print("Number of ways to reach point", N, "is:", result)