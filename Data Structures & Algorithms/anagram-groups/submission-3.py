class Solution:

    def ref_arr(self,s):
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        return dic
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref=[]
        for i in range(len(strs)):
            ref.append([strs[i],False])
        i=0
        j=1
        res=[strs[0]]
        ans=[]
        n=len(strs)
        while i < n-1:
            if ref[i][1]==True:
                i+=1
                j=i+1
                res=[]
                res.append(strs[i])
                continue
            if ref[j][1]==False and self.ref_arr(strs[i])==self.ref_arr(strs[j]):
                res.append(strs[j])
                ref[j][1]=True
            if j==n-1:
                i+=1
                j=i+1
                ans.append(res)
                res=[]
                res.append(strs[i])
                continue
            j+=1
        if ref[-1][1]==False:
            ans.append([ref[-1][0]])
        return ans
            

                
            


        