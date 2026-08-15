class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        write_p = 0
        for read in range(len(nums)):

            if nums[read] == 0:
                continue
            
            copy_val = nums[read]
            nums[write_p] = copy_val

            if read > write_p:
                nums[read] = 0

            write_p += 1

        print(nums)
        return None


s_obj = Solution()

user_input = [0,1,0,3,12]

output_of_it = s_obj.moveZeroes(user_input)

print(output_of_it)