# Angry Professor

# Problem Statement

# The professor is conducting a course on Discrete Mathematics to a class of N students. He is angry at the lack of their discipline, and he decides to cancel the class if there are less than K students present after the class starts.

# Given the arrival time of each student, your task is to find out if the class gets cancelled or not.


# Enter your code here. Read input from STDIN. Print output to STDOUT

def angry(x, y):
    z = 0
    a = map(int, raw_input().split())
    for b in range(x):
        if a[b] <= 0:
            z += 1

    if z >= y:
        return 'NO'
    else:
        return 'YES'

x = int(raw_input())
for _ in range(x):
    y, z = map(int, raw_input().strip().split())
    answer = angry(y, z)
    print (answer)
