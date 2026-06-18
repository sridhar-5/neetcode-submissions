class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start, end = 0, len(s) - 1

        while start < end:
            if not (97 <= ord(s[start]) <= 123 or 48 <= ord(s[start]) <= 57):
                start += 1
                continue
            if not (97 <= ord(s[end]) <= 123 or 48 <= ord(s[start]) <= 57):
                end -= 1
                continue
            
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        
        return True
        
        
            