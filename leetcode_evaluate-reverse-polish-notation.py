# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def evalRPN(self, tokens: List[str]) -> int:
        # (1) Create stack to do calculations on the tokens
        # To reach the final result a cumulative approach is followed with the operations
        stack = []

        # (2) Loop through the elements in tokens[]
        for token in tokens:
            # (4) When encountered with an operation, do the calculation with the existing numbers in the stack
            # Then append the result to the stack
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                # since the number order is reversed in RPN, the substraction is also reversed
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                # since the number order is reversed in RPN, the division is also reversed
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            # (3) If it is not an operation (i.e a number), add it to the stack
            else:
                stack.append(int(token))
        
        # (5) At the end the final result is calculated in the stack[], and it is the first element
        return stack[0]