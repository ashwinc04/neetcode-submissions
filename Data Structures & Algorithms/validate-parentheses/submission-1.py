class Solution:
    def isValid(self, s: str) -> bool:
        p={'(':')','{':'}','[':']'}
        k=[]
        for i in s:
            if (not k) or (p.get(i)) :
                k.append(i)
            elif p.get(k[-1]) == i:
                k.pop()
            else:
                return False
        if not k:
            return True
        else:
            return False
