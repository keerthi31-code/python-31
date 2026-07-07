def counting_sort(arr):
    maximum = max(arr)

    count = [0] * (maximum + 1)

    # Count frequencies
    for num in arr:
        count[num] += 1

    # Build sorted array
    sorted_arr = []

    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr)) 