class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        stripe = 0
        
        if grid == [[]] or grid == []:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        stripe += 1
                    if i == len(grid)-1 or grid[i+1][j] == 0:
                        stripe += 1
                    if j == 0 or grid[i][j-1] == 0:
                        stripe += 1
                    if j == len(grid[i])-1 or grid[i][j+1] == 0:
                        stripe += 1
        return stripe
        
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        stripe = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    stripe += 4
                    if i != 0 and grid[i-1][j] == 1:
                        stripe -= 1
                    if i != len(grid)-1 and grid[i+1][j] == 1:
                        stripe -= 1
                    if j != 0  and grid[i][j-1] == 1:
                        stripe -= 1
                    if j != len(grid[i])-1 and grid[i][j+1] == 1:
                        stripe -= 1
        return stripe
        
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        stripe = 0
        
        for i in range(len(grid)):
            if grid[i] == [0]*len(grid[i]):
                continue
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    stripe += 4
                    if i != 0 and grid[i-1][j] == 1:
                        stripe -= 1
                    if i != len(grid)-1 and grid[i+1][j] == 1:
                        stripe -= 1
                    if j != 0  and grid[i][j-1] == 1:
                        stripe -= 1
                    if j != len(grid[i])-1 and grid[i][j+1] == 1:
                        stripe -= 1
        return stripe
