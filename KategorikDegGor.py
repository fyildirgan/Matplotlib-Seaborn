#Veri Görselleştirme: Matlotlib&Seaborn
#Matplotlib
# Kategorik değişken: sutun grafik. countplot bar
# Sayisal degisken: histogram, boxplot

# Kategorik Degisken Gorsellestirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
print(df.head())
df["sex"].value_counts().plot(kind='bar')
print(plt.show())