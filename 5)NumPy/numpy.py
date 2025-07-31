import numpy as np

                    ### PYTHON İLE VERİ ANALİZİ ( DATA ANALYSIS WITH PYTHON ) ###

#Numpy
#Pandas
#Veri Görselleştirme: Matploit & Seaborn
#Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)


            ### NUMPY

#Neden NumPy? (Why NumPy?)
#NumPy Array'i Oluşturmak (Creating NumPy Arrays)
#NumPy Array Özellikleri (Attributes of NumPy Arrays)
#Yeniden Şekillendirme (Reshaping)
#Index Seçimi (Index Selection)
#Slicing
#Fancy Index
#NumPy'da Koşullu İşlemler (Condition on NumPy)
#Matematiksel İşlemler (Mathematical Operations)


            ###Neden NumPy? (Why NumPy?)

#İki listeyi çarpma
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

#Without numpy

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
print(ab)

#With numpy

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a * b


#NumPy Array'i Oluşturmak (Creating NumPy Arrays)

np.array([1, 2, 3, 4, 5])

np.zeros(10, dtype = int)   #Girdiğiniz sayı kadar 0 içeren array olusturan fonksiyon

np.random.randint(0, 10, size = 10) # Verdiğimiz aralıklarda istediğimiz adetde rastgele sayılar üreten fonksiyon

np.random.normal(10, 4, (3, 4)) #Ortalaması 10, standart sapması 4, 3'e 4'lük bir array olusturan fonksiyon


            ###NumPy Array Özellikleri (Attributes of NumPy Arrays)

#ndim: Boyut sayısı
#shape: Boyut bilgisi
#size: Toplam eleman sayısı
#dtype: Array veri tipi

a = np.random.randint(10, size = 5)

a.ndim

a.shape

a.size

a.dtype


            ###Yeniden Şekillendirme (Reshaping)

#Tek boyutlu arrayi 3 boyutluya cevırme
np.random.randint(1, 10, size = 9)

np.random.randint(1, 10, size = 9).reshape(3, 3)

#Farklı yolu
ar = np.random.randint(1, 10, size = 9)

ar.reshape(3,3)

#Burada hata almamızın sebebı 10 elemanlık bir arrayi 3'e 3'lük bir şekilde çevrilememesi
np.random.randint(1, 10, size = 10).reshape(3, 3)


            ###Index Seçimi (Index Selection)

a = np.random.randint(10, size =  10)

a[0]
a[0:5] #slicing

a[0] = 999

b = np.random.randint(10, size = (3, 5))    #3 satırlı 5 sütunlu array

b[1, 1]

b[2, 3]

b[2, 3] = 999

b[2, 3] = 2.9 #Sadece tek tip veri tuttugu ıcın ondalıklı kısmı atıp sadece 2'yi tutacak

b[:, 0] #Bütün satırlardaki 0. sütun

b[1, :] #1.satırda tüm sütunlar

b[0 : 2, 0 : 3] #Satırlarda 0'dan 2'ye kadar git, sütunlarda ise 0'dan 3'e kadar git


            ###Fancy Index

v = np.arange(0, 30, 3) #Sıfırdan 30'a kadar(30 hariç) 3'er 3'er artacak sekılde array olustur

v
v[5]

catch = [1, 2, 3]
v[catch]


            ###NumPy'da Koşullu İşlemler (Condition on NumPy)

v = np.array([1, 2, 3, 4, 5])

#Klasik döngü ile

ab = []

for i in v:
    if i < 3:
        ab.append(i)


#Numpy ile
#True - False Yöntemi ile, Fancy Yöntemi sayesinde

v[v < 3]
v[v > 3]
v[v != 3] #3'ten farklı olanlar
v[v == 3]
v[v >= 3]


            ###Matematiksel İşlemler (Mathematical Operations)

v = np.array([1, 2, 3, 4, 5])

v / 5

v * 5 / 10

v ** 2

v - 1

np.subtract(v, 1)   #Çıkarma
np.add(v, 1)        #Toplama
np.mean(v)          #Ortalama
np.sum(v)           #Toplam alma
np.min(v)           #Min
np.max(v)           #Max
np.var(v)           #Bir veri kümesindeki sayıların dağılımının bir ölçüsü


#NumPy ile iki bilinmeyenli denklem çözümü

#5*x0 + x1 = 12
#x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)


