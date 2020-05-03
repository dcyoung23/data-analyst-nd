from pulp import *
import os
import csv


def get_optimal_lineup(input_file):
    reader = csv.DictReader(open(input_file, 'rb'))

    # Read in the csv file
    data = []
    for i, row in enumerate(reader):
        t = {k: v for k, v in row.iteritems()}
        t['id'] = i
        # print t
        if len(t['Points']) > 0 and t['Salary'] != 'N/A':
            data.append(t)

    player_list = []
    output = {}
    budget = 60000
    total_players = 9
    positions = {('PG', ): 2,
                 ('SG', ): 2,
                 ('SF', ): 2,
                 ('PF', ): 2,
                 ('C', ): 1}

    players = [player['id'] for player in data]

    prob = LpProblem("Lineup Optimization", LpMaximize)
    x = LpVariable.dicts(
        'table',
        players,
        lowBound=0,
        upBound=1,
        cat=LpInteger)

    prob += sum([float(player['Points']) * x[player['id']] for player in data])
    prob += sum(
        [float(player['Salary']) * x[player['id']] for player in data]) \
        <= budget
    prob += sum([x[player['id']] for player in data]) == total_players
    for position, num in positions.items():
        prob += sum(
            [x[player['id']] for player in data
             if player['Position'] in position]
            ) >= num

    prob.solve()

    # Print out the LP solution status
    # print("Status:", LpStatus[prob.status])

    salary = 0
    target = 0.0
    if prob.status == 1:
        for player in data:
            if x[player['id']].value() == 1.0:
                player_name = player['Player']
                player_salary = float(player['Salary'])
                player_value = float(player['Points'])
                player_list.append(player_name)
                salary += player_salary
                target += player_value
                # print player_name
    else:
        print "Can't create optimal lineup"

    # Print out results
    output['Players'] = player_list
    output['Salary'] = salary
    output['Points'] = target
    return output

if __name__ == "__main__":
    in_file = os.getcwd() + "/Files/fdp_20160123.csv"
    output = get_optimal_lineup(in_file)
    print output
