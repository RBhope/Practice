class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for char in s:
            if char.isalnum():
                tmp += char.lower()

        rev_str = tmp[::-1]

        return rev_str == tmp