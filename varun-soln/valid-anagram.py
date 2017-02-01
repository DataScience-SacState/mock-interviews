# valid anagram
# https://leetcode.com/problems/valid-anagram/

def validAnagram(s, t):
    ht = {}

    for i in s:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] += 1

    ret = 0
    for i in t:
        if i not in ht:
            ret = -1

    if ret == -1:
        return False
    else:
        return True

s = "anagram"
t = "nagaram"

c = "cat"
r = "rat"

print(validAnagram(s,t))
print(validAnagram(c,r))
