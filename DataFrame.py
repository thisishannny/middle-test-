import pandas as pd

sr = pd.Series([100, 200, 300, 400])
sr.index = ['A', 'B', 'O', 'AB']
sr

sr1 = pd.Series([10, 20, 30])
sr1

df = pd.DataFrame({'Ű':[170, 180, 175], '������':[65, 78, 70]})
df.index = ['�����̴���', '���ͽ�Ʈ������', '���̾��']
df


df = pd.read_csv('scores.csv', encoding='cp949')
df

df.head()

df.tail()

df.sample(3)

df.info()

df.shape

len(df)

df.isnull().sum()

df_dropna = df.dropna()
df_dropna

df_fillna = df.fillna(50)
df_fillna

df.describe()

df['����'].sum()

df.value_counts('����')

df['����']

df[['����', '����']]

df.loc[1]

df.loc[[1,2,3]]

df.iloc[2]

df.iloc[2:5]

# �������� �ƴ϶� �ε����� ����
df.loc[2:5]

df

df.iloc[1,3]

df.iloc[1:3, 1:3]