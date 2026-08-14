class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        finalCount = 0
        not_allowed = False
        new_list = []

        for word in words:
            new_list.append(set(word))
        
        for new_word in new_list:
    
            for letter in new_word:
                if (letter in allowed):
                    continue
                else:
                    not_allowed = True

            if (not_allowed == False):
                finalCount += 1
            
            not_allowed = False
            count = 0
        
        return finalCount
        


