class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        k=[]
        area=0
        for i in range(len(heights)):
            while k and heights[i] < heights[k[-1]]:
                p = k.pop()
                height = heights[p]
                if k:
                    width = i - k[-1] - 1
                else:
                    width = i
                area = max(area, height * width)
            k.append(i)
        
        while k:
            p = k.pop()
            height = heights[p]
            if k:
                width = len(heights) - k[-1] - 1
            else:
                width = len(heights)
            area = max(area, height * width)
        
        return area
