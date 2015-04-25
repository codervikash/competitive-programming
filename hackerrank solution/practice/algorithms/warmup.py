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


# Game of Thrones - I

# Dothraki are planning an attack to usurp King Robert from his kingdom. King Robert learns of this conspiracy from Raven and plans to lock the single door through which an enemy can enter his kingdom.

# But, to lock the door he needs a key that is an anagram of a certain palindrome string.

# The king has a string composed of lowercase English letters. Help him figure out if any anagram of the string can be a palindrome or not.

string = raw_input()

found = False
x=0
y = 0
comp = set(string)
comp = list(comp)
for i in range(len(comp)):
    for j in range(len(string)):
        if comp[i] == string[j]:
            x +=1
            j += 1
        else:
            j +=1
    if x%2 == 0:
        pass
    else:
        y +=1
    i +=1
    x = 0
    j = 0
if len(string)%2 == 0:
    if y == 0:
        found = True
    else:
        found = False
else:
    if y == 1:
        found = True
    else:
        found = False

if not found:
    print("NO")
else:
    print("YES")

# some much efficient alternatives:
# 1st

st=raw_input()
arr=[0]*27;
for i in range(len(st)):
    cnt=ord(st[i])-ord('a')
    arr[cnt]+=1
co=0
ce=0
for i in range(26):
    if arr[i]%2==0:
        ce+=1
    else:
        co+=1
if co>1:
    print "NO"
else:
    print "YES"

#2nd

s=raw_input()
cnt={}
for c in s:
    cnt[c]=cnt.get(c,0)+1
nodd=len(filter(lambda x:x%2==1, cnt.values()))
print ["NO","YES"][nodd<=1]


# Filling Jars

# Animesh has N empty candy jars, numbered from 1 to N, with infinite capacity. He performs M operations. Each operation is described by 3 integers a, b and k. Here, a and b are indices of the jars, and k is the number of candies to be added inside each jar whose index lies between a and b (both inclusive). Can you tell the average number of candies after M operations?


# Enter your code here. Read input from STDIN. Print output to STDOUT
def candy(a,b):
    final = {}
    for i in range(b):
        x,y,z = map(int,raw_input().strip().split(' '))

    #using this is inefficient and results in runtime error in large trstcases
    #     for j in range(x,y+1):
    #         final[j] = final.get(j,0)+z
    # result = sum(final.values())/a

        total = total + (y-x+1)*(z)
    result = total/a

    print result



a,b = map(int, raw_input().strip().split(" "))
result = candy(a,b)


# Sherlock and Squares

# Watson gives two integers A & B to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).

# A square integer is an integer which is the square of any integer. For example, 1, 4, 9, 16 are some of the square integers as they are squares of 1, 2, 3, 4 respectively.

# Input Format
# First line contains T, the number of testcases. T test cases follow, each in a newline.
# Each testcase contains two space separated integers denoting A and B.


# Enter your code here. Read input from STDIN. Print output to STDOUT
def sherlock(a,b):
    answer = int((b)**0.5) - int((a-1)**0.5)
    return answer

n = int(raw_input())
for i in range(n):
    a,b = map(int,raw_input().split())
    answer = sherlock(a,b)
    print answer


# Chocolate Feast

# Little Bob loves chocolates, and goes to a store with $N in his pocket. The price of each chocolate is $C. The store offers a discount: for every M wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?


# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    answer = A/B
    wrapper = A/B
    while wrapper >= C1:
        answer += (wrapper/C1)
        wrapper = (wrapper % C1) + (wrapper/C1)
    result = answer
    print result




# Enter your code here. Read input from STDIN. Print output to STDOUT
def stones(a,b,n):
    for i in range(a):
        if a == b:
            return " ".join(map(str,[a * (n - 1)]))
        if a < b:
            return stones(b, a, n)
        return " ".join(map(str,[i * a + (n - i - 1) * b for i in range(n)]))



# Manasa and Stones

# Problem Statement

# Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that two consecutive stones have a difference of either a or b. Legend has it that there is a treasure trove at the end of the trail and if Manasa can guess the value of the last stone, the treasure would be hers. Given that the number on the first stone was 0, find all the possible values for the number on the last stone.

# Note : The numbers on the stones are in increasing order


n = int(raw_input())
for _ in range(n):
    c = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    answer = stones(a,b,c)
    print answer


# Angry Professor

Problem Statement

# The professor is conducting a course on Discrete Mathematics to a class of N students. He is angry at the lack of their discipline, and he decides to cancel the class if there are less than K students present after the class starts.

# Given the arrival time of each student, your task is to find out if the class gets cancelled or not.


# Enter your code here. Read input from STDIN. Print output to STDOUT

def angry(x,y):
    z = 0
    a = map(int,raw_input().split())
    for b in range(x):
        if a[b] <= 0:
            z+=1


    if z >= y:
        return 'NO'
    else:
        return 'YES'

x = int(raw_input())
for _ in range(x):
    y,z = map(int,raw_input().strip().split())
    answer = angry(y,z)
    print answer



# You are given N sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

# Suppose we have six sticks of the following lengths:

# 5 4 4 2 2 8
# Then, in one cut operation we make a cut of length 2 from each of the six sticks. For the next cut operation four sticks are left (of non-zero length), whose lengths are the following:

# 3 2 2 6
# The above step is repeated until no sticks are left.

# Given the length of N sticks, print the number of sticks that are cut in subsequent cut operations.


    # Enter your code here. Read input from STDIN. Print output to STDOUT
def stick(x,y):
    z = len(y)
    b = []
    h = 0
    for a in range(z):
        if y[a] >= x:
            q = y[a] - x
            b.append(q)
        else:
            pass

    c = len(b)
    if c > 1:
        print c
        d = filter(lambda t: t != 0, b)
        f = sorted(d)
        e = d[0]
        stick(e,f)

    else:
        print c


x = int(raw_input())
y = map(int, raw_input().split())
m = sorted(y)
w = m[0]
stick(w,m)


# Given two integers, L and R, find the maximal value of A xor B, where A and B satisfy the following condition:

# L≤A≤B≤R


#!/bin/python

# Complete the function below.


def  maxXor( l,  r):
    a = 0
    for i in range(l ,r+1):
        for j in range(l,r+1):
            b = i ^ j
            if b > a: a = b

    return a


_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)


