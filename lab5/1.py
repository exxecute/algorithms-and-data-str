from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        DIGIT_TO_LETTERS = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        answer = [letter for letter in DIGIT_TO_LETTERS[digits[0]]]
        for digit in digits[1:]:
            new_answer = []
            for letter in answer:
                for new_letter in DIGIT_TO_LETTERS[digit]:
                    new_answer.append(letter + new_letter)
            answer = new_answer
            
        
        return answer