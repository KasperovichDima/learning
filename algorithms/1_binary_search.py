def binary_search(lst: list, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == item:
            return mid
        if lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_lst = [1,3,6,7,9,11,15,19,23,26,33]
print(binary_search(my_lst, 33))
