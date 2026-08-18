# linear Search
def linear_search(arr: list, target: int) -> int:
    """Returns the index of target if found, else -1."""
    for index, val in enumerate(arr):
        if val == target:
            return index
    return -1

data = [10, 50, 30, 70, 40]
print(linear_search(data, 30))  # Output: 2

# Binary Search
def binary_search(arr: list, target: int) -> int:
    """Returns the index of target in a SORTED array, else -1."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1

sorted_data = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(sorted_data, 40))  # Output: 3

# BFS
from collections import deque


def bfs(graph: dict, start: str) -> list:
    """Traverses a graph level-by-level using a Queue."""
    visited = set([start])
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(bfs(graph, "A"))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']

# DFS
def dfs_recursive(graph: dict, node: str, visited=None) -> list:
    """Traverses a graph path-by-path using Recursion (Call Stack)."""
    if visited is None:
        visited = set()

    visited.add(node)
    traversal_order = [node]

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            traversal_order.extend(dfs_recursive(graph, neighbor, visited))

    return traversal_order

print(dfs_recursive(graph, "A"))  # Output: ['A', 'B', 'D', 'E', 'F', 'C']




