def add_ints(arr: list[int]) -> int:
    return arr[-1] + add_ints(arr[:-1]) if len(arr) > 1 else arr[0]


arr = [1,3,4,5,6,3,3,6,7]
print(add_ints(arr))
print(sum(arr))


def len_arr(arr: list) -> int:
    return 0 if not arr else 1 + len_arr(arr[:-1])

arr = [1,2,3,4,5]
print(len_arr(arr))

def max_in_list(arr: list) -> int:
    try:
        arr[1]
        candidat = arr[0]
        next_candidat = max_in_list(arr[1:])
        return candidat if candidat >= next_candidat else next_candidat
    except IndexError:
        return arr[0]

arr = [1,3,19,4,5,6,3,3,6,7]
print(max_in_list(arr))