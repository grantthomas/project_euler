# Power digit sum
# Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?


def NumToDigits(num: int) -> list:
    """converts number to list of digits

    Args:
        num (int): number in

    Returns:
        list: list of ints out
    """
    return [int(x) for x in str(num)]


if __name__ == "__main__":
    result = "result"

    num = int(2 ** 1000)

    digits = NumToDigits(num)

    result = sum(digits)

    print(result)
