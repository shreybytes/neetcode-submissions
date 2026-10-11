class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums) #[1,1,1,1,1]
        left_product=1
        right_product=1
        for i in range(len(nums)):
            #get the products on the left side of the index
            res[i]=left_product
            left_product*=nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i]*=right_product
            right_product*=nums[i]

        return res         

            
                
