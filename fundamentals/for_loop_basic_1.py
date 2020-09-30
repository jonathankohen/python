for i in range(0, 151, 1):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101, 1):
    if i % 10 == 0:
        print("Coding")
    elif i % 5 == 0:
        print("Dojo")
    else:
        print(i)

oddSum = 0
for i in range(0, 500000, 1):
    if i % 3 == 0:
        oddSum += i
print(oddSum)

for i in range(2018, -1, -4):
    if i % 2 == 0:
        print(i)

lowNum = 8
highNum = 320
mult = 8
for i in range(lowNum, highNum + 1, 1):
    if (i % mult == 0):
        print(i)
