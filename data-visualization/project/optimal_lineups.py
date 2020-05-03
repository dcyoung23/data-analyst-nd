import os
import csv
from dkp_optimal_lineup import get_optimal_lineup


input_file = os.getcwd() + "/Files/dkp_2016_1.csv"
reader = csv.DictReader(open(input_file, 'rb'))

# Read in the csv file
flex = ['RB', 'WR', 'TE']
data = []
player_lock = []
for i, row in enumerate(reader):
    t = {k: v for k, v in row.iteritems()}
    t['id'] = i
    player_lock.append(t['Player'])
    for f in flex:
        output = get_optimal_lineup(input_file, f, player_lock)
        data.append(output)

print data
