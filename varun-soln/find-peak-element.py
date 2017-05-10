# find peak element
# https://leetcode.com/problems/find-peak-element/

def findPeakElement(nums):
    print(len(nums))
    for i in range(1,len(nums)-1):
        print nums[i], nums[i+1], nums [i-1]
        if nums[i+1] < nums[i] and nums[i-1] < nums[i]:
            return i

    return -1

def findPeakElementB(nums):
    first = 0
    last = len(nums)
    el = -1

    while first <= last:
        mid = (first + last)/2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        else:

l = [1, 2, 4, 3, 5, 4, 2]
print(findPeakElementB(l))

