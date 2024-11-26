class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        substringStart = 0
        maxlen = 0
        visited = {}

        for charIndex in range(len(s)):
            if s[charIndex] in visited and visited[s[charIndex]] >= substringStart:
                substringStart = visited[s[charIndex]] + 1
            
            visited[s[charIndex]] = charIndex
            maxlen = max(maxlen, charIndex - substringStart + 1)

        return maxlen

