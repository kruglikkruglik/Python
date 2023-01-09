def calculator(a, b, c, operation):
    result = None

    if operation == '+':
        result = sum(a, b, c)
    elif operation == '*':
        result = multiply(a, b, c)
    else:
        print('Неизвестная операция')

    return result

def ask_operation():
        message = '''
Пожалуйста, введите символ операции, которую вы хотите совершить и нажмите Enter:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение

Ваш выбор:
   '''

        # Запрашиваем у пользователя желаемое действие
        operation = input(2+2*5)

        return operation


def run_calculator():
        # Запрашиваем данные
        a = int(input('2 '))
        b = int(input('2 '))
        c = int(input('5 '))

        # Запрашиваем тип операции
        operation = input(2 + 2 * 5)

        # Производим вычисления
        result = calculate(a, b, c operation)

        # Выводим результат в консоль
        print(f'Результат вычислений: {result}')

