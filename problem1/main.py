def find_min_and_max(arr):
    if not arr:
        return None

    min_value = arr[0]
    max_value = arr[0]
    min_index = 0
    max_index = 0

    for i in range(len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
        elif arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    result = f"min: {min_value} index: {min_index} max: {max_value} index: {max_index}"
    return result

if __name__ == "__main__":
    print(find_min_and_max([5, 7, 4, -2, -1, 8]))
    # min: -2 index: 3 max: 8 index: 5
    print(find_min_and_max([2, -5, -4, 22, 7, 7]))
    # min: -5 index: 1 max: 22 index: 3
    print(find_min_and_max([4, 3, 9, 4, -21, 7]))
    # min: -21 index: 4 max: 9 index: 2
    print(find_min_and_max([-1, 5, 6, 4, 2, 18]))
    # min: -1 index: 0 max: 18 index: 5
    print(find_min_and_max([-2, 5, -7, 4, 7, -20]))
    # min: -20 index: 5 max: 7 index: 4