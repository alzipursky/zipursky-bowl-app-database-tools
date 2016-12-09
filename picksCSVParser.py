import csv

with open('2015_picks.csv', 'rb') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    outputFile = open('picksInsertScript.txt', 'wb')
    for row in csvReader:
        username = row[0]
        # insert username into users table
        outputFile.write("insert into users (username) values (\'" + str(username) + "\');\n")
        for x in row:
            if x != username:
                # insert each pick into the picks table
                outputFile.write("insert into picks (picker_username, bowl_game, team_picked) values "
                                 "((select id from users where username=\'" + str(username) +
                                 "\'),(select id from bowl_games where home_team=(select id from football_teams where school_name=\'" + str(x) +
                                 "\') or away_team=(select id from football_teams where school_name=\'" + str(x) + "\'))," +
                                 "(select id from football_teams where school_name=\'" + str(x) + "\')" + ");\n")
    outputFile.close()