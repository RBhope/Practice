class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        visit = {}
        def can_reach_from(position):
            if position >= len(nums)-1:
                return True
            if position in visit:
                return visit[position]
            
            max_jump = nums[position]

            for jump in range(1,max_jump+1):
                next_position = position + jump
                if can_reach_from(next_position):
                    visit[position] = True
                    return True  

            visit[position] = False  
            return False
        
        return can_reach_from(0)
