class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        i=0
        while i<len(nums)-2:
            f=i+1
            l=len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            while f<l:
                if(nums[i]+nums[f]+nums[l]==0):
                    res.append([nums[i],nums[f],nums[l]])
                    f+=1
                    l-=1
                    while f < l and nums[f] == nums[f-1]:
                        f+=1
                    while f<l and nums[l] == nums[l+1]:
                        l-=1
                elif(nums[i]+nums[f]+nums[l]>0):
                    l-=1
                else:
                    f+=1
            i+=1
        return res