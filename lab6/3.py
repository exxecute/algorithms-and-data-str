from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorSet = [0, 0, 0]
        for num in nums:
            colorSet[num] += 1
        index = 0
        for i in range(3):
            for j in range(colorSet[i]):
                nums[index] = i
                index += 1
