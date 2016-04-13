# Chocolate Feast

# Little Bob loves chocolates, and goes to a store with $N in his pocket. The price of each chocolate is $C. The store offers a discount: for every M wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?


# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(0, T):
    A, B, C1 = [int(x) for x in raw_input().split(' ')]
    answer = A / B
    wrapper = A / B
    while wrapper >= C1:
        answer += (wrapper / C1)
        wrapper = (wrapper % C1) + (wrapper / C1)
    result = answer
    print (result)
