import time
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
    all_prime = [2]
    ctr = 1
    t1 = time.perf_counter() 
    for x in range(3,n,2):
        for i in all_prime:
            if x % i == 0: break
        else:
            all_prime.append(x)
            ctr += 1
    t2 = time.perf_counter()
    print(f'the time taken is: {t2 - t1:0.6f}')
    print(f'the numner of primes under {n} is:',ctr)
    print(all_prime)


prime_range()

#O( n^2/ln(n) )
