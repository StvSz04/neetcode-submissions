class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        
        longer = s if len(s) > len(t) else t
        letters = set(longer)


        for letter in s:
            if letter in first:
                first[letter] += 1
            else:
                first[letter] = 0


        for letter in t:
            if letter in second:
                second[letter] += 1
            else:
                second[letter] = 0


        for letter in letters:

            if letter in first and letter in second:

                if first[letter] != second[letter]:
                    return False
            else:
                return False

        return True
        

            