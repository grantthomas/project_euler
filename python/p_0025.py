# 1000-digit Fibonacci number
# Problem 25

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from p_0002 import fibonacci
import pprint


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    result = "result"
    fib = fibonacci(10 ** 1000)

    for n in fib[::-1]:
        if len(str(n)) < 1000:
            result = fib.index(n) + 2
            break

    for n in fib[result - 1 :]:
        t = len(str(n))

    pp.pprint(result)
