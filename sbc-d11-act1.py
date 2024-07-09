def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"After swapping '{arr[j]}' and '{arr[j + 1]}': {' '.join(arr)}")

arr = ["Q", "S", "A", "M", "Z", "R"]
print("Initial array is:", arr)
bubble_sort(arr)
print("Sorted array is:", arr)
