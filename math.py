#Angela Yu
#SoftDev2 pd8
#HW11 -- Ready, Set, Math!
#2017-04-24

def union(a,b):
    set=a
    set.extend([x for x in b if not(x in a)])
    return set

def intersection(a,b):
    return [x for x in a if x in b]

#things in a thats not in b
def setDiff(a,b):
    return [x for x in a if not(x in b)]

def symDiff(a,b):
    set=setDiff(a,b)
    set.extend([x for x in b if not(x in a)])
    return set

def carte(a,b):
    return [(x,y) for x in a for y in b]

print union([1,2,3],[2,3,4])
print intersection([1,2,3],[2,3,4])
print setDiff([1,2,3],[2,3,4])
print setDiff([2,3,4],[1,2,3])
print symDiff([1,2,3],[2,3,4])
print carte([1,2],["red", "white"])
