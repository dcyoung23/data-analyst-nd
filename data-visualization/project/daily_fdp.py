import os
import urllib
from bs4 import BeautifulSoup
import csv
from datetime import datetime, date, timedelta


def name_scrub(Name):
    # Switch Last, First to First Last
    Name = " ".join(Name.split(", ")[::-1])
    return Name


def team_scrub(Team):
    # Scrub spaces
    Team = Team.strip()

    # Convert to Upper
    Team = Team.upper()
    return Team


def salary_scrub(Salary):
    # Remove $ and , from dollar amount
    Salary = Salary.replace("$", "")
    Salary = Salary.replace(",", "")
    return Salary


def date_text(input):
    # Add zero to single digit date for filenames
    if len(input) == 1:
        output = "0" + input
    else:
        output = input
    return output


def get_fdp(date_input):

    counter = 0
    cols = ["Date", "LeagueID", "Position",
            "Player", "Team", "Opp", "Location",
            "Points", "Salary", "Min"]
    month = str(date_input.month)
    day = str(date_input.day)
    year = str(date_input.year)
    date_output = year + "-" + date_text(month) + "-" + date_text(day)
    # date_output = year + date_text(month) + date_text(day)
    # date_output = date_input

    path = os.getcwd() + "/Files/fdp_" \
                       + year \
                       + date_text(month) \
                       + date_text(day) \
                       + ".csv"

    LeagueID = "fd"

    with open(path, "w") as outfile:
        writer = csv.writer(outfile)
        # Write column headers as the first line
        writer.writerow(cols)

        uri = "http://rotoguru1.com/cgi-bin/hyday.pl?mon=" + month \
              + "&day=" + day \
              + "&year=" + year \
              + "&game=" + LeagueID
        urllines = urllib.urlopen(uri)
        pagedat = urllines.read()
        # print pagedat
        urllines.close()
        soup = BeautifulSoup(pagedat, "html.parser")
        for row in soup.find_all("tr"):
            # values = row.find_all(text=True)
            # values = values[2:]
            tds = row.find_all("td")
            a = row.find_all("a")
            try:
                Position = str(tds[0].get_text())
                Player = str(a[0].get_text())
                Points = str(tds[2].get_text())
                Salary = str(tds[3].get_text())
                Team = str(tds[4].get_text())
                Opp = str(tds[5].get_text())
                Min = str(tds[7].get_text())
            except:
                # print "bad string"
                # time.sleep(20)
                continue
            if Team[:4] != "Team":
                Team = team_scrub(Team)
                Player = name_scrub(Player)
                Salary = salary_scrub(Salary)

                if Opp[:1] == "v":
                    Location = "Home"
                elif Opp[:1] == "@":
                    Location = "Away"
                else:
                    Location = "?"

                Opp = Opp[2:]
                Opp = team_scrub(Opp)

                writer.writerow([date_output, LeagueID, Position,
                                 Player, Team, Opp, Location,
                                 Points, Salary, Min])
                counter += 1

    return counter

if __name__ == "__main__":
    start_date = datetime(2015, 10, 27)
    # start_date = datetime(2016, 02, 01)
    end_date = date.today()
    end_date = datetime.combine(end_date, datetime.min.time())
    while (start_date < end_date):
        counter = get_fdp(start_date)
        start_date += timedelta(days=1)
        print start_date
