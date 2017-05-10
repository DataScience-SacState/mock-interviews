# disappearing numbers

def naive(l):
    outl = []
    size = len(l)
    for i in range(1,size):
        if i not in l:
            outl.append(i)
    return outl

l = [4,3,2,7,8,2,3,1]
print(naive(l))

