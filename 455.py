class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:

        g_pointer = 0
        s_pointer = 0
        count = 0

        if s and g:
            g = sorted(g)
            s = sorted(s)
            while g_pointer < len(g) and s_pointer < len(s):

                if s[s_pointer] >= g[g_pointer]:

                    s_pointer += 1
                    g_pointer += 1
                    count +=1

                elif s[s_pointer] < g[g_pointer]:

                    s_pointer += 1

        return count


s_obj = Solution()

g = [1,2,3]
s = [1,1]
output_of_it = s_obj.findContentChildren(g, s)

print(output_of_it)