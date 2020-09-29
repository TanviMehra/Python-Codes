# logic - you buy if the next day price is higher thann the day you are on
def maxProfit(nums):
    profit=0
    if len(nums)==0:
        return 0
    for i in range(1,len(nums)):
        if nums[i-1]<nums[i]:
            profit+= nums[i]-nums[i-1]
    return profit





nums= list(map(int,input().split()))
print (maxProfit(nums))

'''max_profit=0
        if len(prices)==0:
            return 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                max_profit+=(prices[i+1]-prices[i])
        return (max_profit)

'''