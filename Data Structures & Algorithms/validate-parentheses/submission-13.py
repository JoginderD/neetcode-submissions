class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 1:
            return False

        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif s[i] in ")]}" and len(stack) > 0:
                a = s[i]
                if (a == ")" and stack[-1] == "(" or a == "}" and stack[-1] == "{" or a == "]" and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
            else:
                return False

            
        return len(stack) == 0
        