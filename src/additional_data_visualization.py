import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


#return the top occupations
def getocc(name):
    f = pd.read_csv(name, sep=';', index_col=0, header=0)
    labels = list(f.columns)
    if '14' in name:
        certified = f.loc[f['STATUS'] == 'CERTIFIED']
        top = certified.groupby('LCA_CASE_SOC_NAME').count().sort_values('STATUS', ascending=False)['STATUS'][0:10]
    else:
        certified = f.loc[f['CASE_STATUS'] == 'CERTIFIED']
        top = certified.groupby('SOC_NAME').count().sort_values('CASE_STATUS', ascending=False)['CASE_STATUS'][0:10]
    top_name = list(top.index)
    top_occ_num = list(top)
    top_occ_num.append(len(certified) - sum(top_occ_num))
    top_name.append('Others')
    print(labels)
    return top_name, top_occ_num


#return the top states
def getstate(name):
    f = pd.read_csv(name, sep=';', index_col=0, header=0)
    labels = list(f.columns)
    if '14' in name:
        certified = f.loc[f['STATUS'] == 'CERTIFIED']
        top = certified.groupby('LCA_CASE_WORKLOC1_STATE').count().sort_values('STATUS', ascending=False)['STATUS'][
              0:10]
    else:
        certified = f.loc[f['CASE_STATUS'] == 'CERTIFIED']
        top = certified.groupby('WORKSITE_STATE').count().sort_values('CASE_STATUS', ascending=False)['CASE_STATUS'][
              0:10]
    top_name = list(top.index)
    top_state_num = list(top)
    top_state_num.append(len(certified) - sum(top_state_num))
    top_name.append('Others')
    print(labels)
    return top_name, top_state_num


#plot pie plot for each occupation/state
def pieplot(name, flag):
    if flag == 1:
        top_name, top_num = getocc(name)
    else:
        top_name, top_num = getstate(name)

    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'm', 'r', 'brown', 'c', 'aqua', 'lightgray', 'pink']
    explode = [0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    plt.pie(top_num, autopct='%1.1f%%', shadow=True, colors=colors, explode=explode)
    plt.axis('equal')

    plt.legend(top_name, loc=1)
    plt.show()


# pieplot('H1B_FY_2016.csv',2)

#plot the number of certified and non-certified VISAs for each year
def ifcerbars(name):
    x = [2014, 2015, 2016]
    num_cer = []
    num_noncer = []
    for i in x:
        f = pd.read_csv(name + str(i) + '.csv', sep=';', index_col=0, header=0)
        if i == 2014:
            data = len(f.loc[f['STATUS'] == 'CERTIFIED'])
        else:
            data = len(f.loc[f['CASE_STATUS'] == 'CERTIFIED'])

        num_cer.append(data)
        num_noncer.append(len(f) - data)
    ind = np.arange(3)
    fig, ax = plt.subplots()
    ax.bar(ind, num_cer, width=0.2, color='lightskyblue')
    ax.bar(ind + 0.2, num_noncer, width=0.2, color='yellowgreen')
    ax.set_title('Number of Certified and Non-Certified Visas by Year')
    ax.legend(('CERTIFIED', 'NON-CERTIFIED'))
    ax.set_xticks(ind + 0.1)
    ax.set_ylim((0, 600000))
    ax.set_xticklabels(('2014', '2015', '2016'))

    plt.show()


# ifcerbars('H1B_FY_')


#plot the approved working start quarters for each year
def plotquarters(name):
    x=[2014,2015,2016]
    years = []
    for i in x:
        print(i)
        f = pd.read_csv(name +str(i)+'.csv', sep=';', index_col=0, header=0)
        if i==2014:
            certified = f.loc[f['STATUS'] == 'CERTIFIED']
            date = "LCA_CASE_EMPLOYMENT_START_DATE"
            certified["Q"] = 0
            certified["L"] = certified[date].apply(lambda x: len(str(x).split("-")))
            certified = certified.loc[certified["L"] != 1]
            certified.loc[certified[date].apply(lambda x: x.split("-")[1]).isin(["01", "02", "03"]), "Q"] = 1
            certified.loc[certified[date].apply(lambda x: x.split("-")[1]).isin(["04", "05", "06"]), "Q"] = 2
            certified.loc[certified[date].apply(lambda x: x.split("-")[1]).isin(["07", "08", "09"]), "Q"] = 3
            certified.loc[certified[date].apply(lambda x: x.split("-")[1]).isin(["10", "11", "12"]), "Q"] = 4
            quarters = list(certified.groupby('Q').count()['LCA_CASE_EMPLOYMENT_START_DATE'])
        elif i==2015:
            certified = f.loc[f['CASE_STATUS'] == 'CERTIFIED']
            date = "EMPLOYMENT_START_DATE"
            certified["Q"] = 0
            certified["L"] = certified[date].apply(lambda x: len(str(x).split("/")))
            certified = certified.loc[certified["L"] ==3]
            certified.loc[certified[date].apply(lambda x: x.split("/")[0]).isin(["01", "02", "03"]), "Q"] = 1
            certified.loc[certified[date].apply(lambda x: x.split("/")[0]).isin(["04", "05", "06"]), "Q"] = 2
            certified.loc[certified[date].apply(lambda x: x.split("/")[0]).isin(["07", "08", "09"]), "Q"] = 3
            certified.loc[certified[date].apply(lambda x: x.split("/")[0]).isin(["10", "11", "12"]), "Q"] = 4
            quarters = list(certified.groupby('Q').count()['EMPLOYMENT_START_DATE'])[1:]
        else:
            certified = f.loc[f['CASE_STATUS'] == 'CERTIFIED']
            date = "EMPLOYMENT_START_DATE"
            certified["Q"] = 0
            certified["L"] = certified[date].apply(lambda x: len(str(x).split("-")))
            certified = certified.loc[certified["L"] != 1]
            certified.loc[certified[date].apply(lambda x: x.split("-")[1]).isin(["01", "02", "03"]), "Q"] = 1
            certified.loc[certified[date].apply(lambda x: x.split("-")[1]).isin(["04", "05", "06"]), "Q"] = 2
            certified.loc[certified[date].apply(lambda x: x.split("-")[1]).isin(["07", "08", "09"]), "Q"] = 3
            certified.loc[certified[date].apply(lambda x: x.split("-")[1]).isin(["10", "11", "12"]), "Q"] = 4
            quarters = list(certified.groupby('Q').count()['EMPLOYMENT_START_DATE'])
        print(quarters)
        years.append(quarters)
    ax = plt.axes()
    mark = ['+','.','x']
    for i in range(3):
        ax.plot([1,2,3,4],years[i],mark[i],markersize=10)
    ax.set_title('Approved Working Start Quarter of Years')
    ax.set_xticks((1,2,3,4))
    ax.set_xticklabels(['Quarter I','Quarter II','Quarter III','Quarter IV'])
    ax.legend(('2014','2015','2016'))
    plt.show()


# plotquarters('H1B_FY_')
