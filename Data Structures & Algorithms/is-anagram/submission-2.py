class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s  = sorted(s)
        sort_t = sorted(t)

        i = 0
        while(i < len(s) and i < len(t)):
            if(sort_s[i] == sort_t[i]):
                i += 1
                continue
            else:
                return False
            
        if i == len(s) and i == len(t):
            return True
        else:
            return False
        