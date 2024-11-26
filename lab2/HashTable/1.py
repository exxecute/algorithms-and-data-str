class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        listSize = len(nums)

        for i in range(listSize):
            numMap[nums[i]] = i

        for i in range(listSize):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  