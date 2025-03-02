from typing import List


def search(self, nums: List[int], target: int) -> int:
    """二分搜索"""
    # 1、初始化 left 和 right
    left, right = 0, len(nums) - 1

    # 2、处理 while 循环
    while right - left > 1:
        mid = left + (right - left) // 2
        # 3、比较 nums[mid] 和 target
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid
            continue

        right = mid

    # 4、最后剩下两个元素，手动判断
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1
