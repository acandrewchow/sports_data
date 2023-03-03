import requests, sys
from datetime import date
from bs4 import BeautifulSoup

def parse(league, url):
    # receive request
    response = requests.get(url)
    html_content = response.content
    
    # build parser
    soup = BeautifulSoup(html_content, "html.parser")
    teams = soup.find_all("div",class_="Table__Title")

    today = date.today()

    print(f"Injured players for the {league} on {today}:\n")
    for team in teams:
        player_team = team.find(class_="injuries__teamName").text.strip()
        # print(f"{nba_team}")

        # find players associated with team
        player_teams = team.find_next_sibling().find_all(class_="Table__TR--sm")

        # print the associated player for each team
        for player_row in player_teams:
            name = player_row.find(class_="AnchorLink").text.strip()
            position = player_row.find_all("td")[1].text.strip()
            day = player_row.find_all("td")[2].text.strip()
            status = player_row.find_all("td")[3].text.strip()
            update = player_row.find_all("td")[4].text.strip()
            # Print player details
            if (update):
                print(f"{player_team} | {name} | {position} | {day} | {status} \n{update} \n")
            else:
                print(f"{player_team} | {name} | {position} | {day} | {status} \n")

league = sys.argv[1] # extract the league name

# supported leagues via ESPN
if (league == "nba"):
    url = f"https://www.espn.com/{league}/injuries"
    parse(league, url)
elif (league == "nhl"):
    url = f"https://www.espn.com/{league}/injuries"
    parse(league, url)
elif (league == "nfl"):
    url = f"https://www.espn.com/{league}/injuries"
    parse(league, url)
elif (league == "mlb"):
    url = f"https://www.espn.com/{league}/injuries"
    parse(league, url)

