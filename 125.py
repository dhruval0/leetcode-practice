class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        str_length = len(s)
        right_p = str_length - 1

        for left_p in range(str_length):

            if left_p >= right_p:
                break
            
            if not s[left_p].isalnum():
                continue

            if not s[right_p].isalnum():
                while left_p < right_p and not s[right_p].isalnum():
                    right_p -= 1

            if s[right_p].lower() != s[left_p].lower():
                return False

            right_p -= 1

        return True

s_obj = Solution()

user_input = "0P"

output_of_it = s_obj.isPalindrome(user_input)

print(output_of_it)