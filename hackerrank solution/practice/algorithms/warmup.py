# Lonely Integer

# There are N integers in an array A. All but one integer occur in pairs. Your task is to find out the number that occurs only once.

#!/usr/bin/py
def lonelyinteger(a):
    answer = 0
    x = len(a)
    for i in range(x):
        answer ^= a[i]
        i +=1
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)


# Flipping bits

# You will be given a list of 32-bits unsigned integers. You are required to output the list of the unsigned integers you get by flipping bits in its binary representation (i.e. unset bits must be set, and set bits must be unset).

def flipping(a):
    ans = ~a & 0xffffffff
    return ans

n = int(raw_input())
for i in range(n):
    a = int(raw_input())
    ans = flipping(a)
    print ans


# Utopian Tree

# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter.
# Now, a new Utopian tree sapling is planted at the onset of the spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

def utopian(a):
    answer = 1
    for i in range(a):
        if i%2 == 0:
            answer *= 2
        else:
            answer +=1
    return answer

n = int(raw_input())
for i in range(n):
    a = int(raw_input())
    answer = utopian(a)
    print answer


# The Love-Letter Mystery

# James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

# To do this, he follows 2 rules:

# (a) He can reduce the value of a letter, e.g. he can change 'd' to 'c', but he cannot change 'c' to 'd'.
# (b) In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes 'a'. Once a letter has been changed to 'a', it can no longer be changed.

# Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.


def love(a):
    x = len(a)
    y  = x-1
    j = 0
    for i in range(x/2):
        if a[i] == a[y-i]:
            i +=1
        else:
            j += abs(ord(a[i]) - ord(a[y-i]))
            i +=1
    return j


n = int(raw_input())
for i in range(n):
    a = raw_input()
    answer = love(a)
    print answer


# Alternating Characters

# Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.


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





