from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            
            freq = {}
            for char in word:

                if char not in freq:
                    freq.update({char : 1})
                else:
                    freq[char] += 1
            
            signature = frozenset(freq.items())

            if signature not in groups:
                groups[signature] = [word]
            else:
                groups[signature].append(word)

        
        return list(groups.values())


s_obj = Solution()

user_input = ["eat","tea","tan","ate","nat","bat"]
output_of_it = s_obj.groupAnagrams(user_input)

print(output_of_it)