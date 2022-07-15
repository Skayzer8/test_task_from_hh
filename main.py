# # 1 задание

def is_even(value):
    """1 вариант из ТЗ
    Плюсы: код проще для восприятия, более высокоуровневая операция.
    Минусы: медленная по сравнению с побитовым И скорость выполнения."""
    return value % 2 == 0


def is_even_bitwise(value):
    """2 вариант - сравнение двоичного представление числа с двоичным
    представлением единицы (001),  через побитовое И. Значение выражения
    x&1 равно 1, если число x нечетное, и 0, если x четное.
    Можно также реализовать через побитовые сдвиги, но читаемость кода
    будет хуже.
    Плюсы: скорость выполнения, возможность оптимизации,
    Минусы: затрудняется чтение кода, при слишком активном примении код
    становится труднее поддерживать, риск возникновения ошибок на низких
    уровнях программиирования."""
    return value & 1 == 0


# 2 задание
# Первая реализация  требует больше памяти,однако работает эффетивнее, за счет
#  отсутствия необходимости перемещать элементы.
# 1st version

class CyclesBuffer:
    def __init__(self, full):
        self.full = full
        self.data = []

    class Full:
        def append(self, value):
            self.data[self.buffer] = value
            self.buffer = (self.buffer+1) % self.full

        def get(self):
            return self.data[self.buffer:]+self.data[:self.buffer]

    def append(self, x):
        self.data.append(x)
        if len(self.data) == self.full:
            self.buffer = 0

    def get(self):
        return self.data

# 2nd version:


class CyclesBuffering():
    def __init__(self, full):
        self.index = 0
        self.full = full
        self.data = []

    def record(self, value):
        if len(self.data) == self.full:
            self.data[self.index] = value
        else:
            self.data.append(value)
        self.index = (self.index + 1) % self.full

    def getitem(self, key):
        return(self.data[key])

    def get_all(self):
        return(self.data)


# 3 задание
# Как правило наиболее эффективным в данном случае является выбор в сторону
# сортировки слиянием, сложность которой О(nlogn) в худшем случае.

def merge_array(left, right):
    """Функция выполняющая объединение частей массива. На вход получает
    две части массива, выполняет поэлементное сравнение и счет индексов.
    Возвращает осортированный массив."""
    sorted_array = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    if left_index < len(left):
        sorted_array += left[left_index:]
    if right_index < len(right):
        sorted_array += right[right_index:]
    return sorted_array


def merge_sort(array):
    """Функция выполняющая разбиение массива на 2 части,  на вход получает
    несортированный массив. Возвращает две половины массива и передает его
    в функцию merge_array. Применяется рекурсия. Если число элементов в массиве
    равно 1, часть массива считается отсортированной."""
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[middle:])
    right = merge_sort(array[:middle])
    return merge_array(left, right)


# Если массив вводится с клавиатуры можно распаковать следующим образом:
array = list(map(int, input().split()))
print(merge_sort(array))
# Либо передать в качестве аргумента в функцию
array1 = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
print(merge_sort(array1))
