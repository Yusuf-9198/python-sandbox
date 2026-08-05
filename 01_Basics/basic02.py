# from basic01 import sum

# sum(5,6)
# Measure of central tendency
# Mean
age = [12, 45, 32,45, 43, 23, 46]
import numpy as np
print(np.mean(age))
print(np.median(age))

# import seaborn as sns
# df = sns.load_dataset('tip')
# df.head()
# np.mean(df['total_bill'])
# print(sns.histplot(age,kde=True))

# measure of dispersion
print(np.var(age))
print(np.std(age))

# import panda as pd
# data = [[10,12,34],[2,45,67],[43,6,11]]
# df = pd.DataFrame(data,columns=["A","B","C"])
# print(df.head())

