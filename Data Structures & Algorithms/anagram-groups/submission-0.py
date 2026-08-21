from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            s_s = ''.join(sorted(s))
            map[s_s].append(s)
        
        return  list(map.values())