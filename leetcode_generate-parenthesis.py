# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/generate-parentheses/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def generateParenthesis(self, n: int) -> List[str]:
        # (1) There are three condition to follow:
        # 1- Add open parenthesis if openParenthesisCount < n
        # 2- Add closed parenthesis if closedParenthesisCount < openParenthesisCount
        # 3- The stack elements are valid if the parenthesis count(open & closed) == n

        # Create two stacks, one to create+evaluate a parenthesis order, second to return at the end as a result
        stackPar = []
        result = []

        # (2) To follow each rule and evaluate the parenthesis create a function, which will recursively add parenthesis by
        # following the 1st and 2nd conditions, until the 3rd condition is satisfied (i.e when count reach to n)
        def backtrack(openCount: int, closedCount: int) -> List[str]:
            # Check the 3rd condition(the parenthesis count reach to n)
            # If so append the ordered parenthesis elements in the stackPar[] to result[] AS joined strings
            if openCount == closedCount == n:
                result.append("".join(stackPar))
                return result
            
            # Check the 1st condition. Increment open parenthesis count by 1 each time a '(' added
            # After the propriate closed parenthesis added recursively, that will match the open one, remove the added '('
            if openCount < n:
                stackPar.append('(')
                backtrack(openCount+1, closedCount)
                stackPar.pop()
            
            # Check the 2nd condition. Increment closed parenthesis count by 1 each time a ')' added
            # After the propriate open parenthesis added recursively, that will match the closed one, remove the added ')'
            if closedCount < openCount:
                stackPar.append(')')
                backtrack(openCount, closedCount+1)
                stackPar.pop()
        
        # (3) Call the function with 0 open and 0 closed parenthesis, since they will increment themselves by 1 until
        # each one reach the n (in the correct order)
        backtrack(0,0)
        return result