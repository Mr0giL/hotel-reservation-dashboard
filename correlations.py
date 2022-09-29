import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# df = pd.read_csv('lable encoded.csv')
# corrs = df.corr()
# corrs.to_excel('cors.xlsx')
dfs = pd.read_csv('lable encoded + seasons.csv')
corrss = dfs.corr()
corrss.to_excel('corss.xlsx')
# a = plt.figure(figsize=(90,32))
# plt.figure(figsize=(90,32))
# sns.heatmap(df.corr(),annot=True,cmap='Blues',center= 0)
# plt.savefig('out')