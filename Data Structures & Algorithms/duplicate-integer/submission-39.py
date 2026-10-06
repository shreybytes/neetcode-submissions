class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set1=set()
        # for i in nums:
        #     if(i in set1):
        #         return True
        #     else:
        #         set1.add(i)
        # return False
       set1=set(nums)
       if(len(set1)!= len(nums)):
        return True
       else:
        return False
