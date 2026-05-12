class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] not in ref:
                ref[nums[i]]=1
            else:
                ref[nums[i]]+=1
        sor_ref=dict(sorted(ref.items(),key=lambda item:item[1], reverse=True))
        for i in sor_ref:
            if len(ans)==k:
                break
            else:
                ans.append(i)
        return ans

        