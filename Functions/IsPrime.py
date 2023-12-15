def isPrimeNumber(n):
    for i in range(2,n):
        if(n % i == 0) :
            break
        
    else:
        return True
    
    return False;

print(isPrimeNumber(5))


# get a series of prime Number 

def isPrimeSeries(n):
    for d in range(2,n+1):
        isPrime = isPrimeNumber(d)
        if(isPrime) :
            print(d)


print(isPrimeSeries(10))