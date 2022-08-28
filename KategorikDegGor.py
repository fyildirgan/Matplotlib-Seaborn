#Veri Görselleştirme: Matlotlib&Seaborn
#Matplotlib
# Kategorik değişken: sutun grafik. countplot bar
# Sayisal degisken: histogram, boxplot

# Kategorik Degisken Gorsellestirme


df["sex"].value_counts().plot(kind='bar')
print(plt.show())