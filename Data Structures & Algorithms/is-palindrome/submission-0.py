class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for i in s:
            if i.isalnum():
                new+=i
        print(new)
        i=0
        j=len(new)-1
        while i < j:
            if new[i].lower()!=new[j].lower():
                return False
            i+=1
            j-=1
        return True
        