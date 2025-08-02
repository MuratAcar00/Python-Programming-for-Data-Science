import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt                    
                    
                    
                    ### VERİ GÖRSELLEŞTİRME (MATPLOTLIB & SEABORN) ###


    #MATPLOTLIB (LOW LEVEL)

#Kategorik Değişken: Sütun grafiği ile görselleştirilir. Seaborn'da countplot fonksiyonu kullanılarak yapılırken Matplotlib'da barplot kullanılır

#Sayısal Değişken: hist, boxplot


#KATEGORİK DEĞİŞKEN GÖRSELLEŞTİRME:

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

#Cinsiyet dağılımını sütun grafiği şeklinde görselleştiren fonksiyon
df["sex"].value_counts().plot(kind = "bar")
plt.show()


#SAYISAL DEĞİŞKEN GÖRSELLEŞTİRME:


#Histogram Grafiği:

plt.hist(df["age"])
plt.show()

#Box(Kutu) Grafiği
plt.boxplot(df["fare"])
plt.show()


 #Matplotlib'ın Özellikleri


    #plot:

#1. Örnek:
x = np.array([1, 8])
y = np.array([0, 150])

#Çizgi grafiği
plt.plot(x, y)
plt.show()

#Nokta grafiği
plt.plot(x, y, "o")
plt.show()


#2. Örnek:
x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

#Çizgi grafiği
plt.plot(x, y)
plt.show()

#Nokta grafiği
plt.plot(x, y, "o")
plt.show()


    #marker:

y = np.array([13, 28, 11, 100])

plt.plot(y, marker = "o")
plt.show()


plt.plot(y, marker = "*")
plt.show()


    #line:

y = np.array([13, 28, 11, 100])

plt.plot(y)
plt.show()

plt.plot(y, linestyle = "dashdot", color = "r")
plt.show()


    #Multiple Lines:

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)
plt.show()



    #Labels:

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.show()

#Title:
plt.title("Bu ana başlık")

# X ve Y Ekseni İsimlendirmesi:

plt.xlabel("X ekseni")

plt.ylabel("Y ekseni")

#Izgara Ekleme:

plt.grid()

plt.show()


    #Subplots: Birden Fazla Görselin Aynı Anda Gösterilmesi

#plot 1

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)    #1'e 2'lik bir tablo olustur bu 1.tablomuz
plt.title("1")
plt.plot(x, y)

#plot 2

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 2)    #1'e 3'lük bir tablo olustur bu 2.tablomuz
plt.title("2")
plt.plot(x, y)

#plot 3

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)    #1'e 3'lük bir tablo olustur bu 3.tablomuz
plt.title("3")
plt.plot(x, y)

plt.show()



    ### SEABORN (HİGH LEVEL)

df = sns.load_dataset("tips")
df.head()

#seaborn ile sütun grafiği

df["sex"].value_counts()
sns.countplot(x = df["sex"], data = df)
plt.show()

#matplotlib ile sütun grafiği

df["sex"].value_counts().plot(kind = "bar")
plt.show()

#Seaborn ile Sayısal Değişken Görselleştirme:

sns.boxplot(x = df["total_bill"])
plt.show()

#Pandas ile Histogram Grafiği

df["total_bill"].hist()
plt.show()
