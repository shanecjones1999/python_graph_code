graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


def buildAdjacencyList(edges):
    adjacencyList = {}
    for edge in edges:
        if edge[0] not in adjacencyList:
            adjacencyList[edge[0]] = []
        if edge[1] not in adjacencyList:
            adjacencyList[edge[1]] = []
        adjacencyList[edge[0]].append(edge[1])
        adjacencyList[edge[1]].append(edge[0])
    return adjacencyList


def undirectedPath(edges, src, dst):
    adjacancyList = buildAdjacencyList(edges)
    return hasPath(adjacancyList, src, dst, set())


def hasPath(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited):
            return True

    return False


# print(undirectedPath(edges, 'j', 'k'))


def dfs1(graph, start):
    print(start)
    for neighbor in graph[start]:
        dfs1(graph, neighbor)


# dfs1(graph, 'a')


def bfs(graph, start):
    q = []
    q.append(start)
    while q:
        cur = q.pop(0)
        print(cur)
        for neighbor in graph[cur]:
            q.append(neighbor)


# bfs(graph, 'a')

def hasPathBFS(graph, src, dst):
    q = []
    q.append(src)
    while q:
        cur = q.pop(0)
        if cur == dst:
            return True
        for neighbor in graph[cur]:
            q.append(neighbor)
    return False


# print(hasPathBFS(graph, 'a', 'e'))

def countComponents(graph):
    count = 0
    visited = set()
    for node in graph.keys():
        if node not in visited:
            explore(graph, node, visited)
            count += 1
    return count


def explore(graph, src, visited):
    visited.add(src)
    for neighbor in graph[src]:
        if neighbor not in visited:
            explore(graph, neighbor, visited)


compGraph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
    7: [6, 9],
    6: [7, 9],
    9: [7, 6]
}

# print(countComponents(compGraph))


def largestComponent(graph):
    maxCount = 0
    visited = set()
    for node in graph.keys():
        if node not in visited:
            val = explore2(graph, node, visited)
            maxCount = max(val, maxCount)
    return maxCount


def explore2(graph, src, visited):
    size = 1
    visited.add(src)
    for neighbor in graph[src]:
        if neighbor not in visited:
            size += explore2(graph, neighbor, visited)
    return size


# print(largestComponent(compGraph))

edges2 = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

compGraph2 = buildAdjacencyList(edges2)

edges3 = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]

compGraph3 = buildAdjacencyList(edges3)


def minPath(graph, src, dst):
    visited = set(src)
    q = [[src, 0]]
    while q:
        cur = q.pop(0)
        if cur[0] == dst:
            return cur[1]
        for neighbor in graph[cur[0]]:
            if neighbor not in visited:
                q.append([neighbor, cur[1] + 1])
                visited.add(neighbor)
    return -1


# print(minPath(compGraph2, 'w', 'z'))
# print(minPath(compGraph3, 'b', 'g'))


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]


def countIslands(grid):
    count = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore3(grid, r, c, visited):
                count += 1
    return count


def explore3(grid, r, c, visited):
    validRow = (0 <= r) and (r < len(grid))
    validCol = (0 <= c) and c < len(grid[0])
    if not validRow or not validCol:
        return False

    if grid[r][c] == 'W':
        return False

    pos = str(r)+','+str(c)
    if pos in visited:
        return False
    visited.add(pos)

    explore3(grid, r-1, c, visited)
    explore3(grid, r+1, c, visited)
    explore3(grid, r, c-1, visited)
    explore3(grid, r, c+1, visited)

    return True


# print(countIslands(grid))

def minimumIsland(grid):
    minSize = 2**32
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreSize(grid, r, c, visited)
            if size > 0:
                minSize = min(minSize, size)
    return minSize


def exploreSize(grid, r, c, visited):
    validRow = (0 <= r) and (r < len(grid))
    validCol = (0 <= c) and c < len(grid[0])
    if not validRow or not validCol:
        return 0

    if grid[r][c] == 'W':
        return 0
    pos = str(r)+','+str(c)
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1
    size += exploreSize(grid, r-1, c, visited)
    size += exploreSize(grid, r+1, c, visited)
    size += exploreSize(grid, r, c-1, visited)
    size += exploreSize(grid, r, c+1, visited)

    return size


# print(minimumIsland(grid))
