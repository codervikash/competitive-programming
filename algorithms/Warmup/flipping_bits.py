# Flipping bits

# You will be given a list of 32-bits unsigned integers. You are required to output the list of the unsigned integers you get by flipping bits in its binary representation (i.e. unset bits must be set, and set bits must be unset).


def flipping(a):
    ans = ~a & 0xffffffff
    return ans

n = int(raw_input())
for i in range(n):
    a = int(raw_input())
    ans = flipping(a)
    print (ans)
