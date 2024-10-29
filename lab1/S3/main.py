class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character == "(" or character == "[" or character == "{":
                stack.append(character)
            elif character == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif character == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif character == "}" and stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return len(stack) == 0
