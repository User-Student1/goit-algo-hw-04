import random
import timeit
import heapq

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr [j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#Злиття
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

#Tismort
def timsort(arr):
    return sorted(arr)

#Timing
sizes = [100, 1000, 5000]
datasets = [random.sample(range(size*10), size) for size in sizes]

def measure_time(sort_func, data):
    return timeit.timeit(lambda: sort_func(data), number=1)

for data in datasets:
    print(f": {len(data)}")
    print(f"Insertion sort: {measure_time(insertion_sort, data):.6f} c")
    print(f"Merge Sort: {measure_time(merge_sort, data):.6f} c")
    print(f"Timsort: {measure_time(timsort, data):.6f} c\n")

#Висновки
#Insertion Sort дуже швидкий для маленьких списків (100 елементів), але на великих (5000+) стає надзвичайно повільним.
#Merge Sort показує стабільну швидкість навіть для великих списків завдяки складності O(n log n).
#Timsort (вбудований Python) найшвидший, особливо на великих масивах.
#Він комбінує сортування злиттям та вставками і додатково оптимізований для реальних даних.
