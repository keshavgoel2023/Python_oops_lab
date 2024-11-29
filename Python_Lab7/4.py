def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    L, R = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return sorted(L + R)

print(merge_sort([5, 3, 8, 6, 2]))
