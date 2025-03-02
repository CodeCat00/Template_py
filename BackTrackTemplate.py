from typing import List


def backtrack_subsets(nums: List[int], start: int, current_subset: List[int], result: List[List[int]]):
    """子集"""
    result.append(current_subset[:])  # 添加当前子集的副本

    for i in range(start, len(nums)):
        current_subset.append(nums[i])  # 做出选择
        backtrack_subsets(nums, i + 1, current_subset, result)  # 递归调用
        current_subset.pop()  # 撤销选择


def backtrack_permutations(nums: List[int], used: List[bool], current_permutation: List[int], result: List[List[int]]):
    """全排列"""
    if len(current_permutation) == len(nums):
        result.append(current_permutation[:])
        return

    for i in range(len(nums)):
        if used[i]:
            continue

        used[i] = True
        current_permutation.append(nums[i])
        backtrack_permutations(nums, used, current_permutation, result)
        current_permutation.pop()
        used[i] = False


def backtrack_combinations(n: int, target: int, start: int, current_combination: List[int], result: List[List[int]]):
    """组合"""
    if target == 0:
        result.append(current_combination[:])
        return

    for i in range(start, n + 1):
        if i > target:  # 剪枝
            break

        current_combination.append(i)
        backtrack_combinations(n, target - i, i + 1, current_combination, result)
        current_combination.pop()


# 示例调用
if __name__ == "__main__":
    nums = [1, 2, 3]
    subsets_result = []
    backtrack_subsets(nums, 0, [], subsets_result)
    print("子集:", subsets_result)

    permutations_result = []
    backtrack_permutations(nums, [False] * len(nums), [], permutations_result)
    print("全排列:", permutations_result)

    combinations_result = []
    backtrack_combinations(5, 5, 1, [], combinations_result)
    print("组合:", combinations_result)
