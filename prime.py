import time

def prime_range(n):
    t1 = time.perf_counter() 
    all_prime = [2]
    ctr = 1
    for x in range(3,n,2):
        for i in all_prime:
            if x % i == 0: break
        else:
            all_prime.append(x)
            ctr += 1
    t2 = time.perf_counter()
    print(f'the time taken is: {t2 - t1:0.6f}')
    print(ctr)
    return all_prime

#O( n^2/ln(n) )
print(prime_range(100000))

    