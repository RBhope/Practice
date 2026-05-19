class Solution:
    def isPalindrome(self, s: str) -> bool:
        combined=""
        for char in s:
            if char.isalnum():
                combined += char.lower()
        if combined == combined[::-1]:
            return True
        else:
            return False
