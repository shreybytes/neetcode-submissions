class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for num in nums:
            if num not in freq_map:
                freq_map[num]=1
            else:
                freq_map[num]+=1
        sorted_dict = sorted(freq_map.items(),key=lambda item : item[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_dict[i][0])
        return res
        