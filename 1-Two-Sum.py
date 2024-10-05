class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in map1:
                return[map1[diff],i]
            map1[n]=i
        return 