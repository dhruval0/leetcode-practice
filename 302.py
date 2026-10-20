class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:

        return self.prefix[right + 1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(2,5)
print(param_1)


# Go code for this solution
# package main

# import "fmt"

# type NumArray struct {
#     prefix []int
# }

# func Constructor(nums []int) NumArray {
#     prefix := []int{0}

#     for _, num := range nums {
#         prefix = append(prefix, prefix[len(prefix)-1]+num)
#     }

#     return NumArray{prefix: prefix}
# }

# func (this *NumArray) SumRange(left int, right int) int {
#     return this.prefix[right+1] - this.prefix[left]
# }

# func main() {
#     nums := []int{-2, 0, 3, -5, 2, -1}

#     obj := Constructor(nums)

#     fmt.Println(obj.SumRange(0, 2)) // 1
#     fmt.Println(obj.SumRange(2, 5)) // -1
#     fmt.Println(obj.SumRange(0, 5)) // -3
# }
