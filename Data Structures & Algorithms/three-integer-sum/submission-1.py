class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_map = {}
        res = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                if -(nums[i] + nums[j]) in num_map:
                    k = num_map[-(nums[i]+nums[j])]

                    if k != i and k != j:
                        temp = sorted([nums[i],nums[j],nums[k]])
                        if temp not in res:
                            res.append(temp)
                else:
                    if nums[i] not in num_map and nums[j] not in num_map:
                        num_map[nums[i]] = i
                        num_map[nums[j]] = j

        return res