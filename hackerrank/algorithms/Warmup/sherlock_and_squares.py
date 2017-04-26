# Sherlock and Squares

# Watson gives two integers A & B to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).

# A square integer is an integer which is the square of any integer. For example, 1, 4, 9, 16 are some of the square integers as they are squares of 1, 2, 3, 4 respectively.

# Input Format
# First line contains T, the number of testcases. T test cases follow, each in a newline.
# Each testcase contains two space separated integers denoting A and B.


# Enter your code here. Read input from STDIN. Print output to STDOUT
def sherlock(a, b):
    answer = int((b) ** 0.5) - int((a - 1) ** 0.5)
    return answer

n = int(raw_input())
for i in range(n):
    a, b = map(int, raw_input().split())
    answer = sherlock(a, b)
    print (answer)
