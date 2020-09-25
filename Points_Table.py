import csv
import os


# to create points table
def pointstable(year):
    path = os.getcwd()
    csv_path = path + "\\CSV_Files"
    # Reading from league files to get team data's
    SA = open(csv_path + '\\TableSA' + year + '.csv', "r")
    readerSA = csv.reader(SA)
    LL = open(csv_path + '\\TableLL' + year + '.csv', "r")
    readerLL = csv.reader(LL)
    PL = open(csv_path + '\\TablePL' + year + '.csv', "r")
    readerPL = csv.reader(PL)
    B = open(csv_path + '\\TableB' + year + '.csv', "r")
    readerB = csv.reader(B)
    readers = [readerB, readerLL, readerPL, readerSA]  # to read each file

    # For Points Table!
    header = "title,Played,xG,xGA,npxG,npxGA,p_att,p_def,op_att,op_def,deep,deep_allowed,GF,GA,GD,xpts,wins,draws,loses,pts,npxGD\n"
    SA_T = open(csv_path + '\\SerieA' + year + '.csv', "w")
    SA_T.write(header)
    LL_T = open(csv_path + '\\LaLiga' + year + '.csv', "w")
    LL_T.write(header)
    PL_T = open(csv_path + '\\EPL' + year + '.csv', "w")
    PL_T.write(header)
    B_T = open(csv_path + '\\Bundesliga' + year + '.csv', "w")
    B_T.write(header)

    for rdr in readers:
        played = xG = xGA = npxG = npxGA = p_att = p_def = pa_att = pa_def = deep = deep_allowed = GF = GA = xpts = wins = draws = loses = pts = npxGD = gd = 0
        Values = next(rdr)  # header
        print(Values)
        for row in rdr:
            if not row:  # this line doesn't execute at first. Program always (must and) will go to else condition
                if rdr == readerB:  # for writing to respective league file
                    w = B_T
                elif rdr == readerSA:
                    w = SA_T
                elif rdr == readerPL:
                    w = PL_T
                elif rdr == readerLL:
                    w = LL_T
                # calculating goal difference and writing all the elements/attributes
                gd = GF - GA
                w.write(title + "," + (str(played)) + " games" + "," + (str(xG)) + "," + (str(xGA)) + "," + (str(npxG)) + "," + (str(npxGA)) + "," + (
                    str(p_att)) + "," + (str(p_def)) + "," + (str(pa_att)) + "," + (str(pa_def)) + "," + (
                            str(deep)) + "," + (str(deep_allowed)) + "," + (str(GF)) + "," + (str(GA)) + "," + str(
                    gd) + "," + (
                            str(xpts)) + "," + (str(wins)) + "," + (str(draws)) + "," + (str(loses)) + "," + (
                            str(pts)) + "," + (str(npxGD)) + "\n")
                xG = xGA = npxG = npxGA = p_att = p_def = pa_att = pa_def = deep = deep_allowed = GF = GA = xpts = wins = draws = loses = pts = npxGD = gd = 0
                continue
            else:
                print(row)
                title = row[1]
                played = int(row[2])
                xG += float(row[3])
                xGA += float(row[4])
                npxG += float(row[5])
                npxga = (row[6])
                npxga = npxga.strip()  # written to avoid some anomalies, remove/fix at your own risk
                npxGA += float(npxga)
                p_att += int(row[7])
                p_def += int(row[8])
                pa_att += int(row[9])
                pa_def += int(row[10])
                deep += int(row[11])
                deep_allowed += int(row[12])
                GF += int(row[13])
                GA += int(row[14])
                xpts += float(row[15])
                wins += int(row[16])
                draws += int(row[17])
                loses += int(row[18])
                pts += int(row[19])
                npxGD += float(row[20])

    SA_T.close()
    SA.close()
    B_T.close()
    B.close()
    LL_T.close()
    LL.close()
    PL_T.close()
    PL.close()

    # sorting
    leagues = ["SerieA", "Bundesliga", "LaLiga", "EPL"]
    for league in leagues:
        with open(csv_path + '\\' + league + year + '.csv', "r", newline='') as f_input:  # reads unsorted file
            csv_input = csv.DictReader(f_input)  # reads as dict reader so we can sort based on arg given in next line
            data = sorted(csv_input, key=lambda row: (row['pts'], row['GD'], row['GF']), reverse=True)
        with open(csv_path + '\\' + league + year + '.csv', 'w', newline='') as f_output:  # writes to same file
            csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
            csv_output.writeheader()
            csv_output.writerows(data)
