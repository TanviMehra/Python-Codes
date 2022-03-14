def sameDigit(l,r,q):
    count = 0
    for val in range(l,r+1):
        number= q*val
        for char in str(val):
            if char in str(number):
                break
        else:
            count+=1
    return count
print (sameDigit(5,500,2))





def sameDigits(l,r,q):
    count=0
    for i in range(l,r+1):
        prod= i*q
        prod_set=set()
        numb_set= set()
        while prod>0:
            rem= prod%10
            prod_set.add(rem)
            prod=prod//10

        while i > 0:
            rem = i % 10
            numb_set.add(rem)
            i = i // 10
        if not prod_set.intersection(numb_set):
            count+=1
    return count
print (sameDigits(5,500,2))




