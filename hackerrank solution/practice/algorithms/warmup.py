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


