"""
You are given a list of NN people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic or they are not. Find out the maximum number of topics a 2-person team can know. And also find out how many teams can know that maximum number of topics.

Note Suppose a, b, and c are three different people, then (a,b) and (b,c) are counted as two different teams.

Input Format

The first line contains two integers, NN and MM, separated by a single space, where NN represents the number of people, and MM represents the number of topics. NN lines follow.
Each line contains a binary string of length MM. If the iith line's jjth character is 11, then the iith person knows the jjth topic; otherwise, he doesn't know the topic.

Constraints
2≤N≤5002≤N≤500
1≤M≤5001≤M≤500

Output Format

On the first line, print the maximum number of topics a 2-person team can know.
On the second line, print the number of 2-person teams that can know the maximum number of topics.

Sample Input

4 5
10101
11100
11010
00101
Sample Output

5
2
"""
