from Table_Data import *


#3 Leagues year 2019
teamPL = ["Arsenal", "Aston Villa", "Bournemouth", "Brighton", "Burnley", "Chelsea", "Crystal Palace","Everton",
          "Leicester", "Liverpool", "Manchester City", "Manchester United", "Newcastle United","Norwich",
          "Sheffield United", "Southampton", "Tottenham", "Watford", "West Ham","Wolverhampton Wanderers"]
teamLL=["Real Madrid","Barcelona", "Atletico Madrid", "Sevilla","Villarreal","Real Sociedad","Granada","Getafe",
        "Valencia","Osasuna","Athletic Club","Levante","Real Valladolid","Eibar","Real Betis","Alaves","Celta Vigo",
        "Leganes","Mallorca","Espanyol"]
teamSA=["Juventus", "Napoli","Atalanta","Inter","AC Milan","Roma","Torino","Lazio","Sampdoria","Bologna","Sassuolo",
        "SPAL 2013","Parma Calcio 1913","Cagliari", "Udinese","Genoa", "Lecce","Brescia","Fiorentina","Verona"]
teamB=["Bayern Munich","Borussia Dortmund","RasenBallsport Leipzig", "Borussia M.Gladbach","Bayer Leverkusen","Hoffenheim",
       "Wolfsburg","Freiburg","Eintracht Frankfurt","Hertha Berlin","Union Berlin","Schalke 04","Mainz 05","FC Cologne",
       "Augsburg","Werder Bremen","Fortuna Duesseldorf","Paderborn"]

#header for header of CSV file
header = ("id,title,GW,xG,xGA,npxG,npxGA,att,def,att,def,deep,deep_allowed,scored,missed,xpts,wins,draws,loses,pts,npxGD\n")


if __name__=='__main__':
    #4 files for the 4 leagues
    SA= open('TableSA.csv', "w")
    SA.write(header)
    LL= open('TableLL.csv', "w")
    LL.write(header)
    PL= open('TablePL.csv', "w")
    PL.write(header)
    B = open('TableB.csv', "w")
    B.write(header)
    tms= [teamB, teamLL, teamSA, teamPL]

    for league in tms:  #for England, Spain and Italy leagues
        for T in league: #TEAMS
            print(T) #output the team selected
            print(league) #outputs the league selected. Should be in accordance with team selected,ie 'T'

            #to get data from leagues, args sent are team, league and file operand
            loop = asyncio.get_event_loop()
            if league == teamPL:
                w = PL
                t=loop.run_until_complete(results(T,'epl',w))
            elif league== teamLL:
                w=LL
                t = loop.run_until_complete(results(T, 'la liga',w))
            elif league== teamSA:
                w=SA
                t = loop.run_until_complete(results(T, 'serie a',w))
            elif league == teamB:
                w = B
                t = loop.run_until_complete(results(T, 'bundesliga', w))

    #close the files!
    SA.close()
    LL.close()
    PL.close()