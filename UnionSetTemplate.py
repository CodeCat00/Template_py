def __init__(self, size):
    self.parent = list(range(size))  # 初始化每个节点的父节点为自身
    self.rank = [1] * size  # 初始化每个节点的秩为 1

    # 查找节点的根节点，并进行路径压缩


def find(self, x):
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])  # 路径压缩
    return self.parent[x]

    # 合并两个集合


def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x != root_y:
        # 按秩合并，保证树的高度尽量小
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    # 判断两个节点是否属于同一个集合


def connected(self, x, y):
    return self.find(x) == self.find(y)
