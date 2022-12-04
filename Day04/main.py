def OverLapping():
    count = 0
    count2 = 0

    with open("input.txt") as file:
        data = file.read().strip()

    sections = data.split('\n')

    for section in sections:
        pair1, pair2 = section.split(',')
        min1, max1 = map(int, pair1.split('-'))
        min2, max2 = map(int, pair2.split('-'))

        if (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2):
            count += 1

        if set(range(min1, max1 + 1)) & set(range(min2, max2 + 1)):
            count2 += 1

    print("Overlapping fully section pairs count: ", count)
    print("Overlapping sections count: ", count2)


OverLapping()
