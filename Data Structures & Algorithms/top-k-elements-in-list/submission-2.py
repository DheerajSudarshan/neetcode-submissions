class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        
        for i in nums:
            hashmap[i]= 1 + hashmap.get(i,0)

        hashmap =dict(sorted(hashmap.items(), key=lambda item: item[1],reverse = True))
        return list(hashmap.keys())[0:k]