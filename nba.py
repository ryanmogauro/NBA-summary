import pandas as pd

data = pd.read_csv("nbaNew.csv")


startDate = {
    "ATL": 1968,
    "BOS": 1946,
    "BRK": 1976,
    "CHA": 1988,
    "CHI": 1966,
    "CLE": 1976,
    "DAL": 1980,
    "DEN": 1976,
    "DET": 1957,
    "GSW": 1971,
    "HOU": 1971,
    "IND": 1976,
    "LAC": 1984,
    "LAL": 1960,
    "MEM": 2001,
    "MIA": 1988,
    "MIL": 1968,
    "MIN": 1989,
    "NOP": 2002,
    "NYK": 1946,
    "OKC": 1967,
    "ORL": 1989,
    "PHI": 1963,
    "PHO": 1968,
    "POR": 1970,
    "SAC": 1985,
    "SAS": 1976,
    "TOR": 1995,
    "UTA": 1979,
    "WAS": 1998  
}
nameConvert = {
    "ATL": "Atlanta Hawks",
    "BOS": "Boston Celtics", 
    "BRK": "Brooklyn Nets",
    "CHA": "Charlotte Hornets",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Caveliers",
    "DAL": "Dallas Mavericks",
    "DEN": "Denver Nuggets",
    "DET": "Detroit Pistons",
    "GSW": "Golden State Warriors",
    "HOU": "Houston Rockets",
    "IND": "Indiana Pacers",
    "LAC": "Los Angeles Clippers",
    "LAL": "Los Angeles Lakers",
    "MEM": "Memphis Grizzlies",
    "MIA": "Miami Celtics",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NOP": "New Orleans Pelicans",
    "NYK": "New York Knicks",
    "OKC": "Oklahoma City Thunder",
    "ORL": "Orlando Magic",
    "PHI": "Philadelphia 76ers",
    "PHO": "Phoenix Suns ",
    "POR": "Portland Trailblazers",
    "SAC": "Sacremnto Kings",
    "SAS": "San Antonio Spurs",
    "TOR": "Toronto ",
    "UTA": "Utah Jazz",
    "WAS": "Washington Wizzards" 
}
championships = {
    "ATL": 1,
    "BOS": 17,
    "BRK": 0,
    "CHA": 0,
    "CHI": 6,
    "CLE": 1,
    "DAL": 0,
    "DEN": 0,
    "DET": 3,
    "GSW": 6,
    "HOU": 2,
    "IND": 0,
    "LAC": 0,
    "LAL": 17,
    "MEM": 0,
    "MIA": 3,
    "MIL": 2,
    "MIN": 0,
    "NOP": 0,
    "NYK": 2,
    "OKC": 1,
    "ORL": 0,
    "PHI": 3,
    "PHO": 0,
    "POR": 1,
    "SAC": 1,
    "SAS": 5,
    "TOR": 1,
    "UTA": 0,
    "WAS": 1  
}

#returns the highest single-season value of a given stat ever recorded(i.e. points (PTS))
def overallHigh(type):
    high = 0
    for i in data[type]:
        if i > high:
            high = i
    name = data.loc[data[type] == high, "PlayerName"]
    average = high / (data.loc[data[type] == high, 'G'])
    season = data.loc[data[type] == high, "SeasonStart"]
    return (f"{name} had the most amount of assists in a single NBA season, totalling {high} {type} and averaging {average} points per game during the {season}-{season+1} season")

#returns the highest single-season value of a given stat ever recorded on a specicified team(i.e. points (PTS), Los Angeles Lakers (LAL))
def teamHigh(type, team):
    new = data.loc[data['Tm'] == team]
    high = 0
    for i in new[type]:
        if i > high:
            high = i
    name = new.loc[new[type] == high, "PlayerName"]
    average = high / (new.loc[new[type] == high, 'G'])
    season = new.loc[new[type] == high, "SeasonStart"]
    return (f"{name} had the most amount of assists, out of any {team} players, in a single NBA season, totalling {high} {type} and averaging {average} points per game during the {season}-{season+1} season")

#returns the highest single-season 
def playerHigh(type,name):
    new = data.loc[data["PlayerName"] == name]
    high = 0
    for i in new[type]:
        if i>high:
            high = i
    return high
def playerTotal(type, name):
    new = data.loc[data["PlayerName"] == name]
    total = 0
    for i in new[type]:
        total+=i
    return total
def teamTotal(type, team):
    new = data.loc[data['Tm'] == team]
    total = 0
    for i in new[type]:
        total+=i
    return total

        
    
def teamBio(team):
    highpts = teamHigh("PTS", team)
    highptsplayer = data.loc[data["PTS"] == highpts, "PlayerName"]
    highast = teamHigh("AST", team)
    highastplayer = data.loc[data["AST"] == highpts, "PlayerName"]
    highTRB = teamHigh("TRB", team)
    highTRBplayer = data.loc[data["TRB"] == highpts, "PlayerName"]
    totalPTS = teamTotal("PTS", team)
    totalAST = teamTotal("AST", team)
    totalTRB = teamTotal("TRB", team)
    print(f"The {nameConvert.get(team)} played their first season in {startDate.get(team)} and have won {championships.get(team)} championships since. In their history, their top scorer is {highptsplayer} ({highpts} points) and their top rebounder is {highTRBplayer} (highTRB). The franchise has scored {totalPTS} points, grabbed {totalTRB} rebounds, and recorded {totalAST} assists in their history.")
    
    
def playerBio(namee): 
    maxpts = playerHigh("PTS", namee)
    maxptsyear = data.loc[data["PTS"] == maxpts, "SeasonStart"]
    maxast = playerHigh("AST", namee)
    maxastyear = data.loc[data["AST"] == maxast, "SeasonStart"]
    maxtrb = playerHigh("TRB", namee)
    maxtrbyear = data.loc[data["TRB"] == maxast, "SeasonStart"]
    totalpts = playerTotal("PTS", namee)
    totaltrb = playerTotal("AST", namee)
    totalast = playerTotal("TRB", namee)
    return (f"The most points {namee} has scored in an NBA was {maxpts}, which he did in the {maxptsyear} season. In {maxastyear}, he achieved his career high in assists, totalling {maxast} assists. He reached his career rebound record in {maxtrbyear} with {maxtrb} rebounds. All in all, {namee} scored {totalpts}, recorded {totalast} assists, and grabbed {totaltrb} rebounds in his career. ")
        
print(teamBio("LAL"))





    