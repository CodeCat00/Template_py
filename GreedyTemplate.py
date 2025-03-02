from typing import List


def can_jump(self, nums: List[int]) -> bool:
    """跳跃"""
    max_len = 0
    for i in range(len(nums)):
        if i > max_len:
            return False
        max_len = max(max_len, i + nums[i])
    return True


def find_content_children(self, g: List[int], s: List[int]) -> int:
    """分发"""
    g.sort()
    s.sort()

    p, q = 0, 0
    while p < len(g) and q < len(s):
        if g[p] <= s[q]:
            p += 1
        q += 1

    return p
