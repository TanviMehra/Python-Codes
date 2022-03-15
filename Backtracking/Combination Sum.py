def combinationSum(candidates,target):
    def combinationHelper(candidates,target,index=0,curr=[],combinations=[]):
        if target<=0:
            if (target==0):
                combinations.append(curr[:])
            return
        if (index<len(candidates)):
            value=candidates[index]
            curr.append(value)
            combinationHelper(candidates,target-value,index,curr,combinations)
            curr.pop()
            combinationHelper(candidates,target,index+1,curr,combinations)
        return combinations

    return combinationHelper(candidates,target,0,[],[])

candidates=[2,3,5]
target=8

print (combinationSum(candidates,target))
