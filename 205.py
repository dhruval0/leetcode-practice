class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mappend_char = {}
        used_char = set()

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):

            s_char = s[i]
            t_char = t[i]

            if s_char in mappend_char:

                if mappend_char.get(s_char) == t_char:
                    continue
                else:
                    return False
            else:

                if t_char in used_char:
                    return False

                mappend_char.update({s_char : t_char})
                used_char.add(t_char)

        return True

s_object = Solution()

s = "paper"
t = "title"
output_of_it = s_object.isIsomorphic(s, t)

print(output_of_it)