class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        result = [[1]]
        if numRows == 1:
            return result

        while len(result) < numRows:

            prev = result[-1]
            current = [1]

            for i in range(len(prev) - 1):
                current.append(prev[i] + prev[i + 1])

            current.append(1)

            result.append(current)

        return result


s_obj = Solution()

numRows = 5

output_of_it = s_obj.generate(numRows)

print(output_of_it)


# go code
# func generate(numRows int) [][]int {
#     if numRows == 0 {
#         return [][]int{}
#     }

#     result := [][]int{{1}}

#     for len(result) < numRows {
#         prev := result[len(result)-1]
#         current := []int{1}

#         for i := 0; i < len(prev)-1; i++ {
#             current = append(current, prev[i]+prev[i+1])
#         }

#         current = append(current, 1)
#         result = append(result, current)
#     }

#     return result
# }