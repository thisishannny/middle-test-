strVal = 'data science'               # ���ڿ� ����
nVal = 12345                          # ������ ����
fVal = 1.2                            # �Ǽ��� ����
lVal = ['data', 'science']            # ����Ʈ
dVal = {'lecture' : 'data science'}   # ��ųʸ�
bVal = True                           # ���� ����(��/����)
# �⺻���� �ּ�
''' 
�̷� ������ �ּ��� ���� ���
'''
strVal
nVal
fVal
lVal
dVal
bVal
print('strVal : ', strVal)
print('nVal : ', nVal)
print('fVal : ', fVal)
print('lVal : ', lVal)
print('dVal : ', dVal)
print('bVal : ', bVal)
print('strVal : ', strVal)
print('nVal : ', nVal)
print('fVal : ', fVal)
print('lVal : ', lVal)
print('dVal : ', dVal)
print('bVal : ', bVal)
'''
���� �������� ���, ���� �����͸� ���
'''
nVal = 16                          # ������ ����
fVal = 3.14                        # �Ǽ��� ����
print('10���� ǥ�� : ', nVal)       # 10����
print('2���� ǥ�� : ', bin(nVal))  # 2����
print('8���� ǥ�� : ', oct(nVal))  # 8����
print('16���� ǥ�� : ', hex(nVal))  # 16����
btVal = True                           # ���� ����(��)
bfVal = False                          # ���� ����(����)
btVal = TRUE                          # ���� ����(��) - ����
bfVal = FALSE                          # ���� ����(����) - ����
btVal = true                          # ���� ����(��) - ����
bfVal = false                          # ���� ����(����) - ����
10 == 11
10 != 11
10 >= 11
10 <= 11
10 > 11
10 < 11
nBig = 100
nSmall = 10
print(nBig == nSmall)
print(nBig != nSmall)
print(nBig >= nSmall)
print(nBig <= nSmall)
print(nBig > nSmall)
print(nBig < nSmall)
print(nBig =< nSmall)     # ����
print(nBig => nSmall)     # ����
strData = 'data'               # ���ڿ� ����
strSci = "Science"             # ���ڿ� ����
strLecture = strData + strSci
strLecture
strLecture = strData +" "+ strSci
strLecture
strLecture.split()              # split()���� ������ �������� ���ڿ� ����
lSeperate = strLecture.split() # split()���� ������ �������� ���ڿ� ���о��� lSeperate ������ ����
type(lSeperate)
strHello = "�ȳ��ϼ���. �ݰ����ϴ�."
strHello.find("�ݰ�")       # ���ڿ��� ã�� ���� find() �Լ��� �̿�
                            # ���ڿ��� ������, ù��° ���� �ε����� ��ȯ
                            strHello.find("hello")    # ���ڿ��� ������, -1�� ����
                            "�ݰ�" in strHello          # in ��ɾ ����Ͽ� Ȯ�� ���� : if ���ǹ����� Ȱ��
                            strHello.replace('.', '?') 
                            strHello.replace('.', '?')  
                            strHello.replace("�ϼ���", "�ϼ���") 
                            strHello 
                            strNewHello = strHello.replace('.', '?')  
                            strNewHello = strNewHello.replace("�ϼ���", "�ϼ���"
                            strNewHello
                            strHello.strip('�ݰ����ϴ�.') 
                            strHello     
lnData = [1,2,3,4,5]     # lnData�� ����Ʈ�� ����
print(lnData)
print('type : ', type(lnData))
print(lnData[0])    # lnData ����Ʈ�� 0�� �ε����� �� ���
print(lnData[3])    # lnData ����Ʈ�� 3�� �ε����� �� ���
lnData[0] = lnData[4]   # lnData[4]�� ���� lnData[0]�� ����
print(lnData)           # lnData ����Ʈ�� ���
print(lnData[2:4])      # lnData[4]�� ����� 5�� ��µ��� ����
lnData = [1,2,3,4,5]
lstrData=['a', 'b', 'c']

# �� ���� ���δٸ� �ڷ����� ���� ����Ʈ�� ����
lnData + lstrData
lnData.append(10)   # 10�� �� �ڿ� �߰�
lnData
lnData.insert(0, 'python')  #'python'���ڿ��� 0�� �ε����� �߰��ϰ�, ���� �ε����� ����� �����ʹ� �ϳ��� �ڷ� �и�(�ε����� +1 �߰�)
lnData
lnData.remove('python')     # 'python' �����͸� ����
lnData
del lnData[5]              # del ��ɾ ���� �ε����� �����Ͽ� ����
lnData
lnData
lnData.pop(0)     # 0�� �ε����� �����͸� ����
lnData
lnData.pop()     # �ε��� ������ ������, ������ �ε����� ���� ����
lnData
lnData.clear()  # ����Ʈ�� ��� �����͸� ����
lnData
# Ʃ���� �⺻ ����
tVal = ("���", "����", "�ٳ���", "�丶��", "Ű��")

print(tVal)
print(type(tVal))
# Ʃ�ÿ� ����� �����ʹ� ������ �Ұ���
tVal[0] = "����"
# count() �Լ��� �̿��Ͽ� Ʃ�ÿ� ����� Ư�� �������� ������ Ȯ��
tData = ( 1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 7)
tData.count(1)
# len()�Լ��� �̿��Ͽ� Ʃ�ÿ� ����� ��ü ������ ������ Ȯ��
len(tVal)
print(tData[2:5])
tTuple = tVal+ tData
print(tTuple)
tData * 2
tData
tData2 = tData * 2
print(tData2)
print("tVal memory = ", hex(id(tVal)))
tVal = tVal * 2
print("tVal memory = ", hex(id(tVal)))
print(tVal)
print("tVal memory = ", hex(id(tVal)))
tVal = tVal + tVal
print("tVal memory = ", hex(id(tVal)))
print(tVal)
sVal = {1, 2, 3, 4, 5}
print(sVal)
print(type(sVal))
sVal[1:2]
# add �Լ��� �̿��Ͽ� �����͸� �߰��� �� ����
sVal.add(100)
print(sVal)
# update �Լ��� �̿��Ͽ� �������� �����͸� �߰��� �� ����
sVal.update([200, 300])
print(sVal)
# remove �Լ��� �̿��Ͽ� �����͸� ������ �� ����
sVal.remove(200)
print(sVal)
# clear() �Լ��� �̿��Ͽ� �����͸� �ʱ�ȭ �� �� ����
sVal.clear()
print(sVal)
sVal = {100, 200, 300, 400, 500}
sData = {"a", "b", "c", "c", 100, 300}
print(sVal)
print(sData)
# intersection() �Լ��� �̿��Ͽ� �������� ���� �� ����
sVal.intersection(sData)
# deference() �Լ��� �̿��Ͽ� �������� ���� �� ����
sVal.difference(sData)
# "-" �����ڷε� ����
sVal - sData
# union() �Լ��� �̿��Ͽ� �������� ���� �� ����
sVal.union(sData)
# "+"�����ڴ� �Ұ���
sVal + sData
# symetric_difference()�� �̿��Ͽ� �����տ��� �������� �� ������ ���� �� ������
sVal.symmetric_difference(sData)
# ��ųʸ� �⺻ ������ ������ ���� ǥ���� �� ����
dVal = {
    'name' : '���İ�',
    'email' : 'computer@hoseo.edu',
    'address' : '�泲 �ƻ��'
}
print(dVal)
print(type(dVal))
dData = {
    "���" : 300, 
    "����" : 200, 
    "��" : 500,
    "Ű��" : 100
}
# Ű�� �̿��� �׸� �˻�
print(dData["��"])
# get() �Լ��� �̿��� �׸� �˻�
dData.get("��")
# ���ο� Ű �߰��� ���� �׸� �߰�
dData["����"] = 100
print(dData)
# pop�� �̿��� �׸� ����
dData.pop("���")
dData
dData.pop()
# sorted �Լ��� �̿��� ����
sorted(dData)
# sorted�� values �Լ��� �̿��Ͽ� ���� ������ �� ����
sorted(dData.values())
# ���� dData�� ��ȭ�� ����
dData
# �Լ� f(x)�� �����ϰ� x ���� �Է����� ����
def f(x):
  # x�� 10�� ���� ���� ���
  return x + 10
f(2)