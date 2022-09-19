def find_err():
    with open("input.txt", "r") as f:
        s = f.read(1)
        i = 0

        stack = 0
        result = -1  # результирующая позиция
        first_r_pos = -1
        first_l_pos = -1

        while s != '':
            # обрабатываем строку
            if s == "{":
                stack += 1

                first_l_pos = i if first_l_pos == -1 else first_l_pos
            elif s == "}":
                first_r_pos = i if first_r_pos == -1 else first_r_pos
                if stack != 0:
                    stack -= 1
                    first_l_pos = -1 if stack == 0 else first_l_pos
                elif stack == 0 and result == -1:
                    result = first_r_pos + 1
                elif stack == 0 and result != -1:
                    return -1
            s = f.read(1)
            i += 1

        # анализируем результат
        if stack == 1 and result == -1:  # осталась одна скобка, которую можно удалить
            return first_l_pos + 1
        elif stack == 0:  # могли остаться скобки вида }}{} или {}}
            return result
        else:
            return -1


if __name__ == "__main__":
    print(find_err())
