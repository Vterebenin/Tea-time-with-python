# should return count of array with only values with True
def count_sheeps(arrayOfSheeps):
    B = list(filter(lambda x: x == True, arrayOfSheeps))
    return (len(B))

# there is actually a count specific options, so best practices is:


def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)


# * Tests

count_sheeps([True, True, False, True, True, False])
count_sheeps([True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True,
              False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False])
