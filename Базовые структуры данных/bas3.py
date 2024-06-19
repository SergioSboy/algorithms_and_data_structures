def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token in ["+", "-", "*"]:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    expression = input("Введите выражение в постфиксной записи: ")
    result = evaluate_postfix(expression)
    print(result)
