# single number
# https://leetcode.com/problems/single-number/

# linear and no extra space
def findDuplicateXOR(numbersList):
    result = numbersList[0]
    for i in numbersList[1:]:
        result ^= i
    return result

# linear, but o(n) space
def findDuplicateHT(numbersList):
    ht = {}
    sumv = 0
    for i in numbersList:
        if i not in ht:
            ht[i] = 1
            sumv += i
        else:
            ht[i] -= 1
            sumv -= i
    return sumv

l = [2,3,2,5,5,3,4]
print(findDuplicateXOR(l))

