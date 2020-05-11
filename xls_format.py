import shutil
import datetime
import csv


today = datetime.datetime.today()
date = today.strftime("%m.%d.%Y-%H.%M.%S")
print(date)

def xls(date):
    shutil.copyfile("original.csv", "{}_statistic.csv".format(date))
    path = "{}_statistic.csv".format(date)

    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["Ваши игры:", "Время, проведенное в игре:", "Счет:", "Win Rate:", "История побед:"])
        for line in data:
            writer.writerow(line[1:])