            ### GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA) ###


 #1. Genel Resim
 #2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
 #3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
 #4. Hedef Değişken Analizi (Analysis of Target Variable)
 #5. Korelasyon Analizi (Analysis of Correlation)



    #1. Genel Resim:

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")

#Genel olarak fonksiyonlar:
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

#Elimizde ki verinin detaylarını görmek için yazabileceğimiz fonksiyon
def check_df(dataframe, head = 5):
    print("***** Shape *****")
    print(dataframe.shape)
    print("***** Types *****")
    print(dataframe.dtypes)
    print("***** Head *****")
    print(dataframe.head(head))
    print("***** Tail *****")
    print(dataframe.tail(head))
    print("***** NA *****")
    print(dataframe.isnull().sum())
    print("***** Quantiles *****")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99]).T)

check_df(df)

#Başka veri setinde de aynı sekılde kullanılabılır
df = sns.load_dataset("tips")
check_df(df)


df = sns.load_dataset("flights")
check_df(df)


 #2. Kategorik Değişken Analizi (Analysis of Categorical Variables)

df = sns.load_dataset("titanic")
df.head()

df["embarked"].value_counts()
df["sex"].unique()  #Hangi değişkenlerin oldugu bılgısını verır
df["sex"].nunique() #Değişkenlerden kac tane oldugu bılgısını verır

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
cat_cols

#Aslında kategorik olup veri tipleri int ve float olanlar için
#numeric görünümlü kategoriler
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
num_but_cat

#Değişkenin tipi "category" ya da "object" ise ve eşsiz sınıf sayısı 20'den fazla ise bu ölçülebilir bir değişken değildir bunları yakala
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_but_car


cat_cols = cat_cols + num_but_cat
cat_cols

cat_cols = [col for col in cat_cols if col not in cat_but_car]
cat_cols


#Seçtiğimiz değişkenleri dataframe'e taşıma:

df[cat_cols]

df[cat_cols].nunique()

#cat_col'un ıcınde olmayan degıskenler

[col for col in df.columns if col not in cat_cols]



df["survived"].value_counts()   #Değişkenin değerlerinin sayısı
100 * df["survived"].value_counts() / len(df)   #Değişkenin değerlerinin yüzdelik hali

#Yukarıdaki bilgileri tek tek girip cıktı almak yerıne yazacagımız fonksiyon:

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                       "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("************************")
    
#Bu sekılde tek tek tanımlamak yerıne donguye alalım
cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)

#Aynı fonksiyonun sütun grafikli hali
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                       "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("************************")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex",plot=True)

for col in cat_cols:
    if df[col].dtypes=="bool":
        print("Type is bool")
    else:
        cat_summary(df, col,plot=True)

df["adult_male"].astype(int)


cat_summary(df, "sex",plot=True)

for col in cat_cols:
    if df[col].dtypes=="bool":
        df[col]=df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col,plot=True)


    #3. Sayısal Değişken Analizi (Analysis of Numerical Variables)

df[["age", "fare"]].describe().T


#Veri seti içerisinden "numeric" değişkenleri seçme:

num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

#num_cols'ta olupta cat_cols'da olmayanları seçelim:

num_cols = [col for col in num_cols if col not in cat_cols]

def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df, "age")

#Yukarıdakı ıslemı her bır degısken ıcın tek tek yapmak ıcın:

for col in num_cols:
    num_summary(df, col)


#Grafikleştirmek için:

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

num_summary(df, "age", plot=True)

#Tüm değişkenlerde uygulamak ıcın:

for col in num_cols:
    num_summary(df, col, plot=True)
