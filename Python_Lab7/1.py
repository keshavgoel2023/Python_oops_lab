 class BubbleSort:
    def sort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

print(BubbleSort().sort([5, 3, 8, 6, 2]))
