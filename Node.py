class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node(5)
b = Node(7)
c = Node(4)
d = Node(1)
e = Node(9)
f = Node(6)
g = Node(3)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

# Traversing the graph


def dfs1(root=Node):
    if root:
        print(root.val)
    if root.left:
        dfs1(root.left)
    if root.right:
        dfs1(root.right)


def dfs2(root=Node):
    if not root:
        pass
    stack = []
    stack.append(root)
    while stack:
        cur = stack.pop()
        print(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


def bfs(root=Node):
    if not root:
        pass
    q = []
    q.append(root)
    while q:
        cur = q.pop(0)
        print(cur.val)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)

# dfs1(a)

# dfs2(a)

# bfs(a)


def maxRootLeafPath(root=Node):
    if not root:
        return -2**32
    if not root.left and not root.right:
        return root.val
    maxChildPath = max(maxRootLeafPath(root.left),
                       maxRootLeafPath(root.right))
    return root.val + maxChildPath


# print(maxRootLeafPath(a))
