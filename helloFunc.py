def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

for i in range (0, 3):
    result = spam(i)
    print(result)
