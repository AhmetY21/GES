import pandas as pd
import Gesler
def son_iki(df):
    iki=df.iloc[-30*24-2-7:25558-7]
    bir=df.iloc[(-62*24)-3-6:-31*24-2-6]

    return bir,iki

def train_test(df):
    train_start=df.index[(-91*24)-23]
    train_stop=df.index[(-62*24)+25]

    test_start=df.index[(-60*24)-23]
    test_stop=df.index[(-32*24)+25]

    return train_start,train_stop,test_start,test_stop


def ges_ayar(df,starter,stoper):
    A=df['Güneş'].values
    dates=pd.date_range(start=starter,end=stoper,freq='H')  #starter = '2020-05-01' stoper = '2020-06-01'
    z=pd.DataFrame()
    z['Güneş']=A
    z=z.set_index(dates)
    df=z.copy()
    #plt.figure(figsize=(15,4))
    #df['Güneş'].plot()
    return df


def wr_en(weather,ges):
    z=pd.merge(weather,ges,how='outer',left_index=True, right_index=True)
   # print("----------------------------")
    #print(ad)
    #print("----------------------------")
    #pp.pprint(z.corr())
    x=pd.DataFrame(z.corr())
   # plt.figure(figsize=(15,15))
    #sns.heatmap(z.corr(),annot = True,cmap= 'coolwarm', linewidths=3, linecolor='black')
    #print("----------------------------")
    return x


def wr_ayar(df):
    df1,df2=son_iki(df)
    A=df1['Rad'].values
    B=df1['Temp'].values
    C=df2['Rad'].values
    D=df2['Temp'].values
    dates=pd.date_range(start='2020-05-01',end='2020-06-01',freq='H')
    dates2=pd.date_range(start='2020-06-01',end='2020-07-01',freq='H')
    z=pd.DataFrame()
    q=pd.DataFrame()
    z['Rad']=A
    z['Temp']=B
    z=z.set_index(dates)
    q['Rad']=C
    q['Temp']=D
    q=q.set_index(dates2)
    df1=z.copy()
    df2=q.copy()
    ##fig, axs = plt.subplots(2, 2,figsize=(14,10))


    ##axs[0, 0].plot(dates, df1['Rad'])
    ##axs[0, 0].set_title('Training Radyal')
    ##axs[0, 1].plot(dates, df1['Temp'], 'tab:orange')
    ##axs[0, 1].set_title('Training Temp')
    ##axs[1, 0].plot(df2.index, df2['Rad'], 'tab:green')
    ##axs[1, 0].set_title('Test Radyal')
    ##axs[1, 1].plot(df2.index, df2['Temp'], 'tab:red')
    ##axs[1, 1].set_title('Test Temp')

    return df1,df2


def ges_ayar(df,starter,stoper):
    A=df['Güneş'].values
    dates=pd.date_range(start=starter,end=stoper,freq='H')
    z=pd.DataFrame()
    z['Güneş']=A
    z=z.set_index(dates)
    df=z.copy()
    #plt.figure(figsize=(abs15,4))
   # df['Güneş'].plot()
    return df

def split(df):
    #train=pd.concat([test,df]).drop_duplicates(keep=False)
    y_train=df['Güneş'].values

    x_train=df[['Rad', 'Temp', 'Saat', 'Gün']]

    print(y_train.shape)

    print(x_train.shape)

    return x_train,y_train

def f_ekle(df):

    hour=pd.DataFrame(df.index.hour)
    day=pd.DataFrame(df.index.day)

    df['Saat']=hour.values
    df['Gün']=day.values
    return df

def data_prep(data,ad,train_starter,train_stoper,test_starter,test_stoper):
    data_new=data[data['GES']==ad]
    train_start,train_stop,test_start,test_stop=Gesler.train_test(data_new)

    train_data_new=data_new[train_start:train_stop]
    train_data_new=Gesler.ges_ayar(train_data_new,train_starter,train_stoper)

    test_data_new=data_new[test_start:test_stop]
    test_data_new=Gesler.ges_ayar(test_data_new,test_starter,test_stoper)

    return train_data_new,test_data_new
