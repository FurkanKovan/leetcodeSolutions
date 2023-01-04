# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/top-k-frequent-elements/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # (1) Create an hashmap to record each number's occurrence in the nums[]
        mapNum = {}
        # (3) To solve this problem a (kind of) reverse Bucket Sort is used
        # Bucket Sort : create another list where the indexes are the values of nums[], and 
        # the values are how many times a number is occured on nums[] (i.e the count of a nums[] value)
        # In this example the Bucket Sort index/values are reversed, so the indexes are the count of a value in nums[]
        # In this way the length of the Bucket Sort list is at most the length of the nums[], because at worst case
        # all of the nubmers are repated only once in nums[]
        # Create the list for reverse Bucket Sort that will be populated by mapNum{} key/values which give the occurences
        # for each value in nums[]
        freqVal = [[] for i in range(len(nums)+1)]

        # (2) Loop on nums[] to populate the mapNum{}, if the number already exists increase the value by 1
        for num in nums:
            mapNum[num] = 1 + mapNum.get(num, 0)
        
        # (4) Loop on mapNum{} and add each (number , occurence count) value to the freqVal[]
        # In this way each index of freqVal signifies the occurence count, and each value(not a int but a list of int)
        # gives the actual numbers in the nums[]
        for key,val in mapNum.items():
            freqVal[val].append(key)
        
        # (5) Finally since the most occurence is wanted the last (or biggest) index of freqVal is needed first
        result = []
        for i in range(len(freqVal)-1, 0, -1): # loop starting from the back
            for n in freqVal[i]: # since the values of freqVal is list(int) loop again
                result.append(n) # append the value to the result
                if len(result) == k: # since k number of values are wanted, stop when reach k
                    return result
                    