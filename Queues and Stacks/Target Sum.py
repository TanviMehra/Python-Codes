class Solution:
    count=0
    def findTargetSumWays(self,nums, S):
        count=0
        def targetHelper(nums,target,i,current_sum):
            if i==len(nums):
                if current_sum==target:
                    self.count+=1
            else:

                targetHelper(nums,target,i+1,current_sum+nums[i])
                targetHelper(nums,target,i+1,current_sum-nums[i])

        targetHelper(nums,S,0,0)
        return self.count


    def findTargetSumWays1(self,nums, S):
        def helper(nums, idx, part_sum):
            if idx == len(nums):
                return 1 if part_sum == S else 0
            else:
                return helper(nums, idx + 1, part_sum + nums[idx]) + helper(nums, idx + 1, part_sum - nums[idx])

        return helper(nums, 0, 0)


obj= Solution()
nums=[1,1,1,1,1]
S=3
print (obj.findTargetSumWays2(nums,S))