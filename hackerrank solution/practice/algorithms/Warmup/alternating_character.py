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