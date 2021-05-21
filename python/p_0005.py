# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def lcm(max_factor:int) -> int:
    max_factor = int(max_factor)
    limit = math.factorial(max_factor)

    for x in range(1,limit):
        for n_a in range(max_factor,0,-1):
            if (x%n_a!= 0):
                break
            if (n_a == 1):
                return x
    return -1

if __name__ == "__main__":
    num=int(20)
    result=lcm(num)

    print(result)