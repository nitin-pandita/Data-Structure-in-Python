def StringCount(n):
    if n == 1:
        return 3
    elif n == 2:
        return 8
    elif n == 3:
            
        return 19
    else:
        # used to calculate the count of string 
        return int(0.5 * (n ** 3 + 3 * n + 2))
    

print(StringCount(1))