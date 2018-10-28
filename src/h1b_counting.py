import sys
import csv
from io import StringIO
from collections import Counter


def top_certified(name):
    # Read in the dataset
    f = open(name, encoding="utf8")
    lines = f.readlines()

    # Find the labels of each column
    labels = lines[0].split(';')
    # Find the column number of STATUS,OCCUPATION_NAME and STATE in case the labels differ in years.
    status_col = labels.index([i for i in labels if 'STATUS' in i][0])
    occupation_col = labels.index([i for i in labels if 'SOC_NAME' in i][0])
    state_col = labels.index(
        [i for i in labels if 'STATE' in i and 'EMPLOYER_STATE' not in i and 'AGENT_ATTORNEY_STATE' not in i][0])

    # Split the records by ';' using csv and io module
    splitdata = []
    for line in lines[1:]:
        data = StringIO(line)
        reader = csv.reader(data, delimiter=';')
        for row in reader:
            splitdata.append(row)

    # Split the records based on the 'CERTIFIED' flag and only put occupation names in the list
    occupation = [record[occupation_col] for record in splitdata if record[status_col] == 'CERTIFIED']
    states = [record[state_col] for record in splitdata if record[status_col] == 'CERTIFIED']

    # Count the top 10 occupations, sort by values then by keys, find the names, numbers and percentage, Counter returns a list of tuples.
    count_occ = dict(Counter(occupation).most_common(10))
    count_occ = sorted(count_occ.items(), key=lambda x: (-x[1], x[0]))
    top_occ = [i[0] for i in count_occ]
    top_occ_num = [i[1] for i in count_occ]
    percentage_occ = [round(i / len(occupation) * 100, 1) for i in top_occ_num]

    # Count the top 10 states, sort by values then by keys, find the names, numbers and percentage
    count_state = dict(Counter(states).most_common(10))
    count_state = sorted(count_state.items(), key=lambda x: (-x[1], x[0]))
    top_state = [i[0] for i in count_state]
    top_state_num = [i[1] for i in count_state]
    percentage_state = [round(i / len(states) * 100, 1) for i in top_state_num]

    # Create results files and write labels to them
    occ_output = open(sys.argv[2], 'w')
    occ_output.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    state_output = open(sys.argv[3], 'w')
    state_output.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    # Write results to files
    for i in range(len(top_occ)):
        occ_output.write(str(top_occ[i]) + ';' + str(top_occ_num[i]) + ';' + str(percentage_occ[i]) + '%\n')
    for i in range(len(top_state)):
        state_output.write(str(top_state[i]) + ';' + str(top_state_num[i]) + ';' + str(percentage_state[i]) + '%\n')


top_certified(str(sys.argv[1]))
