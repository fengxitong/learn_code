# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:30:43 2018

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pandas基础介绍
s = pd.Series([1,3,6,np.nan, 44, 1])
print(s)

dates = pd.date_range('20181007', periods = 6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = ['a', 'b', 'c', 'd'])
print(df)

df1 = pd.DataFrame(np.random.randn(12).reshape(3,4))
print(df1)


df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20181007'),
                    'C': pd.Series(1, index = list(range(5)),dtype='float'),
                    'D': np.array([3]*5,dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train",'123']),
                    'F':'foo'})
print(df2)

print(df2.T)

print(df2.sort_index(axis=1, ascending=False))

print(df2.sort_values(by='B'))


#pandas选择数据

# =============================================================================
# dates = pd.date_range('20181007',periods= 6)  #列
# df = pd.DataFrame(np.arange(24).reshape(6,4), # 行
#                   index=dates,columns =['A','B','C','D'])
# print(df)
# 
# 
# print(df.A) #A这一列的数据
# print(df['A'])
# 
# print(df[0:3])  #0---2行
# 
# #根据标签loc来选择数据
# print(df.loc['20181007'])  #行标签  ：代表所有行
# 
# print(df.loc[:,['A','B']])  #[行,列]
# 
# print(df.loc['20181007',['A','B']])
# 
# #根据序列iloc 选择数据
# print(df.iloc[3,1])  #iloc[第几行， 第几]
# print(df.iloc[[1,3,5], 1:3])  #iloc[[1，3，5行]，1到2列]的数据
# print('**********************************')
# 
# #混合选择ix
# print(df.ix[:3,['A','C']])  #0到2行 A C列
# 
# #判断筛选
# 
# print(df[df.A>8])
# 
# 
# =============================================================================


#pandas设置值

# =============================================================================
# dates = pd.date_range('20181007', periods = 6)
# df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B', 'C', 'D'])
# 
# print(df)
# 
# #根据位置设置loc和iloc
# 
# df.iloc[2,2]=1111  #根据位置设置值
# df.loc['20181008','C']=222  #根据标签设置值
# print(df)
# 
# df.B[df.A>6]=0  #根据条件设置值
# print(df)
# 
# #按行列设置
# df['F']=np.nan
# print(df)
# 
# #添加数据
# df['F']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20181007',periods=6))
# print(df)
# =============================================================================


#pandas处理丢失的数据

# =============================================================================
# dates = pd.date_range('20181007', periods = 6)
# df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B', 'C', 'D'])
# df.iloc[0,1]=np.nan
# df.iloc[1,2]=np.nan
# 
# print(df)
# 
# 
# print(df.dropna(
#         axis=0,  #0 对行进行操作 1 对列进行操作
#         how='any'  #‘any’: 只要存在NAN 就drop掉， ‘all’必须全部是NAN才drop
#           ))
# 
# #将Nan用其它值代替
# print(df.fillna(value=0))
# 
# 
# #判断是否有1缺失数据  缺失为True
# 
# print(df.isnull())
# 
# #检测书记中是否存在Nan 如果存在就返回True
# print(np.any(df.isnull())==True)
# =============================================================================

#pandas导入导出数据

# =============================================================================
# data = pd.read_csv('student.csv')
# print(data)
# 
# 
# #将资料存成pickle
# 
# data.to_pickle('student.pickle')
# =============================================================================


#pandas合并concat
# =============================================================================
# 
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
# 
# #concat合并
# res = pd.concat([df1, df2, df3], axis=0)
# 
# print(res)
# 
# #ignore_index 重置索引
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(res)
# 
# 
# 
# #join合并方式
# 
# #定义资料集
# df4 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
# df5 = pd.DataFrame(np.ones((3,4))*1, columns=['c','d','e','f'], index=[2,3,4])
# 
# res = pd.concat([df4,df5], axis=0,  join='outer')  #join 默认outer / inner
# print(res)           #join='outer' 相同的列会被合并到一起，其它列自成一行，没有的位置用Nan 填充
# 
# res = pd.concat([df4,df5], axis=0,  join='inner')  #join='inner' 只用相同的行合并到一起，其他的会被抛弃
# print(res)
# 
# 
# 
# #join_axes(依照axes合并)
# 
# df4 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
# df5 = pd.DataFrame(np.ones((3,4))*1, columns=['c','d','e','f'], index=[2,3,4])
# 
# #依照df1.index进行合并
# res = pd.concat([df4,df5], axis=1, join_axes=[df4.index])
# print(res)
# 
# print('\n***************************************\n')
# res = pd.concat([df4,df5], axis=1)
# print(res)
# 
# 
# 
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
# s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
# 
# res = df1.append(df2, ignore_index=True)
# print(res)
# 
# print('\n')
# 
# res = df1.append([df2,df3],ignore_index=True)
# print(res)
# 
# print('\n')
# 
# res = df1.append(s1, ignore_index=True)
# print(res)
# 
# =============================================================================



#pandas合并merge


# =============================================================================
# #indicator 会将合并的记录放在新的一列
# 
# df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
# df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
# 
# print(df1)
# print(df2)
# 
# 
# res = pd.merge(df1,df2, on='col1', how='outer', indicator='indicator_column')
# print(res)
# 
# res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
# print(res)
# 
# 
# #依据index合并
# 
# left = pd.DataFrame({'A':['A0','A1','A2'],
#                      'B':['B0','B1','B2']}, index=['K0','K1','K2'])
# 
# right = pd.DataFrame({'C':['C0','C1','C2'],
#                       'D':['D0','D1','D2']},index=['K0','K1','K3'])
# 
# print(left)
# print(right)
# 
# res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
# print(res)
# 
# res = pd.merge(left, right, left_index=True, right_index=True,how='inner')
# print(res)
# 
# 
# boys = pd.DataFrame({'K':['K0','K1','K2'],'age':[1,2,3]})
# girls = pd.DataFrame({'K':['K0','K1','K2'],'age':[4,5,6]})
# print(boys)
# print(girls)
# 
# res = pd.merge(boys,girls, on='K',suffixes=['_boy','_girls'],how='inner')
# print(res)
# 
# =============================================================================

#pandas plot出图
# =============================================================================
# 
# data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# 
# data.cumsum()
# 
# data.plot()
# plt.show()
# 
# #DataFrame可视化
# 
# data = pd.DataFrame(np.random.randn(1000,4),
#                     index=np.arange(1000),
#                     columns=list('ABCD'))
# data.cumsum()
# data.plot()
# plt.show()
# 
# ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
# data.plot.scatter(x='A',y='C',color='LightGreen',label='Class1',ax=ax)
# plt.show()
# 
# 
# =============================================================================




























