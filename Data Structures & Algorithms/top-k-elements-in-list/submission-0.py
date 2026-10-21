from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_counts = Counter(nums)
        common = int_counts.most_common(k)
        return [num for num, count in common]
