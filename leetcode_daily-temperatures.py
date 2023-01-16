# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/daily-temperatures/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # (1) Create an answer(or output) list that is going to give the desired distance for the temperatures
        # The answer[] is populated with 0s because if for a temperature there is no greater one in the list, default
        # value(i.e days) is going to be 0(i.e no days exist with a greater temperature)
        answer = [0] * len(temperatures)
        # The stack[] is going to hold the temperatures in the temperatures[] to compare the values, AND it is going to
        # hold the indexes to record to answer[] how many days passed
        stack = [] # [temperature, index]

        # (2) Loop through temperatures[]
        for i, t in enumerate(temperatures):
            # While the stack is not empty AND the current temperature t is greater than the top value of the stack
            while stack and t > stack[-1][0]:
                # Since there is no greater temperature that encountered in stack[], pop() the top value (which has a less
                # temperature value than t)
                stackTemp, stackIndex = stack.pop()
                # Find the number of days that it took until coming to this temperature in stack[], and record it to
                # corresponding index at the answer[]
                answer[stackIndex] = (i - stackIndex)

            # If the stack is empty append the current temperature and its index
            stack.append([t,i])

        return answer
