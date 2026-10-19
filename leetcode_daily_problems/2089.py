class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        array = nums.sort()
        output = []
        for i in range (len(nums)):
            if nums[i] == target:
                output.append(i)
                
        return output