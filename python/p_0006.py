# Sum square difference
# Problem 6

# The sum of the squares of the first ten natural numbers is,
#   1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#   3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(num_max:int) -> int:
    num_max = int(num_max)
    result = 0
    for x in range(num_max+1):
        result += x**2
    return result

def square_of_sums(num_max:int) -> int:
    num_max = int(num_max)
    num_sum = sum(range(num_max+1))
    return num_sum**2

if __name__ == "__main__":
    num=int(100)
    n_a = sum_of_squares(num)
    n_b = square_of_sums(num)

    print(n_b - n_a)
