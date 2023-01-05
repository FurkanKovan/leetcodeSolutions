# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/product-of-array-except-self/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def productExceptSelf(self, nums: List[int]) -> List[int]:
        # (1) Create a result array which will hold the product values on each index
        # Default value is taken 1 since multiplying by 1 does not change anything
        result = [1] * len(nums)

        # (2) On this solution approach pre/postfix approach used but the values are assign to the result array directly.
        # Instead of creating these arrays, only one result[] array is used to satisfy O(1) space complexity. All of the
        # calculations are made on this result[] array instead of separately taking values from pre/postfix arrays.
        # Start from the beginning of nums[], for each number record the product value of all the preceding numbers on the
        # current number's index. For the first index(0th) since there is no preceding number, assume there is '1',
        # because it does not effect the product operation.
        # Then, do the same thing in reverse on nums[]. Assume there is a '1' again for the last value.
        # Record the product values to the same array that used before (i.e to the result[]).
        prefix = 1

        # (3) For each number in nums[], add the product value to the result[]
        # Then multiply the current value with the preceding product value of all the numbers until that point, and
        # assign it to the appropriate index of result[] (appropriate index = basically the very next value's index)
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # (4) Since, prefix products are calculated above and held it on the result[],
        # do the same calculations for the postfix but in reverse order
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix # insted of '=', '*=' is used otherwise it overrites on the prefix values on result[]
            postfix *= nums[i]
        
        return result
