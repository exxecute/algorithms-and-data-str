class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        stringLen = len(s)
        LENGTH = 10

        if stringLen <= LENGTH:
            return []
        
        d = dict()
        for i in range(stringLen-(LENGTH-1)):
            key = s[i:i+LENGTH]
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
        
        return [key for key in d.keys() if d[key] > 1]