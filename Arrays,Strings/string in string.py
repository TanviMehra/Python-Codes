def find_shorted_substring(s):
    for i in range(1, len(s) + 1):
        substring = s[:i]
        repeats = len(s) // len(substring)

        if substring * repeats == s:
            return (substring, repeats)

print (find_shorted_substring('bbcdbbcdbbcd'))

def ismultiple(s,t):
    multiple=1
    if s==t:
        return True
    while len(t)*multiple<=len(s):
        multiple+=1
        if t*multiple==s:
            return True

    return False

print (ismultiple('bbcbbcbbc','bbc'))

def find_string(s):
    for i in range(1,len(s)):
        substring = s[:i]
        repeats = len(s)//len(substring)
        if substring * repeats == s:
            return (substring, repeats)
print (find_string('bbcbbcbbc'))
