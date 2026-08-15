class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        write_p = 0

        for read in range(1, len(nums)):

            if nums[read] == nums[write_p]:
                continue
            else:
                write_p += 1
                nums[write_p] = nums[read]
        
        print(nums)

        return write_p + 1


s_obj = Solution()

user_input = [0,0,1,1,1,2,2,3,3,4]

output_of_it = s_obj.removeDuplicates(user_input)

print(output_of_it)
