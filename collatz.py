


def collatz(number):
    number = int(number)

    if number % 2 == 0:
        number = number // 2
    elif number % 2 != 0:
        number = (3*number) +1
    return number

def simpleMathProblem(number):
    number = int(number)
    #number = (int(input()))
    
    set = []
    set.append(number)

    while number > 1:
        number = collatz(number)
        set.append(number)
    return set


print(simpleMathProblem(16))
