import random


def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    rng = range(len(arr))
    pivot_ind = random.choice(rng)
    left, right = [], []
    for _ in rng:
        if _ == pivot_ind:
            continue
        left.append(arr[_]) if arr[_] <= arr[pivot_ind] else right.append(arr[_])
    return quick_sort(left) + [arr[pivot_ind]] + quick_sort(right)


arr = [5, 9, 3, 1, 45, 7, 1, 2, -71, 13]
# arr = [21, 5]
print(quick_sort(arr))