# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/valid-parentheses/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def isValid(self, s: str) -> bool:
        # (1) Create a stack[] that will hold the parentheses to compare while looping the list
        # and create a hashmap to check if any closing parentheses match with the appropriate one
        # Here, checking with closing parentheses is better since every closing parentheses should match an openning one
        # The stack will only hold the openning parentheses, every closing parentheses encountered is checked with an
        # openning one in stack[], if they match as closing-openning (checked via bracketsMap{}) delete them from the stack
        stack = []
        bracketsMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        # (2) Create a loop to check the each character in s[]
        # As looping through the list when arrived at a closing paranthesis, check the closest matching openning
        # parentheses in stack[], note that only openning paranthesis are added to stack[]
        for c in s:
            if c in bracketsMap: # keys of bracketsMap{} are closing parentheses, so check if c is a closing one
                # If stack[] is empty there are no openning parentheses encountered, so no need to check
                # If last added parentheses to the stack, matches as closing-openning with c, means a pair is found,
                # delete the openning one from the stack[] since a match is found
                if stack and stack[-1] == bracketsMap[c]:
                    stack.pop()
                else:
                    return False # No openning parentheses or closing-openning does not match
            else:
                # If c is not a closing parentheses key in bracketsMap{}, it is a openning one. Add to the stack[]
                stack.append(c)

        # If stack[] is empty after looping in s[], every openning parentheses matched with a closing one -> return True
        return True if not stack else False