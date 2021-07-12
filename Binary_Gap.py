"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both
 ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary
representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no
binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N
doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its
longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation
'100000' and thus no binary gaps. """

import re
from functools import reduce


def solution(N):
    # write your code in Python 3.6
    data = bin(N).replace('0b', "")
    # m = re.findall("(?=(10+1))+", data)
    # if len(m) > 0:
    #     len1 = list(map(lambda x: len(x) - 2, m))
    #     return max(len1)
    # return 0

    # Using reduce :
    # data = bin(N).replace('0b', "")
    # m = re.findall("(?=(10+1))+", data)
    # if len(m) > 0:
    #     len1 = reduce(lambda x, y: x if len(x) > len(y) else y, m)
    #     return len(len1) - 2
    # return 0

    max_len = 0
    counter = 0
    for i in data:
        if i == "1":
            if counter > max_len:
                max_len = counter;
            counter = 0
        else:
            counter += 1

    print(max_len)


# 10
print(solution(1041))
