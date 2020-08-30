import pandas as pd
import numpy as np
import seaborn as sns
import glob
import matplotlib.pyplot as plt
import pprint
pp = pprint.PrettyPrinter(width=41,depth=6, compact=True)

from sklearn.ensemble import RandomForestRegressor


import Rf
from sklearn.metrics import mean_squared_error
import Gesler

#uploading data
pp = pprint.PrettyPrinter(width=41,depth=6, compact=True)

path = r"D:\GES"
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    fl = pd.read_csv(filename, index_col=None, header=0,skipfooter=1,engine='python')
    fl=fl[['Tarih','Saat','Güneş']]
    fl['GES']=str(filename.split('-')[1])
    li.append(fl)

for i in range(18):
   # li[i]['Güneş']=li[i]['Güneş'].apply(lambda x: x.replace(',','.'))#.apply(lambda x: float(x))
    li[i]['Güneş']=li[i]['Güneş'].apply(lambda x: x.replace(',','.'))
    li[i]['Güneş']=li[i]['Güneş'].apply(lambda x: float(x))

maksili=[]
for i in range(18):
    maks=float(li[i]['Güneş'].max())
    maksili.append(maks)
    li[i]['Güneş']=li[i]['Güneş'].apply(lambda x: x/maksili[i])


data = pd.concat(li, axis=0, ignore_index=True)

data['Tarihsaat']=pd.to_datetime(data['Tarih']+' '+data['Saat'])
data=data.set_index('Tarihsaat')
data


wr=pd.read_csv('C:/Users\Ahmet YÜKSEL/Desktop/Algopoly Belgeler/trweather.csv')
wr=wr.rename(columns={"loc": "Yer", "forecast_epoch": "Time", "DSWRF_surface": "Rad","TMP_2.m.above.ground":"Temp"})
wr['Temp']=wr['Temp'].map(lambda x:x-273.15) #convert to celcius
locs=wr['Yer'].unique()

wr1=wr[wr['Yer']==locs[0]]
wr1=wr1.drop('Yer',axis=1)

wr2=wr[wr['Yer']==locs[1]]
wr2=wr2.drop('Yer',axis=1)

wr3=wr[wr['Yer']==locs[2]]
wr3=wr3.drop('Yer',axis=1)

wr4=wr[wr['Yer']==locs[3]]
wr4=wr4.drop('Yer',axis=1)

wr5=wr[wr['Yer']==locs[4]]
wr5=wr5.drop('Yer',axis=1)

wr6=wr[wr['Yer']==locs[5]]
wr6=wr6.drop('Yer',axis=1)

wr7=wr[wr['Yer']==locs[6]]
wr7=wr7.drop('Yer',axis=1)


wr1_train,wr1_test=Gesler.wr_ayar(wr1)

wr2_train,wr2_test=Gesler.wr_ayar(wr2)

wr3_train,wr3_test=Gesler.wr_ayar(wr3)

wr4_train,wr4_test=Gesler.wr_ayar(wr4)

wr5_train,wr5_test=Gesler.wr_ayar(wr5)

wr6_train,wr6_test=Gesler.wr_ayar(wr6)

wr7_train,wr7_test=Gesler.wr_ayar(wr7)
