# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/contains-duplicate/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def containsDuplicate(self, nums: List[int]) -> bool:
        # (1) Create hashset to hold numbers in array while looping
        # Hashset add/delete/search operations are in O(1) time, so overall time complexity is O(n)
        setNums = set()
        for num in nums:
            if num in setNums: # If already in the hashset it is a duplicate
                return True
            setNums.add(num) # If it is not a duplicate add to the list
        
        return False # No duplicates so return False