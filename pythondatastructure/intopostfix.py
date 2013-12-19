from pythonds_basic_stack import Stack

def infix_to_postfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
        token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            while opStack.peek() != "(":
                postfixList.append(opStack.pop())
            opStack.pop()
        elif token in ["*", "/", "+", "-", "^"]:
            while (not opStack.isEmpty()) and \
            (prec[opStack.peek()]) >= (prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

#~ print(infix_to_postfix("A * B + C * D"))
#~ print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
#~ print(infix_to_postfix("( A + B ) * ( C + D )"))
print infix_to_postfix("5 * 3 ^ ( 4 - 2 )")

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
        token in "0123456789":
            operandStack.push(token)
        elif token in ["*", "/", "+", "-"]:
            second = operandStack.pop()
            first = operandStack.pop()
            result = eval(" ".join([first, token, second]))
            operandStack.push(str(result))

    return operandStack.pop()

# print(postfixEval('7 8 + 3 2 + /'))
