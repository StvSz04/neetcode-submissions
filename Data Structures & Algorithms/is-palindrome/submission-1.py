class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        alpha = {x for x in range(ord('a'), ord('z') - 1)}
        numeric = {str(x) for x in range(0,10)}

        for c in s:
            if ord(c.lower()) not in alpha and c not in numeric:
                s = s.replace(c,"")

        i = 0
        j = len(s) - 1
        while j >= i:
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
            else:
                return False

        return True
        