class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref=[0]*len(nums)
        for i in range(len(nums)):
            ref[i]=[nums[i],i]
        ref.sort()
        i=0
        j=len(nums)-1
        while i < j:
            if ref[i][0]+ref[j][0]>target:
                j-=1
            elif ref[i][0]+ref[j][0]<target:
                i+=1
            else:
                if ref[i][1]>ref[j][1]:
                    return [ref[j][1],ref[i][1]]
                return [ref[i][1],ref[j][1]]

        
        
        