# Data-Insight-Coding-Challenge

Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.

The problem here is to generate two files: Top 10 Occupations and Top 10 States for certified visa applications.

Input(test) Dataset

H1B_FY_2014.csv
H1B_FY_2015.csv
H1B_FY_2016.csv

Approach

- Find the labels of all columns of the dataset.
- Locate which column that will be uesd later, i.e. occupation_name, state, status.
- Exploit the csv and io module to parse each rows to extract the imformation. There are many records that have semicolons inside a single cell that are covered in two double quotes, so that the regular spliting method (string.split) won't work well in this case.
- Put the filtered information in a created list and use a Counter to count the number of different soc_name/state that are needed.
- Write the output to new files.

Comments

- I did't put test files inside input folder because I didn't want to push large files to github.
- To run, just put the h1b_input.csv file into input folder and run the run.sh.