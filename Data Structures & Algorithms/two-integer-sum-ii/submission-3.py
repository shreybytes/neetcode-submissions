# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]: #[1,2,3,4]
#         seen = {} 
#         for index, num in enumerate(numbers):
#             complement = target - num
#             # If we already saw the exact number we need, we are done!
#             if complement in seen:
#                 return [seen[complement], index+1]
#             seen[num] = index+1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        l=len(numbers)-1
        while f<l:
            if numbers[f] + numbers[l] == target:
                return [f+1,l+1]
            elif numbers[f] + numbers[l] > target:
                l-=1
            else:
                f+=1