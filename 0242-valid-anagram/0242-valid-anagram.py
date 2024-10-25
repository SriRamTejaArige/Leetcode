class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(i for i in s)
        b=list(i for i in t)
        a.sort()
        b.sort()
        # print(a)
        # print(b)
        # if(a==b):
        #     return True
        # else:
        #     return False
        
        return a==b