
# Manasa and Stones

# Problem Statement

# Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that two consecutive stones have a difference of either a or b. Legend has it that there is a treasure trove at the end of the trail and if Manasa can guess the value of the last stone, the treasure would be hers. Given that the number on the first stone was 0, find all the possible values for the number on the last stone.

# Note : The numbers on the stones are in increasing order

# Enter your code here. Read input from STDIN. Print output to STDOUT
def stones(a,b,n):
    for i in range(a):
        if a == b:
            return " ".join(map(str,[a * (n - 1)]))
        if a < b:
            return stones(b, a, n)
        return " ".join(map(str,[i * a + (n - i - 1) * b for i in range(n)]))





n = int(raw_input())
for _ in range(n):
    c = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    answer = stones(a,b,c)
    print answer
