
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for word in strs:
            temp="".join(sorted(word))
            if(temp not in dict):
                dict[temp]=[word]
            else:
                dict[temp].append(word)
        return list(dict.values())
