def solution(n, arr):
    # ? base condition if there is only one element in the array then we are going to return that element only
    if n == 1:
        return arr[0]
    
    # * take two variables one with the first index value and other with the maxElement value of first and last 

    num1 = arr[0]
    num2 = max([arr[0], arr[1]])

    for i in range(2, n , 1):
        temp = num2
        num2 = max([num1 + arr[i], num2])
        num1 = temp


    return num2

print(solution(6, [5, 5, 10, 100, 10, 5]))