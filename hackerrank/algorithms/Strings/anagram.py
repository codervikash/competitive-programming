# Problem Statement
#
# Sid is obsessed with reading short stories. Being a CS student, he is doing some interesting frequency analysis with the books. He chooses strings S1 and S2 in such a way that |len(S1)−len(S2)|≤1.
#
# Your task is to help him find the minimum number of characters of the first string he needs to change to enable him to make it an anagram of the second string.
#
# Note: A word x is an anagram of another word y if we can produce y by rearranging the letters of x.
#
# Input Format The first line will contain an integer, T, representing the number of test cases. Each test case will contain a string having length len(S1)+len(S2), which will be concatenation of both the strings described above in the problem.The given string will contain only characters from a to z.
#
# Output Format An integer corresponding to each test case is printed in a different line, i.e. the number of changes required for each test case. Print −1 if it is not possible.
#
# Constraints 1≤T≤100
# 1≤len(S1)+len(S2)≤104


# Enter your code here. Read input from STDIN. Print output to STDOUT
def anagram(a):
    count1 = [0] * 26
    count2 = [0] * 26
    count = 0
    length = len(a)
    if length % 2 != 0:
        return -1
    else:
        for i in a[0: (length / 2)]:
            count1[ord(i) - 97] += 1

            for i in a[length / 2: length]:
                count2[ord(i) - 97] += 1

                for i in range(26):
                    count += abs(count1[i] - count2[i])
                    return count / 2


x = int(raw_input())

for i in range(x):
    a = raw_input()
    answer = anagram(a)
    print (answer)
