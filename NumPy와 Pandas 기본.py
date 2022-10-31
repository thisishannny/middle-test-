# 내장함수 예 : input
strText = input("아무 문장이나 입력하세요 : ")
print(strText)

# List를 이용한 다차원 배열
flVal = [1.0, 2.0, 3.14, 4.2, 5.1]  # 실수 list를 생성

# flVal 3개를 리스트로 구성하여 arVal 다차원 배열을 생성
arVal = [flVal, flVal, flVal]
arVal

# arVal은 다차원 배열이므로, arVal[n] 인덱스 연산을 통해 n차원 배열 값을 출력
arVal[0]

arVal[1]

arVal[1][2]

# 1 차원 값을 변환하여 다른 값을 대입 했을때의 다차원 배열
arVal[0] = 'python'
arVal

arVal[0][2]

arVal[0] = 'python programming'
arVal

# numpy 패치지를 import 
import numpy as np
arData = np.array([1.0, 2.0, 3.14, 4.2, 5.1])
arData

# 배열 각 요소의 합을 출력
arData.sum()

arVal.sum()

print(type(arVal))
print(type(arData))

# 배열에 대한 표준편차 출력
arData.std()

# 배열의 누적 합을 출력
arData.cumsum()

arData * 2

arData ** 2 # 2를 제곱

# 루트를 적용한 값을 출력
np.sqrt(arData)

arVal = np.array([arData, arData ** 2])
arVal

arVal.sum(axis=0) # 축(axis)이 0일 경우 세로 축의 합을 출력

arVal.sum(axis=1) # 축(axis)이 0일 경우 가로 축의 합을 출력

# NumPy.array를 사용한 코드
np.array([[0,0,0],[0,0,0]])

# NumPy.zeros를 사용한 코드
arZero = np.zeros((2,3), dtype = 'i') 
arZero

# pandas import
import pandas as pd

pandas_series = pd.Series([30, 20, 10], index=['국어', '영어', '수학'])
print(type(pandas_series))
pandas_series

pandas_series[1:]

pandas_series[0]

pandas_series[0][1]

df = pd.DataFrame([30,20,10], columns=['score'], index=['국어', '영어', '수학'])
df

# DataFrame의 index를 표시
df.index

# DataFrame의 column을 표시
df.columns

# DataFrame의index 중에서 국어에 해당하는 값을 출력
df.loc['국어']   # ix 함수가 최근 제거되어 loc를 써야 동작

# DataFrame의 값을 모두 합한 결과를 출력
df.sum()

# DataFrame의 각 colimn 값의 제곱을 출력
df.score ** 2

# DataFrame에 score2 라는 칼럼을 추가하고 값을 입력
df['score2'] = (50, 50, 50)
df

# DataFrame 함수를 이용하여 column을 추가할 수 있음
df['score2'] = pd.DataFrame([90,90,90], index=['국어', '영어', '수학'])
df

# column 삭제
del df['score']

# index 를 맞추기 않았을 경우
df['score2'] = (90, 90, 90, 100)

# index 를 맞추기 않았을 경우
df['score2'] = pd.DataFrame([90, 90, 90, 100], index=['국어', '영어', '수학', '윤리'])
df

# join() 함수를 이용하여 2개의 DataFrame을 하나로 합칠 수 있음
df1 = pd.DataFrame([1, 2, 3], columns = ['A'])
df2 = pd.DataFrame([10, 11, 12, 13], columns = ['B'])

df = df1.join(df2, how='outer')
df

df_inner = df1.join(df2, how='inner')
df_inner

# 난수를 이용한 임의의 값 생성
df = pd.DataFrame(np.random.randn(5,5))
df.columns = ['A', 'B', 'C', 'D', 'E']

df

# 최대값
df.max()

# 최소값
df.min()

# 평균
df.mean()

# 표준편차
df.std()

# 누적값
df.cumsum()

# DataFrame의 통계적 요약
df.describe()

# Group by를 이용한 DataFrame의 그룹화
df['division'] = ['X', 'Y', 'X', 'Y', 'Z']
df

df.groupby(['division']).mean()