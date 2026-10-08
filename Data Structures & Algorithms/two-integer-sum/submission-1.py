class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range (i):
        #         if(nums[i]+nums[j]==target):
        #             return [j,i]
        dict={}
        for i in range(len(nums)):
            if(target-nums[i] in dict):
                return [dict[target-nums[i]],i]
            else:
                dict[nums[i]]=i


                    


                            