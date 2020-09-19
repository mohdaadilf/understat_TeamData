import aiohttp
from understat import Understat

# Lists to get teams for the specified year
teamPL = []
teamLL = []
teamSA = []
teamB = []


async def leagueteams(year):  # gets teams for given year
    leagues = ["epl", "la liga", "serie a", "bundesliga"]  # League names
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        for league in leagues:
            teams = await understat.get_teams(league, year)
            t = teams
            for i in t:
                if league == 'epl':
                    teamPL.append(i['title'])
                elif league == 'la liga':
                    teamLL.append(i['title'])
                elif league == 'serie a':
                    teamSA.append(i['title'])
                elif league == 'bundesliga':
                    teamB.append(i['title'])
    tms = [teamB, teamLL, teamSA, teamPL]
    return tms


async def results(t_t_g, league, w, year):  # t_t_g is team_to_get ie result , league is league and w is file mode
    # header array to get dict key for csv
    header_array = ["id", "title", "history", "xG", "xGA", "npxG", "npxGA", "ppda", "att", "def", "ppda_allowed", "att",
                    "def", "deep", "deep_allowed", "scored", "missed", "xpts", "wins", "draws", "loses", "pts", "npxGD"]
    global teams
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        # team=input("Enter team:")
        teams = await understat.get_teams(league, year, title=t_t_g)  # league, year and team
    t = teams

    for j in range(0, 1):  # outer dict L1
        for i in range(0, 3):  # first 3 array elements (up to hist) L2
            if i < 1:  # history if
                print((t[0][header_array[0]]), end=",")
                w.write((t[0][header_array[0]]) + ",")  # writes id to file
                team = t[0][header_array[1]]
            if i >= 2:  # history if (refer document website and check get_team function example to better understand)
                gw = 1  # game week
                g = t[0][header_array[i]]
                for k in g:  # L3 for 38 games
                    print(gw, end=",")
                    w.write(team + "," + str(gw) + ",")  # writes team and game week
                    for m in range(0, 20):  # L4 for attributes
                        ha = header_array[3:23]  # gw-to-npxGD headers
                        if m == 4 or m == 7:  # ppda and ppda_allowed
                            print(k[ha[m]][ha[m + 1]], end=",")  # att
                            print(k[ha[m]][ha[m + 2]], end=",")  # def
                            w.write((str(k[ha[m]][ha[m + 1]])) + ",")
                            w.write((str(k[ha[m]][ha[m + 2]])) + ",")
                        elif m == 5 or m == 6 or m == 8 or m == 9:  # ppda and ppda allowed
                            continue  # att & def
                        else:  # all other attributes
                            print(k[ha[m]], end=",")
                            w.write((str(k[ha[m]])) + ",")
                    print("\n")  # jumps to next line for next game
                    gw += 1  # increments game week var
                    if len(g) != gw - 1:
                        w.write("\n,")
                    else:
                        w.write("\n\n")
    return teams
