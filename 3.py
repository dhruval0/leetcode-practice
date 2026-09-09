class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # # Here the time comlexity will be o(n2) because of list
        # sub_string = []
        # maximum_sub_string = 0

        # for R in range(len(s)):
            
        #     current_char = s[R]
        #     if current_char not in sub_string:
        #         sub_string.append(current_char)

        #     else:
        #         while current_char in sub_string:
        #             del sub_string[0]
                
        #         sub_string.append(current_char)

        #     maximum_sub_string = max(maximum_sub_string, len(sub_string))

        # return maximum_sub_string

        # # Here the time comlexity will be o(n) because of set
        L = 0
        sub_string = set()
        maximum_sub_string = 0

        for R in range(len(s)):

            current_char = s[R]
            if current_char not in sub_string:
                sub_string.add(current_char)
            
            else:
                while current_char in sub_string:
                    sub_string.remove(s[L])
                    L += 1

                sub_string.add(current_char)
            
            maximum_sub_string = max(maximum_sub_string, len(sub_string))
        
        return maximum_sub_string

s_obj = Solution()

user_input = "abcabcbb"
output_of_it = s_obj.lengthOfLongestSubstring(user_input)

print(output_of_it)