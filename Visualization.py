# 한글 폰트 처리 : 런타임 다시 시작 필요
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

# matplotlib 한글폰트 지정
plt.rc('font', family='NanumBarunGothic')

# - 기호 깨짐 오류 방지
plt.rc('axes', unicode_minus = False)

# x측
x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]

# 그래프
plt.plot(x,y)
plt.show()

# x측
x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]

# 그래프
plt.plot(x,y, color="blue", marker = 'o', linestyle = ':')
plt.title('월별 평균 온도', fontsize=15)
plt.ylabel('온도(도)')
plt.grid(linestyle = ':')
plt.show()

# 40개의 임의의 랜덤값을 생성
aVal = np.random.standard_normal(40)
aVal

# type 확인
# 40개의 랜덤값으로 이루어진 numpy.ndarray형 변수
type(aVal)

index = range(len(aVal))
plt.plot(index, aVal)

# x축, y축의 범위 설정
plt.xlim(0, 20)
plt.ylim(np.min(aVal) -1, np.max(aVal) + 1)
plt.show()

# index는 range 형 변수
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

# 1번째
plt.figure(figsize=(10,5))
plt.subplot(211)
plt.plot(value[:,0], lw = 1.5, label = '1st')
plt.plot(value[:,0], 'ro')
plt.grid(True)
plt.legend(loc = 0)
plt.ylabel("value")
plt.title('Line Plot 3')
# 2번째
plt.subplot(212)
plt.plot(value[:,1], 'g', lw = 1.5, label = '2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

# 1번째
plt.figure(figsize=(13,5))
plt.subplot(231)
plt.plot(value[:,0], lw= 1.5, label = '1st')
plt.plot(value[:,0], 'co')
plt.grid(True)
plt.legend(loc=0)
plt.ylabel('value')
plt.title('Line Plot 3')
# 2번째
plt.subplot(232)
plt.plot(value[:,0], 'g-.', lw=1.5, label='1st')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# 3번째
plt.subplot(233)
plt.plot(value[:,0], 'g', lw=1.5, label='1st')
plt.plot(value[:,0], 'bD')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# 4번째
plt.subplot(234)
plt.plot(value[:,1], '*', lw=1.5, label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# 5번째
plt.subplot(235)
plt.plot(value[:,1], 'b', lw=1.5, label='2nd')
plt.plot(value[:,1], 'ms')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# 6번째
plt.subplot(236)
plt.plot(value[:,1], 'r--', lw=1.5, label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

# x측
x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]

# 그래프
plt.bar(x,y)
plt.show()

# x측
x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]

# 그래프
plt.bar(x,y)
plt.show()

# x측
x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]

# 그래프
plt.bar(x,y, color="orange", width = 0.5, edgecolor = 'black', hatch = '/')
plt.title('월별 평균 온도', fontsize=15)
plt.ylabel('온도(도)')
plt.grid(linestyle = ':', axis = 'y')
plt.show()

# pandas를 import
import pandas as pd

# score.csv 파일 일기
df = pd.read_csv('scores.csv', encoding='cp949')
df

# pandas를 import
import pandas as pd

# score.csv 파일 일기
df = pd.read_csv('scores.csv', encoding='cp949')
df

x = df['이름']
y_kor = df['국어']
y_eng = df['영어']

# 중심을 기준으로 왼쪽/오른쪽에 그래프를 구성
plt.bar(x, y_kor, width = -0.4, align = 'edge', label = '국어')
plt.bar(x, y_eng, width = 0.4, align = 'edge', label = '영어')
plt.title('국어/영어 점수 비교', fontsize = 15)
plt.ylabel('점수')

# 범례
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