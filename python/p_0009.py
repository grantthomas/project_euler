# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math
def find_pythag_triplet(triplet_sum:int) -> int:
    limit = math.ceil(triplet_sum/2)

    for c in range(limit,5,-1):
        for b in range(c-1,4,-1):
            a = triplet_sum - c - b
            if a >= b:
                break
            is_triplet = ((a**2 + b**2) == c**2)
            if is_triplet:
                return [a,b,c]

    return -1

if __name__ == "__main__":
    num=1000
    result = find_pythag_triplet(int(num))
    print(math.prod(result))