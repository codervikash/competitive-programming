# Jim is off to a party and is searching for a matching pair of socks. His drawer is filled with socks, each pair of a different color. In its worst case scenario, how many socks (x) should Jim remove from his drawer after which he finds a matching pair?

# Input Format
# The first line contains the number of test cases T.
# Next T lines contains an integer N which indicates the total pairs of socks present in the drawer.

# Output Format
# Print the number of Draws (x) Jim makes in the worst case scenario.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def draw(a):
    if a == 1:
        return 2
    else:
        return (a + 1)


n = int(raw_input())
for i in range(n):
    a = int(raw_input())
    ans = draw(a)
    print ans