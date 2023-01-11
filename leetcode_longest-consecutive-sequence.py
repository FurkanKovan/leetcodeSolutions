# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/longest-consecutive-sequence/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def longestConsecutive(self, nums: List[int]) -> int:
        # (1) Convert the nums[] list to a set. This removes any duplicates and since a set is implemented as an hashmap
        # in Python, the operations usually will execute in O(1) time complexity
        numsSet = set(nums)

        # (2) Create a variable to hold the longest consecutive sequence of numbers in nums[], default length is 0
        longestSeq = 0

        # (3) To make a consecutive list with numbers, there should be a starting number (which DOES NOT have any element
        # on its left side, just like on a numbers axis) and the following numbers on its right, where each increases by 1
        # Loop the nums[]
        for n in nums:
            # If the current number DOES NOT have any number on its left in numsSet, it represent a starting of a sequence
            if not (n-1) in numsSet:
                # for that starting number sequence, the length of the sequence is 0 at the beginning
                lengthSeq = 0
                # check if the next consecutive number is in the numsSet, while there is such a number increase the length
                # by 1 (e.g for 2 in nums[], check 2(:number) + 1(:length) i.e 3 in numsSet, check 2+2 i.e 4 , 2+3 i.e 5) 
                while (n+lengthSeq) in numsSet:
                    lengthSeq += 1
                
                # after calculating the sequence for the number n in nums[], update the longestSeq
                longestSeq = max(lengthSeq, longestSeq)
                
        return longestSeq