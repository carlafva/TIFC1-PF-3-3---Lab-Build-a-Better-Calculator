def addmultiplenumbers(numbers):
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    resultado = 1

    for number in numbers:
        resultado = resultado * number

    return resultado


def isiteven(num):
    return num % 2 == 0


def isitaninteger(num):
    return type(num) == int


def main():
    print(addmultiplenumbers([5, 10, 15]))
    print(multiplymultiplenumbers([2, 3, 4]))
    print(isiteven(4))
    print(isiteven(7))
    print(isitaninteger(5))
    print(isitaninteger(5.5))
    print("Hello learners!")


if __name__ == "__main__":
    main()