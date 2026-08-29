class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # append and pop

        for b in s:
            if b not in {"}","]",")"}:
                stack.append(b)
            else:
                if len(stack) >= 1:
                    top = stack.pop()
                else:
                    return False

                if b == "}" and top == "{":
                    continue
                elif b == "]" and top == "[":
                    continue
                elif b == ")" and top == "(":
                    continue
                else:
                    return False

        if len(stack) >= 1:
            return False

        return True
        