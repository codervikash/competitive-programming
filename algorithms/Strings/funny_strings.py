# Suppose you have a string S which has length N and is indexed from 0 to N−1. String R is the reverse of the string S. The string S is funny if the condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.
#
# (Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str. |x| denotes the absolute value of an integer x)
#
# Input Format
#
# First line of the input will contain an integer T. T testcases follow. Each of the next T lines contains one string S.
#
# Constraints
#
# 1<=T<=10
# 2<=length of S<=10000
# Output Format
#
# For each string, print Funny or Not Funny in separate lines.
#


# Enter your code here. Read input from STDIN. Print output to STDOUT

def funny(a):
	l = len(a)
	count = 0
	for i in range(1,l):
		if abs(ord(a[i]) - ord(a[i - 1])) == abs(ord(a[l - i]) - ord(a[l - i -1])):
			count += 1
		else:
			return 'Not Funny'

		if count == l -1:
			return 'Funny'


x = int(raw_input())


for i in range(x):
	y = raw_input()
	answer = funny(y)
	print answer
