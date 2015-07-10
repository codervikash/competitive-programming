# Utopian Tree

# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter.
# Now, a new Utopian tree sapling is planted at the onset of the spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?


def utopian(a):
    answer = 1
    for i in range(a):
        if i % 2 == 0:
            answer *= 2
        else:
            answer += 1
    return answer

n = int(raw_input())
for i in range(n):
    a = int(raw_input())
    answer = utopian(a)
    print (answer)
