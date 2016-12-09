import csv

with open('2015_bowl_games.csv', 'rb') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    outputFile = open('bowlsInsertScript.txt', 'wb')
    for row in csvReader:
        outputFile.write("insert into football_teams (school_name, school_nick_name, wins, losses) values (\'" + str(row[1]) + "\',\'" + str(row[2]) + "\'," + str(row[3]) + "," + str(row[4]) + ");\n")
        outputFile.write("insert into football_teams (school_name, school_nick_name, wins, losses) values (\'" + str(row[5]) + "\',\'" + str(row[6]) + "\'," + str(row[7]) + "," + str(row[8]) + ");\n")
        if row[9] == 'Dec.':
            outputFile.write("insert into bowl_games (bowl_name, game_time, tv_network, game_date, home_team, away_team) values (\'" + str(row[0]) + "\',\'" + str(row[11]) + " EST\',\'" + str(row[12]) + "\',\'" + "2015-12-" + str(row[10]) + "\',(select id from football_teams where school_name=\'" + str(row[1]) + "\'),(select id from football_teams where school_name=\'" + str(row[5]) + "\'));\n")
        else:
            outputFile.write("insert into bowl_games (bowl_name, game_time, tv_network, game_date, home_team, away_team) values (\'" + str(row[0]) + "\',\'" + str(row[11]) + " EST\',\'" + str(row[12]) + "\',\'" + "2016-1-" + str(row[10]) + "\',(select id from football_teams where school_name=\'" + str(row[1]) + "\'),(select id from football_teams where school_name=\'" + str(row[5]) + "\'));\n")
    outputFile.close()
