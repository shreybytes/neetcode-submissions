class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s="".join(char.lower() for char in s if char.isalnum())
        # rev=s[::-1]
        # if(rev==s):
        #     return True
        # else:
        #     return False
        new_str=""
        for char in s:
            if char.isalnum():
                new_str +=char.lower()
        return new_str==new_str[::-1]