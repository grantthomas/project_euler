# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right
# in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a
# 1001 by 1001 spiral formed in the same way?

import math
import pprint

# Thoughts: start at center with n=0, each ring n+=1. Where n>0:
#   spacing for each diag where == 2n.
#       n1=( 3, 5, 7, 9)
#       n2=(13,17,21,25)
#   total spots on each ring == 2^(n+2).
#       n1=2^(1+2)=8
#       n2=2^(2+2)=16
#   top right corner on each ring == (2n+1)^2
#       n1=(2*1+1)^2=3^2=9
#       n2=(2*2+1)^2=5^2=25.
#   bottom left corner on each ring == 1+(2n)^2
#       n1=1+(2*1)^2=5
#       n2=1+(2*2)^2=17
# Write out 2 more rings and see if pattern holds.
#   73	74	75	76	77	78	79	80	81
#   72	43	44	45	46	47	48	49	50
#   71	42	21	22	23	24	25	26	51
#   70	41	20	7	8	9	10	27	52
#   69	40	19	6	1	2	11	28	53
#   68	39	18	5	4	3	12	29	54
#   67	38	17	16	15	14	13	30	55
#   66	37	36	35	34	33	32	31	56
#   65	64	63	62	61	60	59	58	57


class NumberSpiral:
    def __init__(self, length):
        self.length = length
        self.TRList = self.TRs()
        self.CornerList = self.Corners()
        self.DiagSums = self.SumDiags()

    def TRs(self):
        trCorners = [1]
        if (self.length % 2 == 0) or (self.length < 1):
            return [-1]
        if self.length == 1:
            return trCorners
        rings = (self.length - 1) // 2 + 1
        for n in range(1, rings):
            corner = (2 * n + 1) ** 2
            trCorners.append(corner)

        return trCorners

    def Corners(self):
        # TR-(2n),TR-2*(2n),TR-3*(2n)
        corners = [[1]]
        if (self.length % 2 == 0) or (self.length < 1):
            return [[-1]]
        if self.length == 1:
            return corners
        for i, TR in enumerate(self.TRList):
            corners.append([TR - 3 * (2 * i), TR - 2 * (2 * i), TR - (2 * i), TR])
        corners.remove([1, 1, 1, 1])
        return corners

    def SumDiags(self):
        total = 0
        for i in range(len(self.CornerList)):
            total += sum(self.CornerList[i])
        return total


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    result = "result"

    # Process:
    #   - Find TR for each ring.
    #       - TR=(2n+1)^2
    #   - fill in prev 3 corners.
    #       - TR-(2n),TR-2*(2n),TR-3*(2n)
    #   - add all to list
    #   - summ full list

    n = NumberSpiral(1001)
    pp.pprint(n.DiagSums)
