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
    def recursive_binary_search(arr, target, left = 0, right = None):
        """재귀 이진 탐색"""
        if right is None:
            right = len(arr) - 1
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return SearchAlgorithms.recursive_binary_search(arr, target, mid + 1, right)
        else:
            return SearchAlgorithms.recursive_binary_search(arr, target, left, mid - 1)
        
    @staticmethod
    def ternary_search(arr, target):
        """삼진 탐색: 정렬된 배열에서 세 구간으로 나누어 탐색"""
        def helper(left, right):
            if left > right:
                return -1
            third = (right - left) // 3
            mid1 = left + third
            mid2 = right - third
            if arr[mid1] == target:
                return mid1
            if arr[mid2] == target:
                return mid2
            if target < arr[mid1]:
                return helper(left, mid1 - 1)
            elif target > arr[mid2]:
                return helper(mid2 + 1, right)
            else:
                return helper(mid1 + 1, mid2 - 1)
        return helper(0, len(arr) - 1)

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
    