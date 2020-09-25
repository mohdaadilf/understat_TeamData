# understat_TeamData

This is an extension (sort of) to the understat package (refer to https://understat.readthedocs.io/en/latest/ ). 
The 3 files main.py, Points_Table.py, and Table_Data.py are pretty self-explanatory. 
Make sure to install understat package. To do this, go to cmd and type "pip install understat" without the quotes.

Updates:

25/9/20:
League tables aren't always accurate. When two or more teams have same points, GD is considered. If GD is same, GF is considered. In some leagues, head-to-head results is considered and taken into account.
I am both lazy and also not sure how to write code for that. I do have reason to believe the table will be more accurate as more games are played and results are more dynamic.

19/9/20:
Team lists needn't be manually updated. Just a year is required as input, the rest is handled by the program.
The program saves all the data into a CSV file from where you can view your data.
The data saved are:
A. Each game data for each team ('get_teams' function). A CSV file is saved for each league for each year with all team data inside these league CSV's. These CSV files are preceded by 'Team', following the League name and year. 
B. League Table (Not sure how accurate it is when it comes to the same points and such, needs more testing). File names have league name following the year. 
Program will be cleaned up a bit and commited+merged to master (within some time of writing this).
Finally, the program outputs close to 8k lines so if you don't want that, you can comment out/remove all the print lines.
Personally, I like to see what is happening hence I keep it as it is.

16/9/20:
The program reads data(Bundesliga, LaLiga, Serie A, and EPL for the year 2019) from understat, and saves them into a CSV file.
The year can be changed but the 'team' list should also be updated. If the teams are changed according to the corresponding year, results for the said year should be written to the CSV file(not tested).
Note: Team names should correspond to names seen on the website. For example, 'Inter Milan' is simply written as 'Inter'. These changed should be noticed.
The aim, as of today, is to create a points table just as seen in the understat website. Also, better the code.
:)

