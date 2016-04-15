# Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar's cipher rotated every letter in a string by a fixed number, KK, making it unreadable by his enemies. Given a string, SS, and a number, KK, encrypt SS and print the resulting string.
#
# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
#
# Input Format
#
# The first line contains an integer, NN, which is the length of the unencrypted string.
# The second line contains the unencrypted string, SS.
# The third line contains the integer encryption key, KK, which is the number of letters to rotate.
#
# Constraints
# 1≤N≤1001≤N≤100
# 0≤K≤1000≤K≤100
# SS is a valid ASCII string and doesn't contain any spaces.
#
# Output Format
#
# For each test case, print the encoded string.
#
# Sample Input
#
# 11
# middle-Outz
# 2
# Sample Output
#
# okffng-Qwvb


n = int(raw_input().strip())
s = x = map(str, raw_input().strip())
k = int(raw_input().strip())

for i in xrange(n):
    if s[i] >= 'A' and s[i] <= 'Z':
        y = (ord(s[i]) + k) if (ord(s[i]) + k) <= ord('Z') else (64 + (((ord(s[i]) + k) - ord('Z')) % 26))
        x[i] = chr(y) if y > 64 else chr(90)
    elif s[i] >= 'a' and s[i] <= 'z':
        y = (ord(s[i]) + k) if (ord(s[i]) + k) <= ord('z') else (96 + (((ord(s[i]) + k) - ord('z')) % 26))
        x[i] = chr(y) if y > 96 else chr(122)

print ''.join(x)
