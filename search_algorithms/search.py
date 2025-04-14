# search_algorithms/search.py

class SearchAlgorithms:

    @staticmethod
    def linear_search(arr, target):
        """선형 탐색: 배열을 처음부터 끝까지 순차적으로 탐색"""
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    @staticmethod
    def binary_search(arr, target):
        """이진 탐색: 정렬된 배열에서 중간값과 비교하며 탐색"""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    @staticmethod
    def dfs(graph, start, visited = None):
        """깊이 우선 탐색 (DFS): 재귀 방식"""
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                SearchAlgorithms.dfs(graph, neighbor, visited)
        return visited
    
    @staticmethod
    def bfs(graph, start):
        """너비 우선 탐색 (BFS): 큐 사용"""
        from collections import deque
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited
    