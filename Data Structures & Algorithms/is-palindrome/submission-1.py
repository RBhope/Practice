class Solution:
    def isPalindrome(self, s: str) -> bool:
        combined=""
        for char in s:
            if char.isalnum():
                combined = (combined+char)
            
        combined = combined.lower()
        rev_comb= combined[::-1]

        if rev_comb == combined:
            return True
        else:
            return False
