# Intersection of two arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

'''
@param list a
@param list b
@return list result
'''
def intersect(a, b):
    outList = []
    ht = {}

    for i in a:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] += 1

    for i in b:
        if ht[i] >= 1:
            if i not in outList:
                outList.append(i)

    return outList

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersect(nums1,nums2))
