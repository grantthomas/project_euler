# Even Fibonacci numbers
# Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def fibonacci(n: int) -> list:
    """generate all fibonacci numbers less than n

    Args:
        n (int): input

    Returns:
        list: list of fibonacci numbers less than n
    """
    i = [1, 1, 2]

    while i[-1] < n:
        next = i[-1] + i[-2]
        if next < n:
            i.append(next)
        else:
            break

    return i


def sum_evens(items: list) -> int:
    result = 0
    for item in items:
        if item % 2 == 0:
            result += item
    return result


if __name__ == "__main__":
    fib = fibonacci(4e6)
    result = sum_evens(fib)
    print(result)
