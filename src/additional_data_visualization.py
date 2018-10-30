import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def getocc(name):
    f = pd.read_csv(name,sep=';',index_col=0,header=0)
    labels = list(f.columns)
    if '14' in name:
        certified = f.loc[f['STATUS']=='CERTIFIED']
        top = certified.groupby('LCA_CASE_SOC_NAME').count().sort_values('STATUS',ascending=False)['STATUS'][0:10]
    else:
        certified = f.loc[f['CASE_STATUS']=='CERTIFIED']
        top = certified.groupby('SOC_NAME').count().sort_values('CASE_STATUS',ascending=False)['CASE_STATUS'][0:10]
    top_name = list(top.index)
    top_occ_num = list(top)
    top_occ_num.append(len(certified)-sum(top_occ_num))
    top_name.append('Others')
    print(labels)
    return top_name,top_occ_num


def getstate(name):
    f = pd.read_csv(name,sep=';',index_col=0,header=0)
    labels = list(f.columns)
    if '14' in name:
        certified = f.loc[f['STATUS'] == 'CERTIFIED']
        top = certified.groupby('LCA_CASE_WORKLOC1_STATE').count().sort_values('STATUS',ascending=False)['STATUS'][0:10]
    else:
        certified = f.loc[f['CASE_STATUS'] == 'CERTIFIED']
        top = certified.groupby('WORKSITE_STATE').count().sort_values('CASE_STATUS',ascending=False)['CASE_STATUS'][0:10]
    top_name = list(top.index)
    top_state_num = list(top)
    top_state_num.append(len(certified)-sum(top_state_num))
    top_name.append('Others')
    print(labels)
    return top_name,top_state_num

def pieplot(name,flag):
    if flag==1:
        top_name,top_num = getocc(name)
    else:
        top_name,top_num = getstate(name)

    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','m','r','brown','c','aqua','lightgray','pink']
    explode = [0.2,0,0,0,0,0,0,0,0,0,0]
    plt.pie(top_num,autopct='%1.1f%%',shadow=True,colors=colors,explode=explode)
    plt.axis('equal')

    plt.legend(top_name, loc=1)
    plt.show()

# pieplot('H1B_FY_2016.csv',2)


def getdata(name):
    x = [2014,2015,2016]
    num_cer = []
    num_noncer = []
    for i in x:
        f = pd.read_csv(name + str(i) + '.csv',sep=';',index_col=0,header=0)
        if i ==2014:
            data = len(f.loc[f['STATUS'] == 'CERTIFIED'])
        else:
            data = len(f.loc[f['CASE_STATUS'] == 'CERTIFIED'])

        num_cer.append(data)
        num_noncer.append(len(f)-data)
    ind = np.arange(3)
    fig,ax = plt.subplots()
    ax.bar(ind,num_cer,width=0.2,color='lightskyblue')
    ax.bar(ind+0.2,num_noncer,width=0.2,color='yellowgreen')
    ax.legend(('CERTIFIED','NON-CERTIFIED'))
    ax.set_xticks(ind+0.1)
    ax.set_ylim((0,600000))
    ax.set_xticklabels(('2014','2015','2016'))

    plt.show()

getdata('H1B_FY_')