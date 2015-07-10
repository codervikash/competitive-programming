# Game of Thrones - I

# Dothraki are planning an attack to usurp King Robert from his kingdom. King Robert learns of this conspiracy from Raven and plans to lock the single door through which an enemy can enter his kingdom.

# But, to lock the door he needs a key that is an anagram of a certain palindrome string.

# The king has a string composed of lowercase English letters. Help him figure out if any anagram of the string can be a palindrome or not.

string = raw_input()

found = False
x = 0
y = 0
comp = set(string)
comp = list(comp)
for i in range(len(comp)):
    for j in range(len(string)):
        if comp[i] == string[j]:
            x += 1
            j += 1
        else:
            j += 1
    if x % 2 == 0:
        pass
    else:
        y += 1
    i += 1
    x = 0
    j = 0
if len(string) % 2 == 0:
    if y == 0:
        found = True
    else:
        found = False
else:
    if y == 1:
        found = True
    else:
        found = False

if not found:
    print("NO")
else:
    print("YES")

# much efficient alternatives:
# 1st

st = raw_input()
arr = [0] * 27
for i in range(len(st)):
    cnt = ord(st[i]) - ord('a')
    arr[cnt] += 1
co = 0
ce = 0
for i in range(26):
    if arr[i] % 2 == 0:
        ce += 1
    else:
        co += 1
if co > 1:
    print ("NO")
else:
    print ("YES")

# 2nd

s = raw_input()
cnt = {}
for c in s:
    cnt[c] = cnt.get(c, 0) + 1
nodd = len(filter(lambda x: x % 2 == 1, cnt.values()))
print (["NO", "YES"][nodd <= 1])
