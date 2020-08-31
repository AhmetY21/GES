import pandas as pd
import pprint
pp = pprint.PrettyPrinter(width=41,depth=6, compact=True)
import Rf
from sklearn.metrics import mean_squared_error
import Gesler
import Upload_data
#uploading data
pp = pprint.PrettyPrinter(width=41,depth=6, compact=True)

data=Upload_data.data

wr=Upload_data.wr

#Hava durumu verisini lokasyon bazında sınıflandırdım

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

### Buradan tarihi belirliyoruz
train_starter='2020-05-01'
train_stoper='2020-06-01'
test_starter='2020-06-01'
test_stoper='2020-07-01'

dates=pd.date_range(start=train_starter,end=train_stoper,freq='H')

#İstenilen santralin verisini işlenebilir hale getiriyoruz.

train_data_cin,test_data_cin=Gesler.data_prep(data,'CINGILLI',train_starter,train_stoper,test_starter,test_stoper)
train_data_omc,test_data_omc=Gesler.data_prep(data,'OMICRONERCIS',train_starter,train_stoper,test_starter,test_stoper)


#Bu kısımda daha fazla santral toplanılabilir buradaki seçim kriterim en çok üreten ve farklı lokasyonlardan olması şeklinde oldu

train_top=train_data_cin.copy()
train_top['Güneş']=train_data_cin['Güneş']+train_data_omc['Güneş']
test_top=test_data_cin.copy()
test_top['Güneş']=test_data_cin['Güneş']+test_data_omc['Güneş']

#Burada veri setimize saat ve günü de değişken olarak ekliyoruz
wr2_test=Gesler.f_ekle(wr2_test)
train_top=Gesler.f_ekle(train_top)

#Burada Hava durumu verisi ile güneş enerji üretim verisini aynı veri setinde birleştiriyoruz

train_top=pd.merge(train_top,wr2_train,how='outer',left_index=True, right_index=True)
test_top=pd.merge(test_top,wr2_test,how='outer',left_index=True, right_index=True)

x_test,y_test=Gesler.split(test_top)
x_train,y_train=Gesler.split(train_top)

# Test setinin değerlerini kaydediyoruz bura sonra da gelebilirdi

real=test_top['Güneş'].values

#Modelimizi train etmek istediğimiz algoritmayı çağırıyoruz.
# Saat ve gün verisini de ekledikten sonra
# kırılımları olan bir veri setini dönüştüğünü düşündüğümden direk random forest uyguladım diğer algoritmaları da deneyeceğim


Rf.rf_random.fit(x_train, y_train)
preds_rf=Rf.rf_random.predict(wr2_test)

predictions=wr2_test.copy()
predictions['Güneş']=preds_rf

#Algoritma içinde panelize işlemi yapmadığımdan gece yarısında bile cok düşük de olsa bir üretim tahminliyor.
#Bir treshold belirledim onun altını sıfırlıyor.

predictions['Güneş']=predictions['Güneş'].apply(lambda x: 0 if x<0.004 else x)
preds_rf=predictions['Güneş'].values


#Değerimiz de fena gelmiyor
print(mean_squared_error(real, preds_rf))



print("bitti")

