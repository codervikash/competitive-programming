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



