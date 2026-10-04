class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        for index in range(len(s)):
            if freq[s[index]] == 1:
                return index
 
        return -1


s_obj = Solution()

s = "loveleetcode"
output_of_it = s_obj.firstUniqChar(s)

print(output_of_it)