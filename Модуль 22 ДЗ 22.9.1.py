def is_valid_sequence(sequence):
    # Проверка, чтобы все элементы в последовательности были числами
    try:
        numbers = list(map(int, sequence.split()))
        return True, numbers
    except ValueError:
        return False, []


def insertion_sort(arr):
    # Реализация сортировки вставками
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def binary_search(arr, target):
    # Реализация двоичного поиска для нахождения нужной позиции
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid  # Элемент найден
    return left  # Возвращаем позицию вставки


def main():
    input_sequence = input("Введите последовательность чисел через пробел: ")
    target_input = input("Введите любое число: ")

    # Проверка правильности ввода последовательности чисел
    is_valid, sequence = is_valid_sequence(input_sequence)
    if not is_valid:
        print("Введенная последовательность содержит нечисловые значения. Пожалуйста, введите правильные данные.")
        return

    # Проверка правильности ввода целевого числа
    try:
        target_number = int(target_input)
    except ValueError:
        print("Введенное число не является целым. Пожалуйста, введите правильное число.")
        return

    # Сортировка списка
    sorted_sequence = insertion_sort(sequence)
    print("Отсортированная последовательность:", sorted_sequence)

    # Нахождение позиции элемента
    position = binary_search(sorted_sequence, target_number)

    # Вывод результата
    if position == len(sorted_sequence):
        print(f"Число {target_number} больше всех элементов в последовательности.")
    elif sorted_sequence[position] == target_number:
        print(f"Число {target_number} находится в последовательности на позиции {position}.")
    else:
        print(f"Число {target_number} должно быть вставлено на позицию {position}, чтобы сохранить порядок.")


if __name__ == "__main__":
    main()