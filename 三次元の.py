from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import pandas as pd

df = pd.read_excel('散布図.xlsx')

#復旧について
print(df['主成分1(復旧)'])
a = df['主成分1(復旧)']
b = df['主成分2(復旧)']
c = df['主成分3(復旧)']
print(type(a))
a_1 = a[0:32]

a_2 = a[33:39]
a_3 = a[40:55]

b_1 = b[0:32]
b_2 = b[33:39]
b_3 = b[40:55]

c_1 = c[0:32]
c_2 = c[33:39]
c_3 = c[40:55]
print(a_1)

x_1 = a_1.to_numpy()
x_2 = a_2.to_numpy()
x_3 = a_3.to_numpy()
y_1 = b_1.to_numpy()
y_2 = b_2.to_numpy()
y_3 = b_3.to_numpy()
z_1 = c_1.to_numpy()
z_2 = c_2.to_numpy()
z_3 = c_3.to_numpy()

# グラフの枠を作成
fig = plt.figure()
ax = Axes3D(fig)

# X,Y,Z軸にラベルを設定
ax.set_xlabel("主成分1")
ax.set_ylabel("主成分2")
ax.set_zlabel("主成分3")

ax.plot(x_1,y_1,z_1,marker="o",color='red',linestyle='None')
#plt.show()
ax.plot(x_2,y_2,z_2,marker="o",color='green',linestyle='None')
ax.plot(x_3,y_3,z_3,marker="o",color='blue',linestyle='None')

plt.show()