# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/group-anagrams/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        # My first attempt. Results in O(m*n*logn) time complexity, where
        # m: element number of the strs list (i.e length) , n: average length of a string in strs
        # Each unique string in strs creates a key in result{}, thus making the compare loop time longer

        result = {}
        for an in strs:
            for key in result.keys():
                if sorted(an) == sorted(key):
                    result[key].extend([an])
                    break
            else:
                result[an] = list()
                result[an].extend([an])
        return list(result.values())
        """
        # (1) Create a dictionary that holds list() values
        result = defaultdict(list)

        # (2) For each string element in strs[], map its chars to a list (named count) that shows
        # how many chars it has between 'a-z'
        # Since for this problem the input values (strings in strs[]) constitute of lower case characters (i.e 'a' to 'z')
        for s in strs:
            count = [0] * 26 # there are 26 lower case charachers in English alphabet (a-z)
            # count[] will be used for representing the key in result{} , values in the result{} will be the 's'

            # (3) Map each character of the 's' to count[] and record how many times a character repeats (increment by 1)
            for c in s:
                count[ord(c) - ord("a")] += 1 # to set the first char (i.e 'a') to 0, substract each chars ASCII value
                # which gives us --> 'a' = 0 ; 'b' = 1 ; ... 'z' = 26
            
            # (4) For each 's' in strs[], map the count[] as the key and append the actual string 's' as value
            # Key has to be immutable so it is converted as tuple
            result[tuple(count)].append(s)

        return result.values()