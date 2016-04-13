# https://www.hackerrank.com/challenges/bear-and-workbook

# Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters.
#
# There are n chapters in Lisa's workbook, numbered from 1 to n.
# The i-th chapter has ti problems, numbered from 1 to ti.
#
# Each page can hold up to k problems. There are no empty pages or unnecessary spaces, so only the last page of a chapter may contain fewer than k  problems.
# Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
# The page number indexing starts at 1.
# Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. Given the details for Lisa's workbook, can you count its number of special problems?
#
# Note: See the diagram in the Explanation section for more details.
#
# Input Format
#
# The first line contains two integers n and k — the number of chapters and the maximum number of problems per page respectively.
# The second line contains n integers t1,t2,…,tn, where ti denotes the number of problems in the i-th chapter.
#
# Constraints
# 1≤n,k,ti≤100
#
# Output Format
#
# Print the number of special problems in Lisa's workbook.
#
# Sample Input
#
# 5 3
# 4 2 6 1 10
# Sample Output
#
# 4

a, b = map(int, raw_input().split())
x = [i for i in (map(int, raw_input().split()))]
y = 0
z = 1
for i in xrange(a):
    p = x[i]
    n = p/b if p % b is 0 else p/b + 1
    for i in xrange(z, z+n+1):
        c = (b*((i-z)+1))+1 if (b*((i-z)+1)) < p else p+1
        if i in xrange((b*(i-z))+1, c):
            y += 1
    z += n
print y
