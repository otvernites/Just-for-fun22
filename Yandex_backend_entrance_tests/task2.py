def participants_select(disciplines, participants):
    disc_candidates = {}
    # словарь: дисциплина - макс кол-во
    for d in disciplines:
        disc_candidates[d[0]] = [d[1]]

    # добавляю имеющихся отранжированных участников
    for p in participants:
        disc_candidates[p[1]].append(p[0])

    # отбор прошло только необходимое количество
    result = []
    for disc in disc_candidates.values():
        for i in disc[1:int(disc[0]) + 1]:
            result.append(i)

    return "\n".join(sorted(result))


if __name__ == '__main__':
    n = int(input())  # число спец. дисциплин
    disciplines = [input().split(sep=",") for i in range(n)]  # название дисциплины, макс. число участников
    k = int(input())  # число участников соревнования
    participants = sorted([input().split(sep=",") for i in range(k)], key=lambda c: (int(c[2]), -int(c[3])),
                          reverse=True)  # id, дисциплина, кол-во приемов, штраф

    print(participants_select(disciplines, participants))
