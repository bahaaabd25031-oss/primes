import time
import math

def prime_range(n):
    all_prime = [True for _ in range(n)]
    t1 = time.perf_counter() 
    sqrtn = int(math.sqrt(n))
    for i in range(2,sqrtn):
        if all_prime[i] == True:
            j = i**2
            while j < n:
                all_prime[j] = False
                j += i
    t2 = time.perf_counter()
    print(f'the time taken is: {t2 - t1:0.6f}')
    [print(indx) for indx in range(2,n) if all_prime[indx] == True]
prime_range(1000)
#O(nloglogn)
