import sys
from collections import Counter
from io import StringIO
import csv


def top_certified(name):
    # Read in the dataset
    f = open(name, encoding="utf8")
    lines = f.readlines()
    # Find the labels of each column
    labels = lines[0].split(';')
    # Find the column number of STATUS,OCCUPATION_NAME and STATE in case the labels differ in years.
    status_col = labels.index([i for i in labels if 'STATUS' in i][0])
    occupation_col = labels.index([i for i in labels if 'SOC_NAME' in i][0])
    state_col = labels.index([i for i in labels if 'STATE' in i and 'EMPLOYER_STATE' not in i][0])
    # Split the records by ';' using csv and io module
    splitdata = []
    for line in lines[1:]:
        data = StringIO(line)
        reader = csv.reader(data, delimiter=';')
        for row in reader:
            splitdata.append(row)
    # Split the records based on the 'CERTIFIED' flag and only put occupation names in the list
    occupation = [record[occupation_col] for record in splitdata if record[status_col] == 'CERTIFIED']
    states = [record[state_col] for record in splitdata if
              record[status_col] == 'CERTIFIED' and record[state_col != '']]
    # Split the records based on the 'CERTIFIED' flag and only put occupation names in the list
    occupation = [record.split(';')[occupation_col] for record in lines[1:] if
                  record.split(';')[status_col] == 'CERTIFIED' and record.split(';')[occupation_col] != '']
    states = [record.split(';')[state_col] for record in lines[1:] if
              record.split(';')[status_col] == 'CERTIFIED' and record.split(';')[state_col] != '']
    # Count the top 10 occupations, find the names, numbers and percentage, Counter returns a list of tuples.
    count_occ = Counter(occupation).most_common(10)
    top_occ = [i[0] for i in count_occ]
    top_occ_num = [i[1] for i in count_occ]
    percentage_occ = [round(i / len(occupation), 1) for i in top_occ_num]
    print(top_occ)
    print(top_occ_num)
    print(percentage_occ)
    # Count the top 10 states, find the names, numbers and percentage
    count_state = Counter(states).most_common(10)
    top_state = [i[0] for i in count_state]
    top_state_num = [i[1] for i in count_state]
    percentage_state = [round(i / len(states), 1) for i in top_state_num]
    print(top_state)
    print(top_state_num)
    print(percentage_state)
    occ_output = open(sys.argv[2], 'w')
    occ_output.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    state_output = open(sys.argv[3], 'w')
    state_output.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    # Write results to files
    for i in range(10):
        occ_output.write(str(top_occ[i]) + ';' + str(top_occ_num[i]) + ';' + str(percentage_occ[i]) + '%\n')
        state_output.write(str(top_state[i]) + ';' + str(top_state_num[i]) + ';' + str(percentage_state[i]) + '%\n')


top_certified(str(sys.argv[1]))
