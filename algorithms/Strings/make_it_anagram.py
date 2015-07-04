# Alice recently started learning about cryptography and found that anagrams are very useful. Two strings are anagrams of each other if they have same character set and same length. For example strings "bacdc" and "dcbac" are anagrams, while strings "bacdc" and "dcbad" are not.
#
# Alice decides on an encryption scheme involving 2 large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. She need your help in finding out this number.
#
# Given two strings (they can be of same or different length) help her in finding out the minimum number of character deletions required to make two strings anagrams. Any characters can be deleted from any of the strings.
#
# Input Format
# Two lines each containing a string.
#
# Constraints
# 1 <= Length of A,B <= 10000
# A and B will only consist of lowercase latin letter.
#
# Output Format
# A single integer which is the number of character deletions.


x = raw_input()
y = raw_input()
s1 = [0]*26
s2 = [0]*26
count = 0

for i in x:
	s1[ord(i) - 97] += 1
for i in y:
	s2[ord(i) - 97] += 1

for i in range(26):
	count += abs(s1[i] - s2[i])

print count
