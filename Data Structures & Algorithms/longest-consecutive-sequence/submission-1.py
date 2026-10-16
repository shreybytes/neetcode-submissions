class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set1=set(nums)   #{2,20,4,10,3,5}
        sorted_list=sorted(set1) #{2,3,4,5,10,20}
        current_streak=1
        longest_streak=1
        for i in range (len(sorted_list) -1):
            if(sorted_list[i+1] - sorted_list[i] ==1):
                current_streak+=1
            else:
                longest_streak=max(current_streak,longest_streak)
                current_streak=1

        longest_streak = max(current_streak, longest_streak)
        return longest_streak
                

        