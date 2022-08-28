#Veri Görselleştirme: Matlotlib&Seaborn
#Matplotlib
# Kategorik değişken: sutun grafik. countplot bar
# Sayisal degisken: histogram, boxplot

# Kategorik Degisken Gorsellestirme
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()


df["sex"].value_counts().plot(kind='bar')
print(plt.show())