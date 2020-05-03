from optimal_lineup import get_optimal_lineup
import os
import csv


def calc_value(Points, Salary):
    try:
        Points = float(Points)
        Salary = float(Salary)
        Implied_Points = 12.25 + ((Salary-3500)/100.0)*.43622
        Value = Points - Implied_Points
    except:
        Value = 0.0
    return round(Value, 2)


def player_type(Salary):
    try:
        Salary = int(Salary)
        if Salary > 8500:
            PlayerType = 'Star'
        elif Salary < 6000:
            PlayerType = 'Scrub'
        else:
            PlayerType = "Mid-Level"
    except:
        PlayerType = 'Unknown'
    return PlayerType


def final_data():
    counter = 0
    cwd = os.getcwd()
    path = cwd + "/Files"
    output = cwd + "/final_data.csv"

    cols = ["SeasonDay", "Date", "LeagueID", "Position",
            "Player", "Team", "Opp", "Location", "Min",
            "Points", "Salary", "Value", "Optimal", "PlayerType"]

    with open(output, "w") as outfile:
        writer = csv.writer(outfile)
        # Write column headers as the first line
        writer.writerow(cols)
        for f in os.listdir(path):
            input_file = path + "/" + f
            if f.endswith(".csv"):
                counter += 1
                output = get_optimal_lineup(input_file)
                # Get optimal players list
                optimal_players = output['Players']
                # print output
                reader = csv.DictReader(open(input_file, 'rb'))
                for i, row in enumerate(reader):
                    t = {k: v for k, v in row.iteritems()}
                    # print t
                    # Prep data fields
                    Date = t['Date']
                    # print Date
                    LeagueID = t['LeagueID']
                    Position = t['Position']
                    Player = t['Player']
                    Team = t['Team']
                    Opp = t['Opp']
                    Location = t['Location']
                    Min = t['Min']
                    Points = t['Points']
                    Salary = t['Salary']
                    # Calculate value field
                    Value = calc_value(Points, Salary)
                    PlayerType = player_type(Salary)
                    # Create Optimal boolean based on in optimal players list
                    if Player in optimal_players:
                        Optimal = "Yes"
                    else:
                        Optimal = "No"
                    if len(Points) > 0 and Salary != 'N/A' and \
                            Min != 'DNP' and Min != 'NA':
                        writer.writerow([counter, Date, LeagueID, Position,
                                        Player, Team, Opp, Location, Min,
                                        Points, Salary, Value,
                                        Optimal, PlayerType])
                    else:
                        continue
    return counter

if __name__ == "__main__":
    counter = final_data()
    print counter
