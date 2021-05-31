# Reciprocal cycles
# Problem 26

# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the
# longest recurring cycle in its decimal fraction part.

import pprint

# Playing with classes, likely horribly inefficient way to do this.
class UnitFraction:
    def __init__(self, num):
        self.num = num
        self.dec = str(1 / num)
        self.notation = self.FindRepeats()

    def FindRepeats(self):
        if len(self.dec) < 10:
            return self.dec
        # test if a single numeral is repeated, including after non-repeating
        # num (0.333... 0.666...0.1666...)
        for pos in range(2, len(self.dec)):
            decString = self.dec[pos:]
            repeatCount = list(decString).count(decString[0])
            if repeatCount == len(decString) & repeatCount > 3:
                string = f"{self.dec[:pos]}({decString[0]})"
                return string

        return "-1"

    notation = "-1"


d = UnitFraction(8)
print(vars(d))


if __name__ == "_main__":
    pp = pprint.PrettyPrinter(indent=4)
    result = "result"

    limit = 11

    repeats = []
    for d in range(1, limit):
        dec = 1 / d
        decStr = str(dec)
        if len(decStr) > 10:
            repeats.append([d, decStr[2:]])
            # print(decStr, len(decStr))
    notation = []
    for d, decStr in repeats:
        decList = list(decStr)
        decLen = len(decStr)
        firstCount = decList.count(decList[0])
        if firstCount == decLen:
            notation.append(f"0.({decList[0]})")
        print(decStr, decLen, firstCount)

    print(notation)
    # pp.pprint(repeats)
