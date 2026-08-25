from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)

        for s in strs:
            sortedS = tuple(sorted(s))
            temp[sortedS].append(s)
        
        output = []
        
        for value in temp.values():
            output.append(value)

        return(output)