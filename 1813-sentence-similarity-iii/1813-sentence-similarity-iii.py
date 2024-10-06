class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        list1 = sentence1.split(' ')
        list2 = sentence2.split(' ')
        if len(list1) > len(list2):
            return self.areSentencesSimilar(sentence2, sentence1)
        
        
        left = 0
        right = 1
        while left <= len(list1) - right:
            if list1[left] == list2[left]:
                left += 1
            elif list1[-right] == list2[-right]:
                right += 1
            else:
                break
                
        return left + right == len(list1) + 1