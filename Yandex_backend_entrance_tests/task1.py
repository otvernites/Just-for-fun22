def str_match(a, b):
    str_len = len(a)
    result = ["I"] * str_len

    letter_dict = {}
    # подсчет букв оригинальной строки
    for letter in a:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    # заполнение точно подходящих P
    for i in range(str_len):
        if a[i] == b[i] and letter_dict[a[i]] >= 1:
            letter_dict[a[i]] -= 1
            result[i] = "P"

    # заполнение остатков S
    for i in range(str_len):
        if b[i] in letter_dict.keys() and a[i] != b[i] and letter_dict[b[i]] >= 1:
            letter_dict[b[i]] -= 1
            result[i] = "S"

    return ''.join(result)


if __name__ == '__main__':
    a = input()
    b = input()
    print(str_match(a, b))
