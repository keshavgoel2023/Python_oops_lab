def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x: return m
        l, r = (m + 1, r) if arr[m] < x else (l, m - 1)
    return -1

print(binary_search(sorted([5, 3, 8, 6, 2]), 8))
