import pandas as pd
from matplotlib import pyplot as plt


def getdata(name):
    f = pd.read_csv(name,sep=';',index_col=0,header=0)
    labels = list(f.columns)
    top = f.loc[f['STATUS']=='CERTIFIED'].groupby('LCA_CASE_SOC_NAME').count().sort_values('STATUS',ascending=False)['STATUS'][0:10]
    top_name = list(top.index)
    top_occ_num = list(top)
    top_occ_num.append(len(f.loc[f['STATUS']=='CERTIFIED'])-sum(top_occ_num))
    top_name.append('Others')
    print(labels)
    return top_name,top_occ_num


def pieplot(name):
    top_name,top_num = getdata(name)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','m','r','brown','c','aqua','lightgray','pink']
    explode = [0.2,0,0,0,0,0,0,0,0,0,0]
    plt.pie(top_num,autopct='%1.1f%%',shadow=True,colors=colors,explode=explode)
    plt.axis('equal')

    plt.legend(top_name, loc=1)
    plt.show()

pieplot('H1B_FY_2014.csv')
# getdata('H1B_FY_2014.csv')