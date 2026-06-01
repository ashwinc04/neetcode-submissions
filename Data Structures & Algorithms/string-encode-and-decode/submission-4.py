class Solution:

    def encode(self, strs: List[str]) -> str:
        engoded=""
        for i in strs:
            engoded = engoded+str(len(i))+'#'+str(i)
        return engoded

    def decode(self, s: str) -> List[str]:
        degoded=[]
        i = 0
        k = ""
        while i<len(s):
            if s[i] != "#":
                k = k + s[i]
                i+=1
            else:
                degoded.append(s[i+1: i+1+int(k)])
                i+= 1+int(k)
                k=""
                
        return degoded