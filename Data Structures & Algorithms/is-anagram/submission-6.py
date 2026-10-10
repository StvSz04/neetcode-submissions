class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        
        for c in t:
            if c in freq and freq[c] > 0:
                freq[c] -= 1
            else:
                return False

        if sum(list(freq.values())) == 0:
            return True
        else:
            return False

        

            