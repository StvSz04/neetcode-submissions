class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i,num in enumerate(nums):
            res = target - num

            if res in index_map:
                return [index_map[res],i]

            else:
                index_map[num] = i
