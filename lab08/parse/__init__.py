#Jonathan Ong
#adaptation of provided code
def precedence(oper):
    if oper in ['+', '-']:
        return 1
    else:
        return 2

def operatorp(x):
    return x in ['+', '-', '/', '*', '!'] #added factorial operator '!'

def numberp(x):
    return not operatorp(x)

def parse(expr):
    return parseHelper(expr, [], [])

def parseHelper(expr, operators, operands):
    if expr == [] and operators ==[] and operands == []: #added a check if expr is empty 
        return None
    elif expr == []:
        if operators == []:
            return operands[0]
        else:
            return handleOp([], operators, operands)
    if type(expr[0]) is list: #add a check to see is expr is in parentheses
        return parseHelper(expr[1:], operators, [parseHelper(expr[0],[],[])]+operands )
    elif numberp(expr[0]):
        return parseHelper(expr[1:], operators, [[expr[0], [], []]]+operands)
    elif operators == [] or precedence(expr[0]) > precedence(operators[0]):
        return parseHelper(expr[1:], [expr[0]]+operators, operands)
    else:
        return handleOp(expr, operators, operands)

def handleOp(expr, operators, operands):
    if operators[0] == '!':#added how to handle the factorial operator
        return parseHelper(expr, operators[1:],[[operators[0],operands[0],[]]]+ operands[1:])
    else:
        return parseHelper(expr, operators[1:], [[operators[0], operands[1], operands[0]]]+operands[2:])

#tests 
#x=['3','/','6','-', '9']
#x=['4', '+', '3', '*', '7']
#x=[['4'], '+', ['3'], '+', '6']
#x=[['4', '+', '3'], '*', '7']
#x=['2', '!']
#x=['4', '+', ['3', '!']]
#x=[]
#x=['2']
#print("--", parse(x))
