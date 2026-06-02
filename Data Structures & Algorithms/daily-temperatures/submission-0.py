class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        p= [0] * n
        k= []
        for i in range(n):
            while k and temperatures[i] > temperatures[k[-1]]:
                p[k[-1]] = i - k[-1]
                k.pop()
            k.append(i)
        return p