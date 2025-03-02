from typing import List


def dfs(self, x: int, y: int, triangle: List[List[int]], saves: List[List[int]]) -> int:
    """DFS"""
    if x == len(triangle) - 1:
        return triangle[x][y]
    if saves[x][y] != 0:
        return saves[x][y]
    min_left = self.dfs(x + 1, y, triangle, saves)
    min_right = self.dfs(x + 1, y + 1, triangle, saves)
    saves[x][y] = min(min_left, min_right) + triangle[x][y]
    return saves[x][y]


def minimum_total(self, triangle: List[List[int]]) -> int:
    """动态规划 - 底向上"""
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[n - 1][i] = triangle[-1][i]
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
    return dp[0][0]


def minimum_total2(self, triangle: List[List[int]]) -> int:
    """动态规划 - 顶向下"""
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    return min(dp[-1])


def minimum_total3(self, triangle: List[List[int]]) -> int:
    """动态规划 - 空间优化"""
    n = len(triangle)
    dp = triangle[-1][:]
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
    return dp[0]
