import sys


def calculate(list):
    while list.count("(") > 0 or list.count("l") > 0:
        while bool(list.count("l")):
            if list.count("l") > 0 and list.count("(") > 0:
                list[list.index("(")] = "l"
                list[list.index("l")] = "("

            parenthesisl = list.index("l")
            parenthesisr = list.index(")")
            inside_parenthesis = list[parenthesisl + 1:parenthesisr]
            list = list[:parenthesisl] + list[parenthesisr + 1:]
            list.insert(parenthesisl, calculate(inside_parenthesis))

        if list.count("(") == 0 and list.count("l") == 0:
            break

        list[list.index("(")] = "l"
        if "(" not in list or list.index(")") < list.index("("):
            parenthesisl = list.index("l")
            parenthesisr = list.index(")")
            inside_parenthesis = list[parenthesisl + 1:parenthesisr]
            list = list[:parenthesisl] + list[parenthesisr + 1:]
            list.insert(parenthesisl, calculate(inside_parenthesis))
        else:
            parenthesisl = list.index("(")
            parenthesisr = list.index(")")
            inside_parenthesis = list[parenthesisl + 1:parenthesisr]
            list = list[:parenthesisl] + list[parenthesisr + 1:]
            list.insert(parenthesisl, calculate(inside_parenthesis))

    while list.count("^") > 0:
        temp = list.index("^")
        list.pop(temp)
        numero2 = list.pop(temp)
        numero1 = list.pop(temp - 1)
        result = float(numero1) ** float(numero2)
        list.insert(temp - 1, result)

    while list.count("*") > 0 or list.count("/") > 0:
        if bool(list.count("*")):
            multiplication_sign = list.index("*")
        if bool(list.count("/")):
            division_sign = list.index("/")

        if list.count("/") == 0:
            list.pop(multiplication_sign)
            numero2 = list.pop(multiplication_sign)
            numero1 = list.pop(multiplication_sign - 1)
            result = float(numero1) * float(numero2)
            list.insert(multiplication_sign - 1, result)

        elif list.count("*") == 0:
            list.pop(division_sign)
            numero2 = list.pop(division_sign)
            numero1 = list.pop(division_sign - 1)
            result = float(numero1) / float(numero2)
            list.insert(division_sign - 1, result)

        elif multiplication_sign < division_sign:
            list.pop(multiplication_sign)
            numero2 = list.pop(multiplication_sign)
            numero1 = list.pop(multiplication_sign - 1)
            result = float(numero1) * float(numero2)
            list.insert(multiplication_sign - 1, result)

        else:
            list.pop(division_sign)
            numero2 = list.pop(division_sign)
            numero1 = list.pop(division_sign - 1)
            result = float(numero1) / float(numero2)
            list.insert(division_sign - 1, result)

    while len(list) >= 3:
        numero1 = float(list.pop(0))
        operator = list.pop(0)
        numero2 = float(list.pop(0))
        if operator == "+":
            list.insert(0, numero1 + numero2)

        elif operator == "-":
            list.insert(0, numero1 - numero2)

    return list[0]


print("\nWelcome to the Expression calculator:")
print("insert the expression with spaces between objects")
print("like: ( 5 + 4 ) * 5 ")
print("write \"QUIT\" to exit\n")

while True:
    print("=-==-==-==-==-==-==-==-==-==-==-=")
    problem = input("insert an expression: ")

    if problem.lower() == "quit":
        break
    problem = problem.strip()

    expression = problem.split(" ")

    print(f"The result is: {calculate(expression)}")
