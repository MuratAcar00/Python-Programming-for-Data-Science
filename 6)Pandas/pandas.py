import numpy as np
import pandas as pd
import seaborn as sns


                    ### PANDAS ###


#Pandas Series
#Veri Okuma (Reading Data)
#Veriye Hızlı Bakış (Quick Look at Data)
#Pandas'ta Seçim İşlemleri (Selection in Pandas)
#Toplulaştırma ve Gruplama (Aggregation & Grouping)
#Apply ve Lambda
#Birleştirme (Join) İşlemleri



        ### Pandas Series ###


s = pd.Series([10, 77, 12, 4, 5])

type(s)
s.index
s.dtype
s.size
s.ndim          #Boyut bilgisini verir
s.values        #Değerleri yazar
type(s.values)
s.head(3)       #Baştan 3 karakteri yazar
s.tail(3)       #Sondan 3 karakteri yazar


        ### Veri Okuma (Reading Data) ###

#Diğer dosya formatlarını okumak için kullanmamız gereken fonksiyonları pd'nin üzerine ctrl ile birlikte tıklayarak öğrenebiliriz
#Veya pandas cheatsheet'den bakabiliriz


#df = pd.read_csv("csv dosya yolu")

df.head()



                ### Veriye Hızlı Bakış (Quick Look at Data) ###


df = sns.load_dataset("titanic") #Titanic veri seti yolculuk sonunda yolcuların hayatta kalıp veya kalamamalarını ifade eden bir veri setidir 

df.head()
df.tail()
df.shape        #Boyut bilgisi için
df.info()       #Detaylı bilgi için
df.columns      #Verinin değişkenlerine erişmek için
df.index
df.describe().T #Verinin özet bilgisine erişmek için kullanıyoruz.Sonuna T (transpozu) yazmamızın sebebi daha okunabılır olmasını saglamak
df.isnull().values.any()        #Veri setinde bir tane bile olsa eksiklik var mı
df.isnull().sum()               #Hangi değişkende kaç tane eksik bilgi var
df["sex"].value_counts()        #Hangi değişkenden kaç tane var



             ### Pandas'ta Seçim İşlemleri (Selection in Pandas) ###


df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]        #0'dan 13'e kadar olan degerlerı getir
df.drop(0, axis = 0).head()     #0'ıncı satırı sil

deleteIndex = [1, 3, 5, 7]

df.drop(deleteIndex, axis = 0).head(10) #deleteIndex içerisindeki değerleri silmeye yarar

df.drop(deleteIndex, axis = 0, inplance = True)#Yaptıgımız degısıklıgı kalıcı hale getırmek ıcın inplance = True kullandık


#Değişkeni Indexe Çevirmek

df["age"].head()
df.age.head()   #İkisi de aynı 

df.index = df["age"]    #Age degıskenını indexe değişken olarak atadık

df.drop("age", axis = 1, inplace = True)        #Silme işlemi satırdan değilde sütundan olacagı ıcın 1 yazıyoruz. 0 = satır, 1 = sütun

df.head()


#Indexi Değişkene Çevirmek

#1. Yol:

df["age"] = df.index
df.head()

#2.Yol:

df.reset_index().head()

#Eger index olarak kullanılan değişkenin dataframe'e eklenmesını ıstemıyorsak

df.reset_index(drop=True, inplace=True)


        ### Değişkenler Üzerinde İşlemler ###


pd.set_option("display.max_columns", None)      #Tabloyu onızlemek için "..." şeklinde gösterilen kısmı oldugu gıbı gosterır
df = sns.load_dataset("titanic")
df.head()

"age" in df     #Değişken dataframe içerisinde var mı
df["age"].head()

type(df["age"].head())  #pandas serisi oldugu bılgısıne erısıyoruz

type(df[["age"]].head())        #Dataframe olarak almaya devam etmek ıstıyorsak degıskenı ıkı parantez ıcıne almamız gerekır


