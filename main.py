from Table_Data import *
from Points_Table import pointstable
import os
import asyncio

if __name__ == '__main__':
    # header for header of CSV file
    header = "id,title,GW,xG,xGA,npxG,npxGA,att,def,att,def,deep,deep_allowed,GF,GA,xpts,wins,draws,loses,pts,npxGD\n"
    year = input("Enter year:")

    # 4 files for the 4 leagues with accordance to year; files are saved in specific folder
    path = os.getcwd()
    while not os.path.exists(path + "\\CSV_Files"):  # makes folder if not found before
        os.mkdir(path + "\\CSV_Files")
    csv_path = path + "\\CSV_Files"
    print("Files will be saved to path: " + csv_path)
    SA = open(csv_path + '\\TableSA' + year + '.csv', "w")
    SA.write(header)
    LL = open(csv_path + '\\TableLL' + year + '.csv', "w")
    LL.write(header)
    PL = open(csv_path + '\\TablePL' + year + '.csv', "w")
    PL.write(header)
    B = open(csv_path + '\\TableB' + year + '.csv', "w")
    B.write(header)

    loop = asyncio.get_event_loop()
    tms = loop.run_until_complete(leagueteams(year))  # gets teams with respect to league

    for league in tms:  # for England, Spain and Italy leagues team data
        for T in league:  # T=TEAMS
            print("Teams in the league:", league)  # outputs the teams in selected league. Should be in accordance with
            # team selected,ie 'T'

            if league == teamPL:
                w = PL
                t = loop.run_until_complete(results(T, 'epl', w, year))
            elif league == teamLL:
                w = LL
                t = loop.run_until_complete(results(T, 'la liga', w, year))
            elif league == teamSA:
                w = SA
                t = loop.run_until_complete(results(T, 'serie a', w, year))
            elif league == teamB:
                w = B
                t = loop.run_until_complete(results(T, 'bundesliga', w, year))

    # close the files!
    SA.close()
    LL.close()
    PL.close()
    B.close()

    pointstable(year)  # for points table!

# thank you stack overflow and the hundred of random strangers on the internet + google
# also thank you to Amos, understat and Reddit without this wouldn't have happened

# understat website https://understat.com/
# documentation website https://understat.readthedocs.io/en/latest/
