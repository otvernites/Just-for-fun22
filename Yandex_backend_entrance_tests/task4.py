class Point:
    def __init__(self, i=0, j=0):
        self.i = i
        self.j = j


def direction_search(n, m, maze):

    # находим координату стартовой клетки
    current_pos = Point()
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                current_pos = Point(i, j)

    # заполнение направлений
    while True:
        if maze[current_pos.i][current_pos.j + 1] == '.':

            current_pos = Point(current_pos.i, current_pos.j + 1)
            maze[current_pos.i][current_pos.j] = 'L'

        elif maze[current_pos.i][current_pos.j - 1] == '.':

            current_pos = Point(current_pos.i, current_pos.j - 1)
            maze[current_pos.i][current_pos.j] = 'R'

        elif maze[current_pos.i + 1][current_pos.j] == '.':

            current_pos = Point(current_pos.i + 1, current_pos.j)
            maze[current_pos.i][current_pos.j] = 'U'

        elif maze[current_pos.i - 1][current_pos.j] == '.':

            current_pos = Point(current_pos.i - 1, current_pos.j)
            maze[current_pos.i][current_pos.j] = 'D'

        elif (maze[current_pos.i][current_pos.j]) != "S":
            curr_letter = maze[current_pos.i][current_pos.j]
            if curr_letter == "R":
                current_pos = Point(current_pos.i, current_pos.j + 1)
            elif curr_letter == "L":
                current_pos = Point(current_pos.i, current_pos.j - 1)
            elif curr_letter == "D":
                current_pos = Point(current_pos.i + 1, current_pos.j)
            else:
                current_pos = Point(current_pos.i - 1, current_pos.j)
        else:
            break

    return maze


if __name__ == '__main__':
    n, m = map(int, input().split())  # n - кол-во строк, m - столбцов
    maze = [list(input()) for i in range(n)]  # план эвакуации
    result = direction_search(n, m, maze)
    for str in result:
        print("".join(str))
