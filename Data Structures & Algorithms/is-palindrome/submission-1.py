class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, second = 0, len(s) - 1
        
        while first < second:
            while first < second and not self.alphaNum(s[first]):
                first += 1
            while first < second and not self.alphaNum(s[second]):
                second -= 1
            if s[first].lower() != s[second].lower():
                return False
            
            first += 1
            second -= 1
        
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) < ord('Z') or
        ord('a') <= ord(c) < ord('z') or
        ord('0') <= ord(c) < ord('9'))