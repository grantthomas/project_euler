# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import pprint
from p_0012 import get_divisors


def GetProperDivisors(num) -> list:
    divisors = get_divisors(num)
    divisors.pop(len(divisors) - 1)
    return divisors


divisorList = {}


def DivisorSum(GetProperDivisors, num: int) -> int:
    properDivisors = GetProperDivisors(num)
    return (sum(properDivisors), properDivisors)


def AmicableNumbers(divisorList):
    amicableList = []
    for key, value in divisorList.items():
        a = divisorList[key]
        if a in divisorList.keys():
            b = divisorList[value]
            if (key != value) and (a == value) and (key == b):
                amicableList.append(key)
    return amicableList


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)

    result = "result"
    for num in range(1, 10000):
        divisorList[num] = DivisorSum(GetProperDivisors, num)[0]
    result = divisorList
    del num

    amicableList = AmicableNumbers(divisorList)

    result = sum(amicableList)
    pp.pprint(result)
