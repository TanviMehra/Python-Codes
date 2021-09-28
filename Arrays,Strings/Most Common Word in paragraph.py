
paragraph="word,word,word"
banned=["bob", "hit"]

normalized_str =''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
print (normalized_str)
final_str= normalized_str.split()
print (final_str)
my_dict={}
for val in final_str:
    if val not in set(banned):
        if val not in my_dict:
            my_dict[val]=1
        else:
            my_dict[val]+=1
print (my_dict)
print (max(my_dict,key=my_dict.get))




