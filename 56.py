from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)

        answers = []
        if len(intervals) > 0:
            answers.append(intervals[0])

            for i in range(1, len(intervals)):

                if intervals[i][0] > answers[-1][1]:
                    answers.append(intervals[i])

                else:

                    answers[-1][0] = min(answers[-1][0] , intervals[i][0])
                    answers[-1][1] = max(answers[-1][1] , intervals[i][1])

        return answers


s_obj = Solution()

user_input = [[4,7],[1,4]]
output_of_it = s_obj.merge(user_input)

print(output_of_it)