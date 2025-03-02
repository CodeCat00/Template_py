from typing import List


def find_kth_largest(self, nums: List[int], k: int) -> int:
    """查找第K大的元素"""
    low, high = 0, len(nums) - 1
    target = len(nums) - k

    while low <= high:
        pivot = self.partition(nums, low, high)
        if pivot == target:
            return nums[pivot]
        elif pivot < target:
            low = pivot + 1
        else:
            high = pivot - 1

    return -1


def partition(self, nums: List[int], low: int, high: int) -> int:
    """分区操作"""
    pivot = nums[low]
    left, right = low + 1, high

    while left <= right:
        if nums[left] > pivot and nums[right] < pivot:
            self.swap(nums, left, right)

        if nums[left] <= pivot:
            left += 1
        if nums[right] >= pivot:
            right -= 1

    self.swap(nums, low, right)
    return right


def swap(self, nums: List[int], i: int, j: int):
    """交换元素"""
    nums[i], nums[j] = nums[j], nums[i]
