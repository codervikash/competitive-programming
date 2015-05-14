# Problem Statement

# Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

# Your task is to find the minimum number of required deletions.

# Input Format

# The first line contains an integer T, i.e. the number of test cases.
# The next T lines contain a string each.

# Output Format

# For each test case, print the minimum number of deletions required.

# Constraints

# 1≤T≤10
# 1≤ length of string ≤105

# Enter your code here. Read input from STDIN. Print output to STDOUT
def character(a):
    ans= 0
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            ans +=1
    return ans


n = int(raw_input())
for i in range(n):
    a = raw_input()
    answer = character(a)
    print answer