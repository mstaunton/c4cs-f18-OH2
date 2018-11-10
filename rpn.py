#!/usr/bin/env python3

import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '//': operator.floordiv,
    '!': operator.mul,
}

def stack_operation(stack, function, token):
    if (token == '!'):
        base = stack.pop()
        if(base < 1):
            stack.append("Error: Factorial only on positive numbers")
            return stack
        stack.append(1)
        for x in range(base, 0, -1):
            fact = stack.pop()
            result = function(fact, x)
            stack.append(result)
        return stack
    arg2 = stack.pop()
    if (token == '/' or token == '//'):
        if(arg2 == 0):
            stack.pop() # pop stack to return it to state before operation called
            stack.append("Error: Cannot divide by Zero, Try again")
            return stack
    arg1 = stack.pop()
    result = function(arg1, arg2)
    stack.append(result)
    return stack

def calculate(myarg):
    stack = list()
    input_line = myarg.split()
    for x in range(0, len(input_line)):
        try:
            token = input_line[x]
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            stack = stack_operation(stack, function, token)
            if len(stack) != 1:
                if x == len(input_line) - 1:
                    raise TypeError("Too many parameters")
                else:
                    if input_line[x+1] == '!':
                        while(len(stack) != 1):
                            stack = stack_operation(stack, function, token)
                        return stack.pop()
                    else:
                        raise TypeError("Invalid Token")  
        print(stack)

    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
