# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/valid-anagram/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def isAnagram(self, s: str, t: bool) -> bool:
        # (1) First condition of anagram is to be at the same length
        # If they are not at the same length, return false
        if len(s) != len(t):
            return False
        
        # (2) Create two hasmaps to hold the elements of the strings
        mapS, mapT = {}, {}

        # (3) To add the elements, loop at the range of the length of s or t (at this point the lengths should be same)
        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0) # add each element to the hashmap 
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
            # The get() method is used instead of '1 + mapS[s[i]]' because if the element not exists in the hashmap yet,
            # python throws an error. get() has default value for this which is the seceond parameter ('0' in this case)

        # (3) After mapping each element, compare the hashmaps
        # If any not matching key-value found return False
        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False
        
        return True