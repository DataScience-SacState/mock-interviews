# first non repeating character
# https://leetcode.com/problems/first-unique-character-in-a-string/

# o(2n) solution with o(n) space
def nonRepeating(word):
    ht = {}
    ind = -1

    for c in word:
        if c not in ht:
            ht[c] = 1
        else:
            ht[c] += 1

    for c in word:
        ht[c] -= 1
        if ht[c] == 0:
            return  word.index(c)
        else:
            pass
    return -1

a = "loveleetcode"
b = "leetcode"
print(nonRepeating(a))
print(nonRepeating(b))


