# �����Լ� �� : input
strText = input("�ƹ� �����̳� �Է��ϼ��� : ")
print(strText)

# List�� �̿��� ������ �迭
flVal = [1.0, 2.0, 3.14, 4.2, 5.1]  # �Ǽ� list�� ����

# flVal 3���� ����Ʈ�� �����Ͽ� arVal ������ �迭�� ����
arVal = [flVal, flVal, flVal]
arVal

# arVal�� ������ �迭�̹Ƿ�, arVal[n] �ε��� ������ ���� n���� �迭 ���� ���
arVal[0]

arVal[1]

arVal[1][2]

# 1 ���� ���� ��ȯ�Ͽ� �ٸ� ���� ���� �������� ������ �迭
arVal[0] = 'python'
arVal

arVal[0][2]

arVal[0] = 'python programming'
arVal

# numpy ��ġ���� import 
import numpy as np
arData = np.array([1.0, 2.0, 3.14, 4.2, 5.1])
arData

# �迭 �� ����� ���� ���
arData.sum()

arVal.sum()

print(type(arVal))
print(type(arData))

# �迭�� ���� ǥ������ ���
arData.std()

# �迭�� ���� ���� ���
arData.cumsum()

arData * 2

arData ** 2 # 2�� ����

# ��Ʈ�� ������ ���� ���
np.sqrt(arData)

arVal = np.array([arData, arData ** 2])
arVal

arVal.sum(axis=0) # ��(axis)�� 0�� ��� ���� ���� ���� ���

arVal.sum(axis=1) # ��(axis)�� 0�� ��� ���� ���� ���� ���

# NumPy.array�� ����� �ڵ�
np.array([[0,0,0],[0,0,0]])

# NumPy.zeros�� ����� �ڵ�
arZero = np.zeros((2,3), dtype = 'i') 
arZero

# pandas import
import pandas as pd

pandas_series = pd.Series([30, 20, 10], index=['����', '����', '����'])
print(type(pandas_series))
pandas_series

pandas_series[1:]

pandas_series[0]

pandas_series[0][1]

df = pd.DataFrame([30,20,10], columns=['score'], index=['����', '����', '����'])
df

# DataFrame�� index�� ǥ��
df.index

# DataFrame�� column�� ǥ��
df.columns

# DataFrame��index �߿��� ��� �ش��ϴ� ���� ���
df.loc['����']   # ix �Լ��� �ֱ� ���ŵǾ� loc�� ��� ����

# DataFrame�� ���� ��� ���� ����� ���
df.sum()

# DataFrame�� �� colimn ���� ������ ���
df.score ** 2

# DataFrame�� score2 ��� Į���� �߰��ϰ� ���� �Է�
df['score2'] = (50, 50, 50)
df

# DataFrame �Լ��� �̿��Ͽ� column�� �߰��� �� ����
df['score2'] = pd.DataFrame([90,90,90], index=['����', '����', '����'])
df

# column ����
del df['score']

# index �� ���߱� �ʾ��� ���
df['score2'] = (90, 90, 90, 100)

# index �� ���߱� �ʾ��� ���
df['score2'] = pd.DataFrame([90, 90, 90, 100], index=['����', '����', '����', '����'])
df

# join() �Լ��� �̿��Ͽ� 2���� DataFrame�� �ϳ��� ��ĥ �� ����
df1 = pd.DataFrame([1, 2, 3], columns = ['A'])
df2 = pd.DataFrame([10, 11, 12, 13], columns = ['B'])

df = df1.join(df2, how='outer')
df

df_inner = df1.join(df2, how='inner')
df_inner

# ������ �̿��� ������ �� ����
df = pd.DataFrame(np.random.randn(5,5))
df.columns = ['A', 'B', 'C', 'D', 'E']

df

# �ִ밪
df.max()

# �ּҰ�
df.min()

# ���
df.mean()

# ǥ������
df.std()

# ������
df.cumsum()

# DataFrame�� ����� ���
df.describe()

# Group by�� �̿��� DataFrame�� �׷�ȭ
df['division'] = ['X', 'Y', 'X', 'Y', 'Z']
df

df.groupby(['division']).mean()