# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    results = {} # Создаем пустой словарь для хранения результатов

    for func in functions: # Перебираем все функции из *functions
        try:
            result = func(int_list) # Вызываем текущую функцию с аргументом int_list
            results[func.__name__] = result # Записываем результат в словарь под ключом имени функции
        except TypeError as exc:
            print(f"Ошибка при вызове функции {func.__name__}: {exc}")
    return results


# Пример использования функции # функции min, max, len, sum, sorted (встроенные функции в Python)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
