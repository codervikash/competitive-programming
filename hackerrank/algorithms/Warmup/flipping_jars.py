# Filling Jars

# Animesh has N empty candy jars, numbered from 1 to N, with infinite capacity. He performs M operations. Each operation is described by 3 integers a, b and k. Here, a and b are indices of the jars, and k is the number of candies to be added inside each jar whose index lies between a and b (both inclusive). Can you tell the average number of candies after M operations?


# Enter your code here. Read input from STDIN. Print output to STDOUT
def candy(a, b):
    total = 0
    for i in range(b):
        x, y, z = map(int, raw_input().strip().split(' '))

    # using this is inefficient and results in runtime error in large trstcases
    #     for j in range(x,y+1):
    #         final[j] = final.get(j,0)+z
    # result = sum(final.values())/a

        total = total + (y - x + 1) * (z)
    result = total / a
    print (result)


a, b = map(int, raw_input().strip().split(" "))
result = candy(a, b)
