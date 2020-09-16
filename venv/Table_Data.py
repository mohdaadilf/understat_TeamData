import asyncio
import aiohttp
from understat import Understat

async def results(t_t_g,league,w): #t_t_g is team_to_get ie result , league is league and w is file mode
        # header array to get dict key for csv
        header_array = ["id", "title", "history", "xG", "xGA", "npxG", "npxGA", "ppda", "att", "def", "ppda_allowed", "att",
                    "def", "deep", "deep_allowed", "scored", "missed", "xpts", "wins", "draws", "loses", "pts", "npxGD"]
        global teams
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            #team=input("Enter team:")
            teams = await understat.get_teams(
            league, #league
            2019, #year
            title=t_t_g #team
        )
        t=teams

        for j in range(0, 1):  # outter dict L1
                for i in range(0, 3):  # first 3 array elements (up to hist) L2
                    if i < 1:  # history if
                        print((t[0][header_array[0]]), end=",")
                        w.write((t[0][header_array[0]])+",") #writes id to file
                        team=t[0][header_array[1]]
                    if i >= 2:  # history if (refer docum website and check get_team function example to better understand)
                        gw = 1 #gameweek
                        g=t[0][header_array[i]]
                        for k in g:  # L3 for 38 games
                            print(gw, end=",")
                            w.write(team+","+str(gw) + ",")#writes team and game week
                            for m in range(0, 20):  # L4 for attributes

                                ha = header_array[3:23] #gw to end headers
                                if m == 4 or m == 7:  # ppda and ppda_allowed
                                    print(k[ha[m]][ha[m + 1]], end=",")  # att
                                    print(k[ha[m]][ha[m + 2]], end=",")  # def
                                    w.write((str(k[ha[m]][ha[m + 1]])) + ",")
                                    w.write((str(k[ha[m]][ha[m + 2]])) + ",")

                                elif m == 5 or m == 6 or m == 8 or m == 9:  #ppda and ppda allowed
                                    continue  # att & def

                                else:
                                    print(k[ha[m]], end=",")  # all other attributes
                                    w.write((str(k[ha[m]])) + ",")
                            print("\n")  # jumps to next line for next game

                            gw+=1 #increments game week var
                            if len(g)!=gw-1:
                                    w.write("\n,")
                            else:
                                    w.write("\n\n\n")
        return teams
