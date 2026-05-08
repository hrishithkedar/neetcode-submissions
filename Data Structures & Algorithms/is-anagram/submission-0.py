class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        reg1={}
        reg2={}
        l1=len(s)
        l2=len(t)
        if l1!=l2:
            return False
        for i in range(l1):
            if s[i] not in reg1:
                reg1[s[i]]=1
            else:
                reg1[s[i]]+=1
        for i in range(l2):
            if t[i] not in reg2:
                reg2[t[i]]=1
            else:
                reg2[t[i]]+=1
        return reg1==reg2
        