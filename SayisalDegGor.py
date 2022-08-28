# Sayisal Degisken Gorsellestirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
print(df.head())
# plt.hist(df["age"])
# print(plt.show())
plt.boxplot(df["fare"])
print(plt.show())