df[["age", "alive"]]    #Birden fazla degıskenı cagırmak ıstedıgımızde

#Asagıdakı yolda aynı sadece listeyi ayrı olarak olusturup cagırıyoruz
colNames = ["age", "adult_male", "alive"]

df[colNames]

#Yeni bir değişken ekleme
df["age2"] = df["age"] ** 2
df[["age", "age2"]]


df["age3"] = df["age"] / df["age2"]
df["age3"]


#Silme işlemi

df.drop("age3", axis = 1).head()


df.drop(colNames, axis = 1).head()


df.loc[:, df.columns.str.contains("age")].head()        #veri çerçevesinden "age" kelimesini içeren tüm sütunların görüntülenmesini sağlar

df.loc[:, ~df.columns.str.contains("age")].head()       #veri çerçevesinden "age" kelimesini içermeyen!!! tüm sütunların görüntülenmesini sağlar


        ### iloc & loc ###
#Seçim işlemleri için kullanılan yapılardır


# iloc: integer based selection

df.iloc[0:3]    #0'dan 3'e kadar olan bilgileri getir

df.iloc[0,0]   #0. satırın 0. sütunundaki bilgileri getir


#loc: label based selection

df.loc[0:3]     #0'dan 3'e kadar olan bilgileri getirir. 3 dahil!!!



df.iloc[0:3, 0:3]       #Bilmem kacıncı satırdan bilmem nereye kadar bilgileri getir ama aynı zamanda istediğim bilgileri getir(sen anladın)

df.loc[0:3, "age"]      #Yukarıda ki işlemi değişkenin adını yazarak yapmak ıstıyorsak "loc" kullanıyoruz


#Aynı ıslemın liste kullanılarak yapılmıs hali
colNames = ["age", "embarked", "alive"]
df.loc[0:3, colNames]


        ### Koşullu Seçim (Conditional Selection) (Bir nevi SQL) ###

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

#Yası 50 den buyuk olanlar
df[df["age"] > 50].head()

#Yası 50'den buyuk kac kısı var
df[df["age"] > 50]["age"].count()

#Yası 50'den buyuk olanların sınıf bılgısı
df.loc[df["age"] > 50, "class"].head()

#Yası 50'den buyuk olanların yas ve sınıf bılgısı
df.loc[df["age"] > 50, ["age", "class"]].head()

#Yası 50'den buyuk cınsıyetı erkek olanların bılgısı
df.loc[(df["age"] > 50) & (df["sex"] == "male") ,["age", "class"]].head()

        ### Suan bu yazdıklarımı bır nevi ezbere yazıyorum dogru durust anlayamıyorum ama halledeceğim
#Önceki örneğin üzerine bir de bindiği limanı şart koştuk
df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg") ,["age", "class", "embark_town"]].head()


