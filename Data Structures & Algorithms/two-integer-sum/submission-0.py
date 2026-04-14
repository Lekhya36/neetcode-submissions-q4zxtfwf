class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}   # dictionary to store number -> index

        for i in range(len(nums)):
            need = target - nums[i]
            if need in mp:
                return [mp[need], i]
            mp[nums[i]] = i
        