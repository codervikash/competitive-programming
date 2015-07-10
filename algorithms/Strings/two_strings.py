# Problem Statement
#
# You are given two strings, A and B. Find if there is a substring that appears in both A and B.
#
# Input Format
#
# Several test cases will be given to you in a single file. The first line of the input will contain a single integer T, the number of test cases.
#
# Then there will be T descriptions of the test cases. Each description contains two lines. The first line contains the string A and the second line contains the string B.
#
# Output Format
#
# For each test case, display YES (in a newline), if there is a common substring. Otherwise, display NO.
#
# Constraints
#
# All the strings contain only lowercase Latin letters.
# 1<=T<=10
# 1<=|A|,|B|<=105


# Enter your code here. Read input from STDIN. Print output to STDOUT
def strings(a, b):
    p = [0] * 26
    for i in a:
        p[ord(i) - 97] += 1
    for j in b:
        if p[ord(j) - 97]:
            return 'YES'

    return 'NO'

x = int(raw_input())

for i in range(x):
    a = raw_input()
    b = raw_input()
    ans = strings(a, b)
    print (ans)
