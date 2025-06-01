import pandas as pd
from sklearn.preprocessing import LabelEncoder
def preprocessing():
    df = pd.read_csv('/opt/airflow/dags/Flight_data.csv')
    df['duration'] = (df['duration']*3600).round().astype('int64')
    df = df.drop(['flight'],axis=1)
    labelencoder = LabelEncoder()
    df['airline'] = labelencoder.fit_transform(df['airline'])
    df['source_city'] = labelencoder.fit_transform(df['source_city'])
    df['stops'] = labelencoder.fit_transform(df['stops'])
    df['arrival_time'] = labelencoder.fit_transform(df['arrival_time'])
    df['destination_city'] = labelencoder.fit_transform(df['destination_city'])
    df['class'] = labelencoder.fit_transform(df['class'])
    df['departure_time'] = labelencoder.fit_transform(df['departure_time'])
    
    x = df.drop(['price'],axis=1)
    y = df['price']
    return [x,y]


