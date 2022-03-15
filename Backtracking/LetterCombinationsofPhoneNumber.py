import itertools
letter_dict= {'2':'abc','3':'def','4':'ghi','5':'jkl',
              '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}


tokens=[]
new_list=[]
num=input()
for val in num:
    tokens.append(letter_dict[val])
my_list=list(itertools.product(*tokens))
for val in my_list:
    new_val=''.join(val)
    new_list.append(new_val)
print (new_list)

