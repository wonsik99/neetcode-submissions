class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s, list_t = [], []

        for i in range(len(s)):
            list_s.append(s[i])

        for i in range(len(t)):
            list_t.append(t[i])
        
        list_s.sort()
        list_t.sort()

        if list_s == list_t:
            return True
        return False
        