


# 10001st prime
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


from p_0003 import factors

if __name__ == "__main__":
    num_primes = 0
    x = 1
    while num_primes < 10001:
        factor_list = factors(x)
        if len(factor_list) < 1:
            num_primes += 1
        x += 1


    print(num_primes, x-1)