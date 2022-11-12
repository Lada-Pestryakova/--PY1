from random import randint


def get_unique_list_numbers(start_=-10, end_=10, size=15) -> list[int]:  # TODO написать функцию для получения списка уникальных целых чисел
    list_ = []
    while len(list_) != size:
        num = randint(start_, end_)
        if num not in list_:
            list_.append(num)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
