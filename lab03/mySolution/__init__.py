from pythonds.basic import Stack
import math
#Jonathan Ong

def infixToPostfixEval(str): 
    digits = "1234567890"
    priority = {"(":1,"+":2,"-":2,"/":3,"*":3,"!":4}
    evalStack = Stack()
    opStack = Stack()
    postequ = []
    infixExpression = str.split()

    #forms the postfix expression
    for l in infixExpression:
        if l in digits:
            postequ.append(l)
        elif l == '(':
            opStack.push(l)
        elif l == ')':
            op = opStack.pop() 
            while op !=  '(':  
                postequ.append(op)     
                op = opStack.pop()
        else:
            while not opStack.isEmpty() and (priority[opStack.peek()] >= priority[l]):
                op = opStack.pop()
                postequ.append(op)
            opStack.push(l)
        
    while not opStack.isEmpty():
        postequ.append(opStack.pop())
    
    #evalutation of postfix expression
    for l in postequ:
        if l in digits:
            evalStack.push(int(l))
        else:
            if l != '!':
                num1 = evalStack.pop()
                num2 = evalStack.pop()
                evalStack.push(cal(l,num1,num2))
            else:
                evalStack.push(math.factorial(evalStack.pop()))
    
    return evalStack.pop() ," ".join(postequ)

#note cal uses integer division 
def cal(op, n1, n2):
    if op == "*":
        return n1 * n2
    elif op == "/":
        return int(n2 / n1)
    elif op == "+":
        return n1 + n2
    else:
        return n2 - n1

