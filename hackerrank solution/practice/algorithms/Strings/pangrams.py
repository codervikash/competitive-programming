# Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)
#
# After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.
#
# Given a sentence s, tell Roy if it is a pangram or not.
#
# Input Format Input consists of a line containing s.
#
# Constraints
# Length of s can be at most 103 (1≤|s|≤103) and it may contain spaces, lower case and upper case letters. Lower case and upper case instances of a letter are considered the same.
#
# Output Format Output a line containing pangram if s is a pangram, otherwise output not pangram.


# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = raw_input().replace(' ','').lower()
b= collections.Counter(a)
c = list(set(b.elements()))
if set(x).issubset(c):
	print('pangram')
else:
	print('not pangram')
