# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def factors(limit):
    limit = int(limit)
    primes=[]
    if limit <2:
        return [1]
    elif limit == 2:
        return primes
        
    while (limit%2 == 0):
        primes.append(2)
        limit = limit // 2
    
    for x in range(3,int(math.sqrt(limit))+1,2):
        while (limit%x == 0):
            primes.append(x)
            limit = limit // x
    
    
    return primes

def prime_factors(primes:list,number:int) -> int:
    result=[]
    for prime in primes:
        if number%prime == 0:
            result.append(prime)
    return result

if __name__ == "__main__":
    number=int(600851475143)
    primes = factors(number)

    prime_factor_list = prime_factors(primes,number)
    if len(prime_factor_list) > 0:
        largest_prime_factor = prime_factor_list[-1]
    else:
        largest_prime_factor = number
    print(number,largest_prime_factor)