# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:01:11 2019

@author: ougs
"""
import matplotlib.pyplot as plt
import pandas as pd

df=open('E:\python文件\量化投资以python为工具数据文件\平安银行昨收价.csv')
dataset=pd.read_csv(df)
df.close()

#收益率直方图
returns=dataset.ix[:,'return']
plt.hist(returns)

'''数据的位置'''
#求平均数
returns.mean()

#求中位数
returns.median()
#求众数
returns.mode()

#上下四分位数
[returns.quantile(i) for i in [0.25,0.5,0.75]]


'''数据的离散度'''
#极差=最大值-最小值
returns.max()-returns.min()

#平均绝对偏差（mean absolute deviation
returns.mad()

#方差和标准差
returns.var()
returns.std()


