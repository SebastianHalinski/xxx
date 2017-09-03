def count_games(file_name):
    with file_name as f:
        print(len(f.readlines()))


def decide(file_name, year):
    path = r'/home/sebastian/Dokumenty/SI_week4/cw2/game_stat.txt'
    file_name = open(path, "r")

    row = []
    for line in file_name.readlines():
        tmp = []
        for i in line.split('\t'):
            tmp.append(i)
        row.append(tmp)
    true = 0
    for l in row:
        if l[2] == year:
            true = 1
    return true == 1



def get_latest(file_name):
    path = r'/home/sebastian/Dokumenty/SI_week4/cw2/game_stat.txt'
    file_name = open(path, "r")
    row = []
    for line in file_name.readlines():
        tmp = []
        for i in line.split('\t'):
            tmp.append(i)
        row.append(tmp)
    year = []
    for i in row:
        year.append(i[2])
    print(max(year))
    print(year)
    print(year.index(max(year)))
    new_game_index = int(year.index(max(year)))
    print(row[new_game_index][0])


def count_by_genre(file_name, genre):
    path = r'/home/sebastian/Dokumenty/SI_week4/cw2/game_stat.txt'
    file_name = open(path, "r")
    row = []
    for line in file_name.readlines():
        tmp = []
        for i in line.split('\t'):
            tmp.append(i)
        row.append(tmp)
    count = 0
    for i in row:
        if genre == str(i[3]):
            print(float(i[1]))
            count += 1
    return count


def get_line_number_by_title(file_name, title):
    path = r'/home/sebastian/Dokumenty/SI_week4/cw2/game_stat.txt'
    file_name = open(path, "r")

    row = []
    for line in file_name.readlines():
        tmp = []
        for i in line.split('\t'):
            tmp.append(i)
        row.append(tmp)
    total = []
    for i in row:
        if title == str(i[0]):
            print(row.index(i) + 1)



def main():
    title =[]
    path = r'/home/sebastian/Dokumenty/SI_week4/cw2/game_stat.txt'
    file_name = open(path, "r")
    count_games(file_name)
    decide(file_name, "2000")
    get_latest(file_name)
    count_by_genre(file_name, "First-person shooter")
    get_line_number_by_title(file_name, "Counter-Strike: Condition Zero")

main()
