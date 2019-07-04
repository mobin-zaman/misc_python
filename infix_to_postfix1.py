digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def modprint(string):
    print(string, end='')


def E(string):
    T(string)
    Eprime(string[1:])


def Eprime(string):
    if string[0] == '+':
        T(string[1])  # first character of the string
        modprint('+')
        if len(string) <= 3: return
        Eprime(string[2:])

    if string[0] == '-':
        T(string[1])
        modprint('-')
        if len(string) <= 3: return
        Eprime(string[2:])

    else:
        T(string)


def T(string):
    if (len(string) is 0): return
    if string[0] in digit:
        modprint(string[0])
    return


print("input exit to exit")
while (1):
    infix = input()
    if infix == "exit": exit()
    E(infix)
    print()
