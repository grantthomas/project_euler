# Maximum path sum I
# Problem 18
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 00 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


def TriangleNextStep(current_index: int, nextLevel: list) -> int:
    path_left = nextLevel[current_index]
    path_right = nextLevel[current_index + 1]

    if path_right < path_left:
        return (current_index, path_left)
    return (current_index + 1, path_right)


def naive_solution():
    """Misinterpret the problem as asking to choose the path to the bottom maximizing the move to the next level.

    Returns:
        [int]: return correct sum if the interpretation was correct.
    """
    current_index = 0
    current_level = 0

    result = triangle[0][0]

    print(0, result, result)
    while current_level < len(triangle) - 1:
        current_index, current_value = TriangleNextStep(
            current_index=current_index, nextLevel=triangle[current_level + 1]
        )
        current_level += 1
        result += current_value
        print(current_index, current_value, result)
    return result


def TriangleWalkMaxSum(triangle) -> int:
    """Find the path from the top of the triangle to the bottom providing the largest possible sum.

    Args:
        triangle (list): triangular list

    Returns:
        int: sum of steps producing highext value
    """
    for level in range(len(triangle) - 2, -1, -1):
        for index in range(len(triangle[level])):
            current_index = index
            nextLevel = triangle[level + 1]
            tt = TriangleNextStep(current_index, nextLevel)
            triangle[level][current_index] += tt[1]
    return triangle[0][0]


if __name__ == "__main__":
    result = "result"

    # triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    triangle = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [0, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]
    # result = naive_solution()

    # TODO The problem is asking for maximum possible route, not maximum of the next step.

    result = TriangleWalkMaxSum(triangle=triangle)

    print(result)
