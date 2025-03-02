# Quick Sort
def quick_sort(self, nums, start, end):
    if start >= end:  # Recursion termination condition
        return

    pivot = self.partition(nums, start, end)  # Partition the array
    self.quick_sort(nums, start, pivot - 1)  # Recursively sort the left part
    self.quick_sort(nums, pivot + 1, end)  # Recursively sort the right part


def partition(self, nums, left, right):
    pivot = nums[left]
    i, j = left + 1, right

    while i <= j:
        if nums[i] > pivot and nums[j] < pivot:
            self.swap(nums, i, j)
        if nums[i] <= pivot:
            i += 1
        if nums[j] >= pivot:
            j -= 1

    self.swap(nums, left, j)  # Place pivot at the correct position
    return j


# Merge Sort
def merge_sort(self, nums, start, end):
    if start >= end:  # Recursion termination condition
        return

    mid = start + (end - start) // 2  # Find the middle point
    self.merge_sort(nums, start, mid)  # Recursively sort the left part
    self.merge_sort(nums, mid + 1, end)  # Recursively sort the right part
    self.merge(nums, start, mid, end)  # Merge the sorted parts


def merge(self, nums, start, mid, end):
    temp = [0] * (end - start + 1)  # Temporary array to hold merged result
    i, j, k = start, mid + 1, 0

    while i <= mid and j <= end:
        if nums[i] < nums[j]:
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i <= mid:
        temp[k] = nums[i]
        i += 1
        k += 1
    while j <= end:
        temp[k] = nums[j]
        j += 1
        k += 1

    # Copy the sorted array back to the original array
    for p in range(len(temp)):
        nums[start + p] = temp[p]


# Heap Sort
def heap_sort(self, nums):
    n = len(nums)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        self.heapify(nums, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        self.swap(nums, 0, i)  # Swap the root with the last element
        self.heapify(nums, i, 0)  # Heapify the root


def heapify(self, nums, n, i):
    largest = i  # Assume the largest is the root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right

    if largest != i:
        self.swap(nums, i, largest)
        self.heapify(nums, n, largest)  # Recursively heapify


# Three-way Quick Sort
def three_way_quick_sort(self, array, low, high):
    if low < high:
        pivot_indices = self.partition2(array, low, high)
        self.three_way_quick_sort(array, low, pivot_indices[0] - 1)
        self.three_way_quick_sort(array, pivot_indices[1] + 1, high)


def partition2(self, array, low, high):
    pivot = array[low]
    lt, gt = low, high
    i = low + 1

    while i <= gt:
        if array[i] < pivot:
            self.swap(array, lt, i)
            lt += 1
            i += 1
        elif array[i] > pivot:
            self.swap(array, i, gt)
            gt -= 1
        else:
            i += 1

    return [lt, gt]


# Swap function
def swap(self, nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]
