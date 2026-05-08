class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        reg={}
        for i in range(len(nums)):
            if nums[i] not in reg:
                reg[nums[i]]=1
            else:
                reg[nums[i]]+=1
                return True
        return False
        

        