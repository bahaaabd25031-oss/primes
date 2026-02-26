import time
import math

def int_input():
    while True:     
        try:
            n = int(input('enter a number to show the primes less than it: '))
            if n <= 2:
                raise Exception('an error happened make sure the input is an intger and larger than two')
            break
        except:
            print('an error happened make sure the input is an intger and larger than two') 
    return n   

def prime_range():
    n = int_input()
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
    [print(indx,end =' - ') for indx in range(2,n) if all_prime[indx] == True]
    
prime_range()
#O(nloglogn)
