def countdown(num):
    newArr = []
    for i in range(num, -1, -1):
        newArr.append(i)
    return newArr


print(countdown(5))


def p_r(list):
    print(list[0])
    return (list[1])


print(p_r([1, 2]))


def f_p(list):
    return list[0] + len(list)


print(f_p([1, 2, 3, 4, 5]))


def greaterThanSecond(list):
    counter = 0
    newArr = []
    if len(list) < 2:
        return False
    for i in range(0, len(list), 1):
        if list[i] > list[1]:
            counter += 1
            newArr.append(list[i])
    print(counter)
    return newArr


print(greaterThanSecond([5, 2, 3, 2, 1, 4]))


def length_and_value(size, val):
    newArr = []
    for i in range(0, size, 1):
        i = val
        newArr.append(i)
    return newArr


print(length_and_value(4, 7))
print(length_and_value(6, 2))
