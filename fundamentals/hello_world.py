# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle!"
print("Hello", name)  # with a comma
print("Hello " + name)  # with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)  # with a comma
# print("Hello" + name)  # with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(
    fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}")  # with an f string


# for i in range(start, condition on when to stop, incrementor,/decrementor)
# 0 - 150
for i in range(0, 150, 1):
    print(i)

x = [1, 2, 3, 4, 5, 15]
for i in range(0, len(x), 1):
    print(i)

# multiples of 5 from 20 to 100
for i in range(20, 101, 5):
    print(i)

for i in range(20, 101, 1):
    if i % 5 == 0:
        print(i)

# add odd ints from 100 - 200
total = 0
for i in range(100, 201, 1):
    if i % 3 == 0:
        total += i
print(total)

lowNum = 8
highNum = 320
mult = 8
for i in range(lowNum, highNum + 1, 1):
    if (i % mult == 0):
        print(i)

for i in range(2030, 2019, -1):
    print(i)


def biggie_size(someList):
    for i in range(0, leng(someList), 1):
        if someList[i] > 0:
            print(someList[i])


biggie_size([-1, 3, 5, -5])

x = [-1, 3, 5, -5, -92, 23, 24, 8, 3, -85]


def negativeCounter(someList):
    negativeTotal = 0
    for i in range(len(someList)):
        print(i)


negativeCounter(x)
