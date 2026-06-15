import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for number in nums:
            counts[number] = 1 + counts.get(number, 0)
        
        heap = []
        for key in counts.keys():
            heapq.heappush_max(heap, (counts[key], key))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop_max(heap)[1])
        
        return result