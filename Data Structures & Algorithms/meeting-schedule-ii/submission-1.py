"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_point, end_point = 0,0
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        current_rooms = 0
        max_rooms = 0

        while start_point < len(intervals):
            if starts[start_point] < ends[end_point]:
                current_rooms+=1
                start_point+=1
            else:
                current_rooms-=1
                end_point+=1
            max_rooms = max(max_rooms, current_rooms)
        return max_rooms

            