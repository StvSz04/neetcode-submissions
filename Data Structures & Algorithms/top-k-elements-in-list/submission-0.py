class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        result = []
        for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True):
            result.append(key)



        return result[:k]