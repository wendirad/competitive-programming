class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = float('-inf')
        stack = []

        n = len(heights)
        
        stack.append((heights[0], 0))
        
        for i in range(n):
            if len(stack) == 0:
                stack.append((heights[0], 0))
            elif heights[i] >= stack[-1][0]:
                stack.append((heights[i], i))
            else:
                while stack and heights[i] < stack[-1][0]:
                    h, w = stack.pop()
                    area = h * (i - w)
                    max_area = max(max_area, area)
                stack.append((heights[i], w))

        while len(stack) != 0:
            h, w = stack.pop()
            area = h * (n - w)
            max_area = max(max_area, area)
        
        return max_area