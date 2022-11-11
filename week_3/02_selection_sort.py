input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)

    for i in range(5 - 1):
        min_index = i
        for j in range(5 - i):
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index]= array[min_index], array[i]

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!