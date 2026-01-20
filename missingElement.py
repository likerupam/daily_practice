import performance
@performance.measure_performance
def missing_element(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum

    a = arr.sort()
    for i in range(1, n + 1):
        if a[i - 1] != i:
            return i
arr = list(map(int, input("Enter the array elements: ").split()))
missing = missing_element(arr)
print(f"The missing element is: {missing}")