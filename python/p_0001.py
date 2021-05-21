#Multiples of 3 and 5
#Problem 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiples_to_n(factors: list, n: int) -> int:
    result=0
    for i in range(1,n):
        if i%3==0:
            result += i
        elif i%5==0:
            result += i
    return result


if __name__ == "__main__":
    factors=[3,5]
    number=1000

    result=sum_multiples_to_n(factors, number)
    print(result)