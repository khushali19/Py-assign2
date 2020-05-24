# W.A.P to do binary search on sorted elements.


def bin(test, item):
    first = 0
    last = len(test)-1
    found = False
    
    while first<=last:
        midpoint = (first+last)//2
        if test[midpoint] == item:
            found = True
        else:
            if item<test[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
        return found

	
test = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(bin(test, 13))
