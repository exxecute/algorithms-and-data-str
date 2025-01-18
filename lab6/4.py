from typing import List

class Solution:
    def combSort(self, arr):
        n = len(arr)
        gap = n  
        shrink = 1.3  
        sorted = False

        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True 

            for i in range(n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted = False  

    def maximumGap(self, nums: List[int]) -> int:
        self.combSort(nums)
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        return max_gap
    
nums = [3,6,9,1]
Solution().countingSort(nums)
print(nums)