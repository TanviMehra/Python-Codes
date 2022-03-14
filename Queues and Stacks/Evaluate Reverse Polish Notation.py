def evaluateRPN(tokens):
    stack=[]
    symbols=["+","-","*","/"]
    for dig in tokens:
        if dig in symbols:
            dig2=stack.pop()
            dig1=stack.pop()
            if dig=='+':
                evaluated_char= dig1+dig2
            elif dig=='-':
                evaluated_char=dig1-dig2
            elif dig=='*':
                evaluated_char=dig1*dig2
            else:
                evaluated_char=dig1/dig2
            stack.append(int(evaluated_char))


        else:
            stack.append(int(dig))
    return stack[0]


tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print (evaluateRPN(tokens))

