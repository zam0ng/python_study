import pandas as pd

df1 = pd.read_csv("C:/Users/cso/Desktop/test/test.csv", encoding='cp949')
print(df1.shape)
print(df1['날짜'])
print(pd.to_datetime((df1['날짜'])))

df1['날짜_datatime'] = pd.to_datetime(df1['날짜'])
print(df1.shape)
df1['날짜_연도'] = df1['날짜_datatime'].dt.year
print("------날짜연도--------")
print(df1['날짜_연도'])
print(df1.head())
print(df1.tail(2))

filterd_df = df1[df1['날짜_연도'] == 2019]['날짜'].unique().tolist()
print('---------')
print(filterd_df)

def print_test():
    print(df1['날짜_연도'][0])
    print('---------')

    print(list(df1['날짜_연도']))
    # newArr = [for i in list(df1['날짜_연도'])]

print_test()