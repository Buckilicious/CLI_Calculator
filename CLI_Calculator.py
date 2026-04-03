print("Shroomy Calculator ready.\nType quit and press enter at any point to close.")
def calc():
    try:
        while True:
            # Get equation
            num1 = float(input('Enter the first number\n'))
            if num1 == 'quit':
                break
            op = input('Enter operator (+, -, *, /)\n')
            if op == 'quit':
                break
            num2 = float(input('Enter the second number\n'))
            if num2 == 'quit':
                break
            if op == '+':
                print(f'Calculation complete\n{num1 + num2}')
            elif op == '-':
                print(f'Calculation complete\n{num1 - num2}')
            elif op == '*':
                print(f'Calculation complete\n{num1 * num2}')
            elif op == '/':
                if num2 == 0:
                    print(ZeroDivisionError)
                else:
                    print(f'Calculation complete\n{num1 / num2}')
            else:
                print('Invalid opertor!')
            continue
    except ValueError:
        print("Invalid input, please enter numbers.")


if __name__ == '__main__':
    calc()