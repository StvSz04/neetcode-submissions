class Solution:
    def rob(self, nums: List[int]) -> int:
        M = [-1] * len(nums)
        B = [-1] * len(nums)
        M[0] = nums[0]
        if len(nums) > 1:
            M[1] = max(nums[0],nums[1])

        for i in range (2,len(nums)):
           M[i] = max(M[i - 2] + nums[i], M[i - 1])

        return(max(M))