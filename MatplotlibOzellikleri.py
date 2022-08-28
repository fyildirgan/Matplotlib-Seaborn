# Matplotlib'in Ozellikleri
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# plot ozelligi: veriyi gorsellistirmek icin kullanılan fonksiyonlardan biri.
x = np.array([1, 8])
y = np.array([0, 150])

#plt.plot(x, y)
#print(plt.show())
#cizgi yerine nokta koymak istersek:
#plt.plot(x, y, 'o')
#print(plt.show())

#z = np.array([2, 4, 6, 8, 10])
#p = np.array([1, 3, 5, 7, 9])
#plt.plot(z, p)
#print(plt.show())

# marker ozelligi
#a = np.array([13, 28, 11, 100])
#plt.plot(a, marker='o')
#print(plt.show())
#markers = [o, *, ., ,, x, X, +, P, s, D, d, p, H, h]

# line ozelligi
#b = np.array([13, 28, 11, 100])
#plt.plot(b, linestyle="dashed", color="r")
#print(plt.show())

# multiple lines
#c = np.array([23, 18, 31, 10])
#d = np.array([13, 28, 11, 100])
#plt.plot(c)
#plt.plot(d)
#print(plt.show())

# Labels
#e = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
#f = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#plt.plot(e, f)
# baslik
#plt.title("bu ana baslik")
# x eksenini isimlendirme
#plt.xlabel("x ekseni isimlendirme")
# y eksenini isimlendirme
#plt.ylabel("y ekseni isimlendirme")
# arka fona izgara koymak istersek
#plt.grid()
#print(plt.show())

# Subplots: birlikte birden fazla gorselin gosterilmesi calismasi

#plot 1
g = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
i = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(g, i)

#plot 2
g1 = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
i1 = np.array([24, 30, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(g1, i1)


#plot 3
g2 = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
i2 = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(g2, i2)
print(plt.show())










