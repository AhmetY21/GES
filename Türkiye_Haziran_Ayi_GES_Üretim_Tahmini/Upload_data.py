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


pp = pprint.PrettyPrinter(width=41,depth=6, compact=True)

#Epiaş'dan çektiğim verileri bir klasöre kopyalamıştım. O klasördeki dosyaları birleştiren fonksiyon
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

#Her bir santralin saatlik üretimini maks üretim değerine oranlayan fonksiyon

maksili=[]
for i in range(18):
    maks=float(li[i]['Güneş'].max())
    maksili.append(maks)
    li[i]['Güneş']=li[i]['Güneş'].apply(lambda x: x/maksili[i])


data = pd.concat(li, axis=0, ignore_index=True)

#indexing

data['Tarihsaat']=pd.to_datetime(data['Tarih']+' '+data['Saat'])
data=data.set_index('Tarihsaat')
data

#Hava durumu verisi

wr=pd.read_csv('C:/Users\Ahmet YÜKSEL/Desktop/Algopoly Belgeler/trweather.csv')
wr=wr.rename(columns={"loc": "Yer", "forecast_epoch": "Time", "DSWRF_surface": "Rad","TMP_2.m.above.ground":"Temp"})
wr['Temp']=wr['Temp'].map(lambda x:x-273.15) #Çok önemli bir işlem

