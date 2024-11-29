def linear_search(arr, x):
    return next((i for i, val in enumerate(arr) if val == x), -1)

print(linear_search([5, 3, 8, 6, 2], 8))
