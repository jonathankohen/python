def biggie_size(list):
    for i in range(0, len(list), 1):
        if list[i] > 0:
            list[i] = 'big'
    return list


print(biggie_size([-1, 3, 5, -5]))


def count_positives(list):
    counter = 0
    for i in range(0, len(list), 1):
        if list[i] > 0:
            counter += 1
    list[len(list) - 1] = counter
    return list


print(count_positives([-1, 1, 1, 1]))


def sum_total(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    return sum


print(sum_total([1, 2, 3, 4]))


def average(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    return sum / len(list)


print(average([1, 2, 3, 4]))


def length(list):
    return len(list)


print(length([37, 2, 1, -9]))


def minimum(list):
    if len(list) == 0:
        return False

    min = list[0]

    for i in range(0, len(list), 1):
        if list[i] < min:
            min = list[i]

    return min


print(minimum([37, 2, 1, -9]))
print(minimum([]))


def maximum(list):
    if len(list) == 0:
        return False

    max = list[0]

    for i in range(0, len(list), 1):
        if list[i] > max:
            max = list[i]

    return max


print(maximum([37, 2, 1, -9]))
print(maximum([]))


def ultimate_analysis(list):
    sum = 0
    min = list[0]
    max = list[0]

    for i in range(0, len(list), 1):
        sum += list[i]
        if list[i] < min:
            min = list[i]
        if list[i] > max:
            max = list[i]

    avg = sum / len(list)

    return "{" + f"'sumTotal': {sum}, 'average': {avg}, 'minimum': {min}, 'maximum': {max}, 'length': {len(list)}" + "}"


print(ultimate_analysis([37, 2, 1, -9]))
