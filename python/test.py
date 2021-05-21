#600851475143
import math

def factors(limit):
    limit = int(limit)
    primes=[]
    while (limit%2 == 0):
        primes.append(2)
        limit = limit // 2
    
    for x in range(3,int(math.sqrt(limit))+1,2):
        while (limit%x == 0):
            primes.append(x)
            limit = limit // x
    
    return primes


num = 600851475143
print(f"num: {num}\n {factors(num)}")
