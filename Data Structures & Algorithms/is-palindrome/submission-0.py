class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(char.lower() for char in s if char.isalnum())
        rev=s[::-1]
        if(rev==s):
            return True
        else:
            return False
        