
def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]==9:
            digits[i]=0
        else:
            digits[i]+=1
            return digits
    return [1]+digits









digits=[0]
print (plusOne(digits))