from collections import deque
from time import perf_counter

# My solution:
def selection_sort(arr: list) -> deque[int]:
    res: deque[int] = deque()
    while arr:
        max_ind = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_ind]:
                max_ind = i
        res.appendleft(arr.pop(max_ind))
    return res




# Book solution:
def smallest_index(arr: list[int]) -> int:
    min_val = arr[0]
    min_ind = 0
    for _ in range(1, len(arr)):
        if arr[_] < min_val:
            min_val = arr[_]
            min_ind = _
    return min_ind

def book_selection_sort(arr: list[int]) -> list[int]:
    res = []
    for _ in range(len(arr)):
        res.append(arr.pop(smallest_index(arr)))
    return res


arr1 = [5, 3, 6, 2, 10]
arr2 = [5, 3, 6, 2, 10]

now = perf_counter()
print(book_selection_sort(arr1), perf_counter() - now)
now = perf_counter()
print(selection_sort(arr2), perf_counter() - now)