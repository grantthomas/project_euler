# Names scores
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import pprint
import string


def StrToChar(input: str) -> list:
    """converts string to list of characters

    Args:
        input (str): string in

    Returns:
        list: list of chars out
    """
    return [x for x in input]


def NameToScore(name: str) -> list:
    chars = StrToChar(name)
    name_index = []
    for letter in chars:
        letterIndex = string.ascii_uppercase.index(letter) + 1
        name_index.append(letterIndex)
    name_sum = sum(name_index)
    return name_sum


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    result = "result"

    name_file = open("p022_names.txt", "r")
    name_list = name_file.readline().replace('"', "").split(sep=",")
    name_list.sort()

    scores = []
    name_scores = {}
    for name in name_list:
        name_sum = NameToScore(name)
        name_index = name_list.index(name) + 1
        score = name_sum * name_index
        name_scores[name] = score

    result = sum(name_scores.values())

    pp.pprint(result)
