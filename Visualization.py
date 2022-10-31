# �ѱ� ��Ʈ ó�� : ��Ÿ�� �ٽ� ���� �ʿ�
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

# matplotlib �ѱ���Ʈ ����
plt.rc('font', family='NanumBarunGothic')

# - ��ȣ ���� ���� ����
plt.rc('axes', unicode_minus = False)

# x��
x = ['1��', '2��', '3��', '4��', '5��']
y = [7, 10, 17, 20, 23]

# �׷���
plt.plot(x,y)
plt.show()

# x��
x = ['1��', '2��', '3��', '4��', '5��']
y = [7, 10, 17, 20, 23]

# �׷���
plt.plot(x,y, color="blue", marker = 'o', linestyle = ':')
plt.title('���� ��� �µ�', fontsize=15)
plt.ylabel('�µ�(��)')
plt.grid(linestyle = ':')
plt.show()

# 40���� ������ �������� ����
aVal = np.random.standard_normal(40)
aVal

# type Ȯ��
# 40���� ���������� �̷���� numpy.ndarray�� ����
type(aVal)

index = range(len(aVal))
plt.plot(index, aVal)

# x��, y���� ���� ����
plt.xlim(0, 20)
plt.ylim(np.min(aVal) -1, np.max(aVal) + 1)
plt.show()

# index�� range �� ����
type(index)

plt.figure(figsize=(7,4))
plt.plot(aVal.cumsum(), 'b', lw= 1.5)
plt.plot(aVal.cumsum(), 'ro')
plt.xlabel('index')
plt.ylabel('aVal')
plt.title('Line Plot')
plt.show()

value = np.random.standard_normal((30, 2))
value

value[0]

plt.figure(figsize=(10,4))
plt.plot(value[:,0], lw= 1.5)
plt.plot(value[:,1], lw= 1.5)
plt.plot(value, 'ro')
plt.grid(True)
# plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('Line Plot')

# 1��°
plt.figure(figsize=(10,5))
plt.subplot(211)
plt.plot(value[:,0], lw = 1.5, label = '1st')
plt.plot(value[:,0], 'ro')
plt.grid(True)
plt.legend(loc = 0)
plt.ylabel("value")
plt.title('Line Plot 3')
# 2��°
plt.subplot(212)
plt.plot(value[:,1], 'g', lw = 1.5, label = '2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

# 1��°
plt.figure(figsize=(13,5))
plt.subplot(231)
plt.plot(value[:,0], lw= 1.5, label = '1st')
plt.plot(value[:,0], 'co')
plt.grid(True)
plt.legend(loc=0)
plt.ylabel('value')
plt.title('Line Plot 3')
# 2��°
plt.subplot(232)
plt.plot(value[:,0], 'g-.', lw=1.5, label='1st')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# 3��°
plt.subplot(233)
plt.plot(value[:,0], 'g', lw=1.5, label='1st')
plt.plot(value[:,0], 'bD')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# 4��°
plt.subplot(234)
plt.plot(value[:,1], '*', lw=1.5, label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# 5��°
plt.subplot(235)
plt.plot(value[:,1], 'b', lw=1.5, label='2nd')
plt.plot(value[:,1], 'ms')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# 6��°
plt.subplot(236)
plt.plot(value[:,1], 'r--', lw=1.5, label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

# x��
x = ['1��', '2��', '3��', '4��', '5��']
y = [7, 10, 17, 20, 23]

# �׷���
plt.bar(x,y)
plt.show()

# x��
x = ['1��', '2��', '3��', '4��', '5��']
y = [7, 10, 17, 20, 23]

# �׷���
plt.bar(x,y)
plt.show()

# x��
x = ['1��', '2��', '3��', '4��', '5��']
y = [7, 10, 17, 20, 23]

# �׷���
plt.bar(x,y, color="orange", width = 0.5, edgecolor = 'black', hatch = '/')
plt.title('���� ��� �µ�', fontsize=15)
plt.ylabel('�µ�(��)')
plt.grid(linestyle = ':', axis = 'y')
plt.show()

# pandas�� import
import pandas as pd

# score.csv ���� �ϱ�
df = pd.read_csv('scores.csv', encoding='cp949')
df

# pandas�� import
import pandas as pd

# score.csv ���� �ϱ�
df = pd.read_csv('scores.csv', encoding='cp949')
df

x = df['�̸�']
y_kor = df['����']
y_eng = df['����']

# �߽��� �������� ����/�����ʿ� �׷����� ����
plt.bar(x, y_kor, width = -0.4, align = 'edge', label = '����')
plt.bar(x, y_eng, width = 0.4, align = 'edge', label = '����')
plt.title('����/���� ���� ��', fontsize = 15)
plt.ylabel('����')

# ����
plt.legend() 
plt.show()

value = np.random.standard_normal((500,2))
plt.plot(value[:,0], value[:,1], 'ro')
plt.grid(False)
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 1')

plt.figure(figsize=(7,5))
plt.scatter(value[:,0], value[:,1], marker='o')
plt.grid(True)
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 2')

color = np.random.randint(0,10,len(value))

plt.figure(figsize=(10,5))
plt.scatter(value[:,0], value[:,1], c=color, marker = 'o')
plt.colorbar()
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 3')

import seaborn as sns
df = sns.load_dataset('tips')
df

df.head()

df.describe()

df.info()

x = df['total_bill']
y = df['tip']

sns.scatterplot(x,y)

sns.boxplot(x="day", y = "tip", hue="sex", data=df, palette="muted")