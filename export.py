import reports
path = r'/home/sebastian/Dokumenty/SI_week4/cw2/game_stat.txt'
file_name = open(path, "r")
list_answers = [str(reports.count_games(file_name)),
str(reports.decide(file_name, "2000")),
str(reports.get_latest(file_name)),
str(reports.count_by_genre(file_name, "Simulation")),
str(reports.get_line_number_by_title(file_name, "Counter-Strike: Condition Zero"))
]
print (list_answers)

path1 = r'/home/sebastian/Dokumenty/SI_week4/cw2/export.txt'
import sys
sys.stdout = open(path1,'wt')
for i in list_answers:
    print(i)
