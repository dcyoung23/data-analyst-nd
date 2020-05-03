import csv
import pandas as pd


def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. 
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        f_in = open(name, 'r')
        new_name = 'updated_' + name
        f_out = open(new_name,'w')

        reader_in = csv.reader(f_in, delimiter = ',')
        writer_out = csv.writer(f_out, delimiter = ',')

        # 8 fields per batch
        # First 3 fields per line need to repeat per new line

        for line in reader_in:
            first_part_of_line = [line[0],line[1],line[2]]

            line_len = len(line)
            current_part_of_line = []
            for i in range(3,line_len):
                current_part_of_line.append(line[i])

                #print len(current_part_of_line)
                #print current_part_of_line
                
                # If Current Part of Line is 5 then start next batch
                if len(current_part_of_line) == 5:
                    writer_out.writerow(first_part_of_line + current_part_of_line)
                    # Start new Current Part of Line
                    current_part_of_line = []


if __name__ == "__main__":
    input_files = ['turnstile_110528.txt', 'turnstile_110604.txt']
    fix_turnstile_data(input_files)


'''
import urllib

url = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt'

urllib.urlretrieve(url, "turnstile_110507.txt")

f_in = open('turnstile_110528.txt', 'r')
f_out = open('updated_turnstile_110528.txt','w')

reader_in = csv.reader(f_in, delimiter = ',')
writer_out = csv.writer(f_out, delimiter = ',')

#reader_in.next()

# 8 fields per batch
# First 3 fields per line need to repeat per new line
# Varying number of batches per line
# Total fields per line - 3 / 5 equals number of batches per line


for line in reader_in:
    first_part_of_line = [line[0],line[1],line[2]]

    line_len = len(line)
    current_part_of_line = []
    for i in range(3,line_len):
        # If Current Part of Line is 5 then start next batch
        if len(current_part_of_line) == 5:
            writer_out.writerow(first_part_of_line + current_part_of_line)
            current_part_of_line = []

        current_part_of_line.append(line[i])
'''

