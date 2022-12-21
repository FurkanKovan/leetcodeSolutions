# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/two-sum/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def twoSum(self, nums: List[int], target: int) -> List[int]:
        # (1) Create map to hold the current number and the index of that number
        numsMap = {}

        # (2) Loop on the nums list
        for i, n in enumerate(nums):
            # Instead of searching sum of 2 numbers in list that equals to target,
            # reverse the operation. Check if any number satisfies the difference from the target
            diff = target - n
            if diff in numsMap: # If a difference from the target exists, a sum also exists
                return [numsMap[diff], i]
            numsMap[n] = i # Record the number and it's position
        
        return False