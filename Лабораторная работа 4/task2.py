def get_count_char(str_):
    number_of_chars = {}  # TODO посчитать количество каждой буквы в строке в аргументе str_
    DEFAULT_COUNT = 0
    for char in str_.lower():
        if char.isalpha():
            number_of_chars[char] = number_of_chars.get(char, DEFAULT_COUNT) + 1
    return number_of_chars


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


def get_percentage_char(dict_):
    for char in dict_:
        dict_[char] = round((dict_.get(char) / sum(dict_.values())) * 100, 2)
    return dict_

