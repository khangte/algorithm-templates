# sort_algorithms/sort.py

class SortAlgorithms:

    @staticmethod
    def quick_sort(arr):
        """퀵 정렬: 피벗을 기준으로 작은 값, 큰 값으로 나누어 재귀 정렬"""
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        tail = arr[1:]
        left = [x for x in tail if x <= pivot]
        right = [x for x in tail if x > pivot]

        return SortAlgorithms.quick_sort(left) + [pivot] + SortAlgorithms.quick_sort(right)

    @staticmethod
    def counting_sort(arr):
        """계수 정렬: 정수 카운트를 기반으로 정렬"""
        """데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능"""
        if not arr:
            return []
        if min(arr) < 0:
            raise ValueError("Counting sort only supports non-negative integers.")

        count = [0] * (max(arr) + 1)
        for num in arr:
            count[num] += 1

        sorted_arr = []
        for i, c in enumerate(count):
            sorted_arr.extend([i] * c)

        return sorted_arr

    @staticmethod
    def bubble_sort(arr):
        """버블 정렬: 인접한 두 수를 비교하여 큰 값을 뒤로 보내는 방식"""
        arr = arr[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def selection_sort(arr):
        """선택 정렬: 가장 작은 값을 선택하여 맨 앞에 위치"""
        arr = arr[:]
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr):
        """삽입 정렬: 현재 값을 정렬된 부분에 삽입"""
        arr = arr[:]
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break
        return arr

    @staticmethod
    def merge_sort(arr):
        """병합 정렬: 리스트를 반으로 나눈 뒤 정렬하여 병합"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortAlgorithms.merge_sort(arr[:mid])
        right = SortAlgorithms.merge_sort(arr[mid:])

        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
        