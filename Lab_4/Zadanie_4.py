def evaluate_rpn(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit():  # Jeśli liczba, wrzucamy na stos
            stack.append(int(token))
        elif token in operators:  # Jeśli operator, wykonujemy operację
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)  # Zakładamy dzielenie zmiennoprzecinkowe
        else:
            raise ValueError(f"Nieznany symbol: {token}")

    return stack[0] if stack else None  # Wynik końcowy

# Przykładowe użycie
expression = "5 6 + 4 - 3 *"
result = evaluate_rpn(expression)
print("Wynik:", result)