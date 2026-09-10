from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        # 1. Always sort intervals by their start times first
        intervals.sort(key=lambda x: x[0])
        
        # Initialize your results array with the very first interval
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # Look at the last interval we successfully added to our results
            last_added_start = res[-1][0]
            last_added_end = res[-1][1]
            
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            
            # Your exact logic check: Do they overlap?
            if current_start <= last_added_end:
                # Merge them by expanding the end time of the last added interval
                res[-1][1] = max(last_added_end, current_end)
            else:
                # No overlap, so safely append the current interval as a new entry
                res.append(intervals[i])
                
        return res
