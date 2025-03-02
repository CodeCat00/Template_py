from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive Traversal
def traverse(self, p, result):
    if p is None:
        return
    # Add node value before traversing children for pre-order
    result.append(p.val)
    self.traverse(p.left, result)
    self.traverse(p.right, result)


# Pre-order Traversal (Non-recursive)
def preorder_traversal(self, root):
    result = []
    if root is None:
        return result

    stack = []
    stack.append(root)  # Push root node to stack

    while stack:
        node = stack.pop()  # Visit the current node
        result.append(node.val)  # Record the current node's value

        # Push right child first, then left child to maintain pre-order
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# In-order Traversal (Non-recursive)
def inorder_traversal(self, root):
    result = []
    stack = []
    current = root

    while current or stack:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Visit the node
        current = stack.pop()
        result.append(current.val)

        # Move to the right subtree
        current = current.right

    return result


# Post-order Traversal (Non-recursive)
def postorder_traversal(self, root):
    result = []
    if root is None:
        return result

    stack = []
    output = []
    stack.append(root)

    # Perform pre-order traversal, reversing the order later
    while stack:
        node = stack.pop()
        output.append(node)  # Push root to output stack

        # Push left and right children
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Extract results from the output stack
    while output:
        result.append(output.pop().val)

    return result


# Depth-First Search (DFS)
def dfs(self, p, path, paths):
    if p is None:
        return

    path.append(str(p.val))

    if p.left is None and p.right is None:
        paths.append("->".join(path))
        return

    path.append("->")
    self.dfs(p.left, path.copy(), paths)
    self.dfs(p.right, path.copy(), paths)


# Breadth-First Search (BFS)
def level_order(self, root):
    result = []
    if root is None:
        return result

    queue = deque([root])

    while queue:
        p = queue.popleft()
        result.append(p.val)

        if p.left:
            queue.append(p.left)
        if p.right:
            queue.append(p.right)

    return result
