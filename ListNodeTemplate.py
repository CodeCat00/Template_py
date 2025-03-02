class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(self, head: ListNode) -> ListNode:
    """删除重复节点"""
    p = head
    while p:
        while p.next and p.val == p.next.val:
            p.next = p.next.next
        p = p.next
    return head


def reverse_list(self, head: ListNode) -> ListNode:
    """反转链表"""
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
    """合并两个有序链表"""
    start = ListNode(0)
    curr = start
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return start.next


def middle_node(self, head: ListNode) -> ListNode:
    """快慢指针找到链表的中间节点"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
