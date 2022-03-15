

def permute(nums):
    answer=[]
    def backtrack(options,current,answer):
        if len(options)==0:
            answer.append(current[:])
            return
        else:
            for i,num in enumerate(options):
                current.append(num)
                print (current)
                backtrack(options[:i]+options[i+1:],current,answer)
                current.pop()
    backtrack(nums,[],answer)
    return answer


nums=[1,2,3]
print(permute(nums))