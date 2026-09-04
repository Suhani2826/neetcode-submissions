class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        result=[]


        for num in nums:
            d[num]=d.get(num,0)+1
         
        sorted_items=sorted(d.items(),key=lambda x: x[1],reverse=True)
        for item in sorted_items[:k]:
            result.append(item[0])

        return result

        