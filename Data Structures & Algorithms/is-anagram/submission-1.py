from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # freq1=Counter(s)
        # freq2=Counter(t)
        # if (freq1!= freq2):
        #     return False
        # else:
        #     return True
        dict={}
        if(len(s)!=len(t)):
            return False
        
        for char in s:
            if char in dict:
                dict[char]+=1
            else:
                dict[char]=1
        
        for char in t:
            if char in dict:
                dict[char]-=1
            else:
                return False
        for x in dict.values():
            if(x!=0):
                return False
        return True

        
        