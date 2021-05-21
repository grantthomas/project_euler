# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num:int) -> bool:
    input = str(num)
    to_check = input[::-1]

    result=(input == to_check)
    return result

def find_largest_palindrome(num_min:int, num_max:int) -> int:
    pass
    result = -1
    for n_a in range(num_max,num_min,-1):
        for n_b in range(n_a,num_min,-1):
            product = n_a*n_b
            if is_palindrome(product):
                if product > result:
                    result = product
    return result


if __name__ == "__main__":
    num_min = int(1e2)
    num_max = int(1e3)-1
    
    result = find_largest_palindrome(num_min,num_max)
    print(result)