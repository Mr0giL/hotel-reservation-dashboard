import pandas as pd
import numpy as np
from sklearn import preprocessing
lb = preprocessing.LabelEncoder()
df = pd.read_csv('hotel_booking.csv')
df.drop(['name','email','phone-number','credit_card'],axis=1,inplace=True)
df_2 = df
df_2[["reservation_status_day", "reservation_status_month", "reservation_status_year"]] = df["reservation_status_date"].str.split("/", expand = True)
df_2[["reservation_status_day", "reservation_status_month", "reservation_status_year"]] = df_2[["reservation_status_day", "reservation_status_month", "reservation_status_year"]].astype(np.int64)
df_2.drop('reservation_status_date',axis=1,inplace=True)
month_names = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
df_2['arrival_date_month'] = df_2['arrival_date_month'].map(month_names)
df_3 = df_2.select_dtypes('object')
df_3 = df_3.apply(lb.fit_transform)
df_5 = df_3 + 100000
df_4 = df_2
# for col in df_2.select_dtypes('object') :
#     df_2[col] = df_3[col]
for col in df_4.select_dtypes('object') :
    df_4[col] = df_5[col]
# df_2.to_csv('lable encoded.csv')
df_4.to_csv('lable encoded reviewed.csv')











