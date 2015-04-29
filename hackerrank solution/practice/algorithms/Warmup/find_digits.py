# Problem Statement

# You are given an integer N. Find the digits in this number that exactly divide N (division that leaves 0 as remainder) and display their count. For N=24, there are 2 digits (2 & 4). Both of these digits exactly divide 24. So our answer is 2.

# Note

# If the same number is repeated twice at different positions, it should be counted twice, e.g., For N=122, 2 divides 122 exactly and occurs at ones' and tens' position. So for this case, our answer is 3.
# Division by 0 is undefined.
# Input Format

# The first line contains T (the number of test cases), followed by T lines (each containing an integer N).

# Constraints
# 1≤T≤15
# 0<N<1010
# Output Format

# For each test case, display the count of digits in N that exactly divide N in a separate line.

# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(raw_input())
for _ in range(x):
  y = int(raw_input())
  z = str(y)
  a = 0
  for i in z:
    if int(i) == 0:
      pass
    elif y % int(i) == 0 :
      a +=1

  print a