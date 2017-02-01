# first non repeating character
# https://leetcode.com/problems/first-unique-character-in-a-string/

# o(2n) solution with o(n) space
def nonRepeating(word):
    ht = {}
    ind = -1
    listOut = []

    for i in word:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] += 1

    for j in word:
        ht[j] -= 1
        if ht[j] == 0:
            return  word.index(j)
        else:
            pass
    return -1

a = "loveleetcode"
b = "leetcode"
print(nonRepeating(a))
print(nonRepeating(b))


