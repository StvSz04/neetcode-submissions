class Solution:


    def encode(self, strs: List[str]) -> str:
        # I need a delimeter    

        encoded_string = ""

        # Iterate for each string "encode" it and append to current         encoded_string with the delimeter appended to the end

        for s in strs:
            length = len(s)
            encoded_string += (str(length) + "#" +  s)

        # Return encoded string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        len_idx = 0
        res = []

        while len_idx < len(s):
            delim_idx = s.find('#', len_idx)
            length = int(s[len_idx:delim_idx])
            start = delim_idx + 1
            end = start + length
            res.append(s[start:end])
            len_idx = end

        return res
