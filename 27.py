class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        write_p = 0

        for read in range(len(nums)):

            if nums[read] == val:
                continue

            nums[write_p] = nums[read]
            write_p += 1

        print(nums)
        return write_p


s_obj = Solution()

user_input = [0,1,2,2,3,0,4,2]
val = 2

output_of_it = s_obj.removeElement(user_input, val)

print(output_of_it)
