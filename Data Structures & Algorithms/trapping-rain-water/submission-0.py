class Solution:
    def trap(self, height: List[int]) -> int:
        f = 0
        l = len(height) - 1
        total_water = 0
        max_left = max_right = 0
        
        while f < l:
            # Always process the side with the shorter current wall
            if height[f] < height[l]:
                # Update the running left peak
                max_left = max(max_left, height[f])
                # Water trapped is the peak height minus the current block height
                total_water += max_left - height[f]
                f += 1
            else:
                # Update the running right peak
                max_right = max(max_right, height[l])
                # Water trapped is the peak height minus the current block height
                total_water += max_right - height[l]
                l -= 1
                
        return total_water
