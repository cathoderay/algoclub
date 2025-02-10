# problem: https://leetcode.com/problems/range-sum-query-immutable/
# space: O(n) | time (initialization): O(n) | time (query): O(1)


class NumArray:
   def __init__(self, nums):
       self.prefix = [nums[0]]
       for i in range(1, len(nums)):
           self.prefix.append(self.prefix[i-1] + nums[i])

   def sumRange(self, left, right):
       return self.prefix[right] - (self.prefix[left-1] if left > 0 else 0)
