#!/usr/bin/python3

# Longest Collatz sequence
# Problem 14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

from typing import Sequence


def CollatzSequence(n:int,seq_dict:dict={}) -> dict:
    """Generate Collatz Sequence from n

        Args:
            n (int): input to generate Collatz Sequence from
            seq_dict (dict, optional): cache of all calculated sequences encountered. Defaults to {}.

        Returns:
            dict: returns dict seq_dict
    """
    sequence=[]
    current_n=n
    while current_n > 1:
        if current_n in seq_dict:
            sequence.extend(seq_dict[current_n])
            break
        elif current_n % 2 == 0:
            current_n = current_n//2
        else:
            current_n = 3*current_n +1
        sequence.append(current_n)
    seq_dict[n]=sequence
    sequenceLength=len(sequence)
    for i in range(sequenceLength):
        collatzN=sequence[sequenceLength-i-1]
        if collatzN not in seq_dict:
            childList = sequence[sequenceLength-i:]
            seq_dict[collatzN]=childList
    return seq_dict
    
collatzSequenceDict={}

if __name__ == "__main__":
    t=collatzSequenceDict=CollatzSequence(837799, collatzSequenceDict)
    result="hi"
    for n in range(2,int(1e6)):
        collatzSequenceDict=CollatzSequence(n, collatzSequenceDict)
    
    collatzSequenceIndex=0
    collatzSequenceCount=0
    
    for n in range(1,int(1e6)):
        if n > 837797:
            print("break")
        current_length=len(collatzSequenceDict[n])
        if current_length > collatzSequenceCount:
            collatzSequenceIndex=n
            collatzSequenceCount=current_length
    result=collatzSequenceIndex
    print(result)


