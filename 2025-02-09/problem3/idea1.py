# problem: https://leetcode.com/problems/range-sum-query-mutable/
# space: O(n) | time (initialization): O(n) | time (update): O(log(n)) | time (queries): O(log(n))


from dataclasses import dataclass


@dataclass
class STNode:
    a : int
    b : int
    summa : int = 0
    left : int = None
    right : int = None


class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.__build(STNode(a=0, b=len(nums)-1))
 
    def __build(self, node):
        if node.a == node.b:
            node.summa = self.nums[node.a]
            return node

        mid = (node.a + node.b) // 2
        node.left = self.__build(STNode(a=node.a, b=mid))
        node.right = self.__build(STNode(a=mid + 1, b=node.b))
        node.summa = node.left.summa + node.right.summa

        return node

    def update(self, index: int, val: int) -> None:
        self.__update(self.root, index, val)
 
    def __update(self, node, index, val):
        if node.a == node.b:
            node.summa = self.nums[index] = val
            return
 
        mid = (node.a + node.b) // 2
        self.__update(node.left if index <= mid else node.right, index, val)
        node.summa = node.left.summa + node.right.summa

    def sumRange(self, left: int, right: int) -> int:
        return self.__sum_range(self.root, left, right)

    def __sum_range(self, node, left, right):
        if right < node.a or left > node.b: return 0
        if left <= node.a and node.b <= right: return node.summa

        x = self.__sum_range(node.left, left, right)
        y = self.__sum_range(node.right, left, right)
        return x + y
