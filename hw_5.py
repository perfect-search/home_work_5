import re


def caching_fibonacci():
    # Создаем словарь
    cache = dict()

    def fibonacci(number: int):
        # вычесления на основе словаря
        if (number <= 0):
            return 0
        elif (number == 1):
            return 1
        elif (number in cache):
            return cache[number]

        # рекурсия
        cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return cache[number]

    # возврат вложенной функции
    return fibonacci


fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610


def generator_numbers(text: str):
    # Регулярка для чисел
    pattern = r'\d+\.\d+'
    for number in re.findall(pattern, text):
        yield float(number)


def sum_profit(text: str, func: callable):
    return sum(func(text))


# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
