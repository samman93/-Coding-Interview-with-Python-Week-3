class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ''
        for i in s:
            if i.isalpha():
                l = l + i.lower()
            elif i.isnumeric():
                l = l + i
        
        if l == l[::-1]:
            return True
        return False
        