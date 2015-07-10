# Problem Statement
#
# Given a word w, rearrange the letters of w to construct another word s in such a way that s is lexicographically greater than w. In case of multiple possible answers, find the lexicographically smallest one.
#
# Input Format
#
# The first line of input contains t, the number of test cases. Each of the next t lines contains w.
#
# Constraints
# 1≤t≤105
# 1≤|w|≤100
# w will contain only lower-case English letters and its length will not exceed 100.
#
# Output Format
#
# For each testcase, output a string lexicographically bigger than w in a separate line. In case of multiple possible answers, print the lexicographically smallest one, and if no answer exists, print no answer.


def findceil(a, first, l, h):
        index = l
        for i in range(l + 1, h + 1):
            if a[i] > first and a[i] < a[index]:
                index = i
        return index


def sorting(a, b, size):
        for i in range(b + 1, size):
            for j in range(b + 1, size - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a


def bigger(i):
    i = list(i)
    length = len(i)

    for j in xrange(length - 2, -2, -1):
        if i[j] < i[j + 1]:
            break
    if j == -1:
        return 'no answer'

    else:
        index = findceil(i, i[j], j + 1, length - 1)
        i[j], i[index] = i[index], i[j]
        sorting(i, j, length)

    return ''.join(i)

x = int(raw_input())
for i in range(x):
    a = raw_input()
    answer = bigger(a)
    print(answer)
