from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create hash map to store freq for each unique num
        # Key = num and value = freq
        freq = defaultdict(int)

        # Iterate through the array and incremeant the freq for each num
        for num in nums:
            freq[num] += 1

        # Return the k largets freqs
        # Sort -> slice the list
        sorted_freq = list(freq.items())
        sorted_freq.sort(key = lambda x : x[1], reverse=True)
        res = [x[0] for x in sorted_freq[:k]]
        return res