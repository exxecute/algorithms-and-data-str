from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
    
        q = deque()
        q.append((startGene, 0))
        while q:
            print(q)
            tochk, limit = q.popleft()
            if tochk == endGene:
                return limit
            
            bankIndex = 0
            while bankIndex < len(bank):
                word = bank[bankIndex]
                
                differencies = 0
                for i in range(8):
                    if tochk[i] != word[i]:
                        differencies += 1
                
                if differencies == 1:
                    q.append((word, limit+1))
                    bank.remove(word)
                    continue   
                bankIndex += 1
        
        return -1
    
# startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])