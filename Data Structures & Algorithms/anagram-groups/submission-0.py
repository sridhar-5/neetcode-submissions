class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # counts tuple => [] list of anagrams

        for string in strs:
            count = [0] * 26
            for i in string:
                count[ord(i) - ord("a")] += 1

            anagrams[tuple(count)].append(string)
        
        return list(anagrams.values())