class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        num_of_char = len(s)
        zigzag_list = [""] * numRows
        max_down = numRows - 1
        current_row = 0
        
        if numRows == 1 or num_of_char <= numRows:
            return s
    
        for read in range(num_of_char):

            current_ele = s[read]
            zigzag_list[current_row] += current_ele

            if current_row == max_down:
                direction = -1

            elif current_row == 0:
                direction = 1

            current_row += direction

        zigzag_str = ""
        for str_values in zigzag_list:
            zigzag_str += str_values

        return zigzag_str

s_obj = Solution()

numRows = 3
user_input = "PAYPALISHIRING"
output_of_it = s_obj.convert(user_input, numRows)

print(output_of_it)
