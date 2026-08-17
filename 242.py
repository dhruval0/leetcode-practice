class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        s_count = {}
        for i in s:
            if i not in s_count:
                s_count[i] = 1
            else:
                s_count[i] += 1

        t_count = {}
        for i in t:
            if i not in t_count:
                t_count[i] = 1
            else:
                t_count[i] += 1

        for character, count in s_count.items():

            if character in t_count:
                t_count_character_count = t_count.get(character)
                if count != t_count_character_count:
                    return False
            else:
                return False

        return True


s_object = Solution()

user_first_input = "rat"
user_second_input = "car"

output_of_it = s_object.isAnagram(user_first_input, user_second_input)

print(output_of_it)