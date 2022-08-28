# Seaborn
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
print(df.head())
df["sex"].value_counts()
sns.countplot(x=df["sex"], data =df)

#df['sex'].value_counts().plot(kind='bar') - matplotlib
#print(plt.show())

# Sayisal degisken Gorsellestirme

sns.boxplot(x=df["total_bill"])
print(plt.show())

#df["total_bill"].hist() - pandas fonksiyonu
#print(plt.show())

