# max consecutive ones
# https://leetcode.com/problems/max-consecutive-ones/

def maxConsec(l):
    sumr = 0
    maxn = 0
    for i in l:
        if (i != 0):
            sumr += 1
            maxn = sumr
        else:
            sumr = 0
    return maxn

l = [1,1,0,1,1,1]

print(maxConsec(l))
