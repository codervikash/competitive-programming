# Sherlock Holmes suspects his archenemy, Professor Moriarty, is once again
#   plotting something diabolical. Sherlock's companion, Dr. Watson,
#   suggests Moriarty may be responsible for MI6's recent issues with
#   their supercomputer, The Beast.
#
# Shortly after resolving to investigate, Sherlock receives a note from
#   Moriarty
#   boasting about infecting The Beast with a virus; however, he also gives him
#   a clue—a number, N
#
# Sherlock determines the key to removing the virus is to find the largest
#   Decent Number having N digits.
#
# A Decent Number has the following properties:
#
# Its digits can only be 3's and/or 5's.
# The number of 3's it contains is divisible by 5.
# The number of 5's it contains is divisible by 3.
# If there are more than one such number, we pick the largest one.
# Moriarty's virus shows a clock counting down to The Beast's destruction, and
#   time is running out fast. Your task is to help Sherlock find the key before
#   The Beast is destroyed!
#
# Constraints
# 1≤T≤20
# 1
# T
# 20
#
# 1≤N≤100000
# 1
# N
# 100000
#
#
#
# Input Format
#
# The first line is an integer, T
# T
# , denoting the number of test cases.
#
# The T
# T
#  subsequent lines each contain an integer, N
# N
# , detailing the number of digits in the number.
#
# Output Format
#
# Print the largest Decent Number having N
# N
#  digits; if no such number exists, tell Sherlock by printing -1.
#
# Sample Input
#
# 4
# 1
# 3
# 5
# 11
# Sample Output
#
# -1
# 555
# 33333
# 55555533333
# Explanation
#


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    m = n
    while m % 3 is not 0:
        m -= 5
    if m < 0:
        print -1
    else:
        print m*'5'+(n-m)*'3'
