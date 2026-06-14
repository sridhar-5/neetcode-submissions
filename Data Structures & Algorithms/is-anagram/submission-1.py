class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for char in s:
            if char in map_s:
                map_s[char] += 1
            else:
                map_s[char] = 1
        
        for char in t:
            if char in map_t:
                map_t[char] += 1
            else:
                map_t[char] = 1
        
        for key in map_s.keys():
            if (key not in map_t) or (key in map_t and map_s[key] != map_t[key]):
                return False
        
        for key in map_t.keys():
            if (key not in map_s) or (key in map_s and map_t[key] != map_s[key]):
                return False
        
        return True