def stringCompression(s):
    i=0
    out=[]
    count=1
    if len(s)==1:
        return s
    while i<len(s):
        if i<len(s)-1 and s[i]!=s[i+1]:
            out.append(s[i])
            i=i+1
        else:
            while i<len(s)-1 and s[i]==s[i+1]:
                count+=1
                char=s[i]
                i=i+1
            i=i+1
            out.append(char+str(count))
            count=1
    return (''.join(out))

def compress(chars) -> int:
    i=0
    j=0
    out=[]
    while i<len(chars):
        while j<len(chars) and chars[i]==chars[j]:
            j=j+1
        out.append(chars[i])
        if j-i>1:
            out.append(str(j-i))
        i=j
    return ''.join(out)


print (compress('abbccccccccccccccccccc'))

