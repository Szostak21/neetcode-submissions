"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque([node])
        oldToNew = {node: Node(node.val)}

        while q:
            curr = q.popleft()
            copy = oldToNew[curr]
            for nei in curr.neighbors:
                if nei in oldToNew:
                    copy.neighbors.append(oldToNew[nei])
                    continue
                clone = Node(nei.val)
                oldToNew[nei] = clone
                copy.neighbors.append(clone)
                q.append(nei)
                
        return oldToNew[node]