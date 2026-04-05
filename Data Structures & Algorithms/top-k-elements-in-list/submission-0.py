from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key, c in count.items():
            heapq.heappush(heap, (c,key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [key for _,key in heap ]

