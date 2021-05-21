# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


from p_0003 import factors

if __name__ == "__main__":
    num = 2e6
    primes=[]
    for x in range(1,int(num)):
        factor_list = factors(x)
        if len(factor_list) < 1:
            primes.append(x)
        if x % int(1e4) == 0:
            print(x,len(primes))


    print(sum(primes))