class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]+=1
        sorted_dict = sorted(dict.items(),key=lambda item : item[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_dict[i][0])
        return res
        