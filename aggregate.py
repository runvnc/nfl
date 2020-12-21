# Read the game stats data
# Add up all of the stats up to that game in the season
# Average them out
# Write to new file


import csv
from dateutil.parser import parse
import datetime


def add(team, key, val):
  print(team,key,val)
  if not home in teams:
      teams[team] = {}
  if not key in teams[home]:
      teams[team][key] = 0
  teams[team][key] += int(val)


with open('nfl_dataset_2002-2019week6.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    prev_dt = datetime.datetime.today()
    season = 0
    week = 1
    teams = {} # {'Giants':{}}

    for row in csv_reader:
        if line_count == 0:
            cols=row
            line_count += 1
        else:
       
            line_count += 1
  
            date,away,home,first_downs_away,first_downs_home,third_downs_away,third_downs_home, \
            fourth_downs_away,fourth_downs_home,passing_yards_away,passing_yards_home,rushing_yards_away, \
            rushing_yards_home,total_yards_away,total_yards_home,comp_att_away,comp_att_home,sacks_away, \
            sacks_home,rushing_attempts_away,rushing_attempts_home,fumbles_away,fumbles_home,int_away,int_home,\
            turnovers_away,turnovers_home,penalties_away,penalties_home,redzone_away,redzone_home,drives_away,\
            drives_home,def_st_td_away,def_st_td_home,possession_away,possession_home,score_away,score_home = row

            dt = parse(date)
            
            if prev_dt == None or dt.month-prev_dt.month>5:
                season += 1
                cleartotals()
                
            print(dt,season,home,away)
            add(home,'first_downs', first_downs_home)
            addgame(home,away)
            prev_dt = dt

print(f'Processed {line_count} lines.')

print(teams['Chargers'])

