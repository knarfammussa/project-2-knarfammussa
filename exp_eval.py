from stack_array1 import Stack


# You should not change this Exception class!
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str: str) -> float:
    input_list = list(input_str.strip().split())
    capacity = len(input_list)
    stack = Stack(capacity)
    op = ["+", "-", "*", "/", "**", "<<", ">>"]
    if capacity == 0:
        raise PostfixFormatException("Insufficient operands")
    for i in input_list:
        if i in op:
            if stack.size() < 2:
                raise PostfixFormatException("Insufficient operands")
            last = stack.pop()
            second_last = stack.pop()
            if i == "+":
                result = last + second_last
            elif i == "-":
                result = second_last - last
            elif i == "*":
                result = second_last * last
            elif i == "/":
                if last == 0:
                    raise ValueError
                result = second_last / last
            elif i == "**":
                result = second_last ** last
            elif i == "<<":
                result = second_last << last
            elif i == ">>":
                result = second_last >> last
            stack.push(result)
        else:
            try:
                stack.push(int(i))
            except ValueError:
                try:
                    stack.push(float(i))
                except ValueError:
                    raise PostfixFormatException("Invalid token")
    if stack.size() != 1:
        raise PostfixFormatException("Too many operands")
    return stack.pop()
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""


def infix_to_postfix(input_str: str) -> str:
    input_list = list(input_str.strip().split())
    capacity = len(input_list)
    stack = Stack(capacity)
    op = ["+", "-", "*", "/", "**", "<<", ">>"]
    postfix = ""
    for i in input_list:
        if i == "(":
            stack.push(i)
        elif i == ")":
            pop = stack.pop()
            while not stack.is_empty() and pop != ")" and pop != "(":
                postfix = postfix + " " + pop
                pop = stack.pop()
        elif i in op:
            op1 = i
            if stack.size() == 0:
                stack.push(op1)
            else:
                precedence = {}
                precedence["+"] = 1
                precedence["-"] = 1
                precedence["*"] = 2
                precedence["/"] = 2
                precedence["**"] = 3
                precedence[">>"] = 4
                precedence["<<"] = 4
                while not stack.is_empty() and stack.peek() in precedence and (
                        op1 != "**" and precedence[op1] <= precedence[stack.peek()]):
                    postfix = postfix + " " + stack.peek()
                    stack.pop()
                while not stack.is_empty() and stack.peek() in precedence and (
                        op1 == "**" and precedence[op1] < precedence[stack.peek()]):
                    postfix = postfix + " " + stack.peek()
                    stack.pop()
                stack.push(op1)
        else:
            postfix = postfix + " " + i
    while stack.size() > 0:
        postfix = postfix + " " + stack.pop()
    return postfix.strip()
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression x """


def prefix_to_postfix(input_str: str) -> str:
    input_list = list(input_str.strip().split())
    capacity = len(input_list)
    stack = Stack(capacity)
    op = ["+", "-", "*", "/", "**", "<<", ">>"]
    for i in range(capacity - 1, -1, -1):
        if input_list[i] in op:
            op1 = stack.pop()
            op2 = stack.pop()
            str1 = op1 + " " + op2 + " " + input_list[i]
            stack.push(str1)
        else:
            stack.push(input_list[i])
    postfix = stack.pop().strip()
    return postfix
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
