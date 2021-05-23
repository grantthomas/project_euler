# Number letter counts
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import pprint


def ProcessWordRange(
    num_words: dict, num: int, start: int = 1, word_list: list = []
) -> list:

    num = 1 if num < 1 else num
    word_list = []
    for n in range(start, num + 1):
        word_list.append(NumToWords(n, num_words, word_list))
    return word_list


def NumToWords(n, num_words, word_list):
    if n == 0:
        return ""
    if n not in num_words:
        magnitude = 10 ** (len(str(n)) - 1)
        part_l = (n // magnitude) * magnitude
        part_r = n - part_l
        if part_l % 1000 == 0:

            hundo = part_l // 1000
            word_l = NumToWords(hundo, num_words, word_list) + "thousand"
        elif part_l % 100 == 0:

            hundo = part_l // 100
            word_l = NumToWords(hundo, num_words, word_list) + "hundred"
        else:
            word_l = num_words[part_l]

        if part_r in num_words:
            word_r = num_words[part_r]
        else:
            word_r = NumToWords(part_r, num_words, word_list)

        modifier = " and " if ((n > 100) and (n % 100 > 0)) else ""
        return word_l + modifier + word_r
    return num_words[n]


if __name__ == "__main__":
    result = "result"

    num_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    word_list = ProcessWordRange(num_words=num_words, start=1, num=1000, word_list=[])
    concat = "".join(word_list)
    result = len(concat.replace(" ", ""))

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(word_list)
    print(result)
    print("done")
