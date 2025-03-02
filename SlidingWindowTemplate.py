from typing import List


def sliding_window(self, nums: List[int], k: int) -> int:
    """滑动窗口模板"""
    left, right = 0, 0  # 定义左右指针
    total = 0  # 用来跟踪窗口内的数值和
    result = 0  # 存储结果

    while right < len(nums):
        # 扩大窗口，加入右边元素
        total += nums[right]

        # 判断窗口是否满足条件，如：窗口大小为 k
        while right - left + 1 > k:
            total -= nums[left]  # 缩小窗口，移除左边元素
            left += 1

        # 当窗口大小为 k 时，更新结果
        if right - left + 1 == k:
            result = max(result, total)  # 根据题意更新结果（这里假设是最大和）

        right += 1  # 扩大窗口

    return result  # 返回最终结果
