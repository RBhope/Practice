class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 step has 1 way, 2 steps have 2 ways
        if n <= 2:
            return n
            
        one_step_back = 2  # Represents ways(2)
        two_steps_back = 1 # Represents ways(1)
        current = 0
        
        # Iteratively calculate ways up to step n
        for i in range(3, n + 1):
            current = one_step_back + two_steps_back
            
            # Shift pointers forward for the next iteration
            two_steps_back = one_step_back
            one_step_back = current
            
        return current
