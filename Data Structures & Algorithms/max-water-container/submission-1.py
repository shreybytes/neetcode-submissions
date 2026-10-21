class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f=0
        l=len(heights)-1
        max_area=0
        while f<l:
            width=l-f
            height=min(heights[f],heights[l])
            current_area=width*height
            if(current_area>max_area):
                max_area=current_area
            if(heights[f]>heights[l]):
                l-=1
            else:
                f+=1
        return max_area
                 