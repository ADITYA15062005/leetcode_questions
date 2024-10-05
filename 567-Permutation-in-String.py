class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        len1=len(s1)
        len2=len(s2)
        counts1=[0]*26
        counts2=[0]*26
        for i in range(len1):
            counts1[ord(s1[i])-97]+=1
            counts2[ord(s2[i])-97]+=1
        if counts1 == counts2:
            return True
        for i in range(len1,len2):
            counts2[ord(s2[i])-97]+=1
            counts2[ord(s2[i-len1])-ord('a')]-=1
            if counts1==counts2:
                return True
        return False