# Billionaire
# Problem 267
# You are given a unique investment opportunity.

# Starting with £1 of capital, you can choose a fixed proportion, f, of your capital to bet on a fair coin toss repeatedly for 1000 tosses.

# Your return is double your bet for heads and you lose your bet for tails.

# For example, if f = 1/4, for the first toss you bet £0.25, and if heads comes up you win £0.5 and so then have £1.5.
# You then bet £0.375 and if the second toss is tails, you have £1.125.

# Choosing f to maximize your chances of having at least £1,000,000,000 after 1,000 flips, what is the chance that you become a billionaire?

# All computations are assumed to be exact (no rounding), but give your answer rounded to 12 digits behind the decimal point in the form 0.abcdefghijkl.

import pprint
import random


def PlaceBet(balance: float, rate: float) -> float:
    """Simulate betting on a coin toss

        Args:
            balance (float): current total purse
            rate (float): percentage of total purse to wager

        Returns:
            float: purse after bet
    Note this may not be part of the problem.
    """
    coinFlip = random.choice(seq=[0, 1])

    if coinFlip == False:
        outcome = balance + ((balance * rate) * -1)
        return outcome

    outcome = balance + ((balance * rate) * 2)
    return outcome


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    result = "result"

    balance = 1.0
    bet = 0.05

    for i in range(1000):
        balance = PlaceBet(balance=balance, rate=bet)
        print(f"{i+1} : {balance}")
        if balance <= 0.0:
            break

    pp.pprint(f"{result}")

    f = 0
    rate = 0
    for i in range(2, 110):
        magnitude = 10
        t_rate = pow((1 / i * magnitude), 10)
        print(f"{i} 1/{i*magnitude} {t_rate}")
        if t_rate > rate:
            f = i
            rate = t_rate
