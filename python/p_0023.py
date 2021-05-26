# Non-abundant sums
# Problem 23

# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

from p_0021 import GetProperDivisors
import pprint


def NumberType(num: int) -> str:
    divisorList = list(set(GetProperDivisors(num)))
    divisorSum = sum(divisorList)

    if num > divisorSum:
        return "deficient"
    elif num < divisorSum:
        return "abundant"
    return "perfect"


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    result = "result"

    # defined in the problem.
    limit = 28123

    abundants = []
    for n in range(1, limit + 1):
        numberType = NumberType(n)
        if numberType == "abundant":
            abundants.append(n)

    # Find the sum of all the positive integers which cannot be written as the sum
    # of two abundant numbers.

    # this block of code is the major time sink of the program.
    # I think this can be optimized as it takes much too long to run.
    abundantSums = []
    for n in abundants:
        if n > limit:
            break
        for n1 in abundants:
            testSum = n + n1
            if testSum > limit:
                break
            if testSum not in abundantSums:
                abundantSums.append(testSum)

    notAbundantSum = []
    for n in range(1, limit + 1):
        if n not in abundantSums:
            notAbundantSum.append(n)

    result = sum(notAbundantSum)
    pp.pprint(result)