#Sectiğimiz limanın o ya da su sartını yazacagız
df.loc[(df["age"] > 50) & (df["sex"] == "male") & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")) ,["age", "class", "embark_town"]].head()



                        ### #Toplulaştırma ve Gruplama (Aggregation & Grouping) ###

# count(): Boş olmayan değerlerin sayısını hesaplar.
# first(): Her gruptaki ilk değeri döndürür.
# last(): Her gruptaki son değeri döndürür.
# mean(): Değerlerin aritmetik ortalamasını hesaplar.
# median(): Sayısal verinin orta noktasındaki değeri bulur.
# min(): Değerlerin en küçüğünü bulur.
# max(): Değerlerin en büyüğünü bulur.
# std(): Değerlerin standart sapmasını hesaplar.
# var(): Değerlerin varyansını hesaplar.
# sum(): Değerlerin toplamını hesaplar.
# pivot table:  Bir tablodaki verileri özetlemek ve yeniden düzenlemek için kullanılır.
# agg(): Pandas'ta gruplanmış veya gruplanmamış verilere aynı anda birden çok toplama (aggregate) işlemi uygulamak için kullanılan güçlü ve esnek bir fonksiyondur.

#Yas ortalaması

df["age"].mean()

#Kadınların ve erkeklerin yas ortalamasını ayrı ayrı alma

df.groupby("sex")["age"].mean()

#Farklı ve asıl kullanmamız gereken yolu

df.groupby("sex").agg({"age": "mean"})

#Hem ortalamasını alıp hemde toplam sonucu verir
df.groupby("sex").agg({"age": ["mean", "sum"]})


#Hem cınsıyete hemde bindiği limana göre grupla ve yasama oranlarının ortalamasını da ekle
df.groupby(["sex", "embark_town"]).agg({"age" : ["mean", "sum"], "survived": "mean"})

#Sınıfları da ekle
df.groupby(["sex", "embark_town", "class"]).agg({"age" : ["mean", "sum"], "survived": "mean"})

#Cinsiyet sayılarını da ekle
df.groupby(["sex", "embark_town", "class"]).agg({"age" : ["mean", "sum"], "survived": "mean", "sex": "count"})



        ### Pivot Table ###


#Yaş ve gemiye binilen liman üzerinden pivot table olusturup bunların kesısımınden de yas bılgısıne erıselım

df.pivot_table("survived", "sex", "embarked") #Tabloda survived kısmının ortalamasını almasının sebebı pivot_table'da ön tanımlı olan fonksiyonun mean() olmasından kaynaklıdır

df.pivot_table("survived", "sex", "embarked", aggfunc = "std") # Burada değiştirip standart sapmasını hesaplatıyoruz


#Bindiği liman ve sınıfına göre hangi cinsiyette yasama sansının ne oldugu tablosu
df.pivot_table("survived", "sex", ["embarked", "class"])


df["newAge"] = pd.cut(df["age"], (0, 10, 18, 25, 40, 90)) #cut fonksiyonu basta ne bolecegını sonrasında ıse hangi aralıkları bolecegı gırılerek kullanılır
df.head()


df.pivot_table("survived", "sex", ["newAge", "class"])

pd.set_option("display.width", 750) #Tüm tabloyu daha rahat gorebılmek ıcın görüntüleme genişliğini arttırdık


                        ### Apply and Lambda ###


#Apply: bir DataFrame'in her bir satırına veya sütununa özel bir fonksiyon uygulamak için kullanılan çok yönlü bir Pandas metodudur.

#Lambda: Python'da yalnızca tek bir ifade içeren ve isimsiz olarak tanımlanan küçük, hızlı ve anonim bir fonksiyondur.


df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5
df.head()

#Asagıda yazdıklarımızı otomatıklestır
(df["age"] / 10).head()
(df["age2"] / 10).head()
(df["age3"] / 10).head()

#Yazdırdık
for col in df.columns:
        if "age" in col:
                print((df[col] / 10).head())

#Kalıcı hale getırdık
for col in df.columns:
        if "age" in col:
                df[col] = df[col] / 10


#Apply ve Lambda ile:

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

#Farklı Yol:

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()



                ### Birleştirme (Join) İşlemleri ###


m = np.random.randint(1, 30, size = (5, 3))

df1 = pd.DataFrame(m, columns = ["var1", "var2", "var3"])

df2 = df1 + 99

pd.concat([df1, df2])   # concat metodu ile 2 dataframe'i birleştirdik
                        #İki dataframe'in de indexleri 0'dan baslıyor!!!(sıkıntı)

pd.concat([df1, df2], ignore_index = True)      #Kendi indexlerini tutmadan birleştiler


        # Merge ile Birleştirme İşlemleri

df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["mark", "john", "dennis", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})



pd.merge(df1, df2)      #Merge ile df'leri birleştirdik

pd.merge(df1, df2, on = "employees")    #Hangi değişkene göre birleştirmek istiyorsak on = "istediğimiz değişken" olacak sekılde yazıyoruz


#Her çalısanın mudur bılgısıne erısmek

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                   "manager": ["Caner", "Mustafa", "Berkcan"]})


pd.merge(df3, df4, on = "group")

