#Veri Yapilari Giris:

#Sayilar: integer

x = 45
type(x)

#Sayilar: Float

y = 10.1
type(y)


#Sayilar: Complex

z = 2j + 1
type(z)

#String

a = "Hello AI"
type(a)

#Boolean

True
False

5 == 4  #False

5 == 5  #True


#List

x = ["btc", "eth", "xrp"]
type(x)

#Dictionary

x = {"name": "Murat", "Age": 23}
type(x)

#Tuple(Demet)

x = ("python", "ml", "ds")
type(x)

#Set

x = {"python", "ml", "ds"}

type(x)

#NOT: Liste,tuple,set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.

                    ### Sayilar ###

#Sayinin karesini alma ** örneğin 5 in karesi 5 ** 2 küpünü alma 5 ** 3 gibi...

#Tipleri değiştirme: Float olan a değişkenini integer'a dönüştürmek istersek int(a) veya float(b)

                    ### Strings ###

#Çok Satırlı Karakter Dizileri: """ İçine yazdığımız her şeyi karakter olarak tanımlar """

longStr = """ 25 Temmuz:

1543 - Estergon Kuşatması: Estergon, Osmanlı İmparatorluğu tarafından kuşatıldı ve yaklaşık iki hafta süren kuşatma sonrasında Osmanlı egemenliğine girdi.
1909 - Louis Blériot, uçağı ile ilk kez Manş Denizi'ni aştı.
1933 - Lev Troçki, sığınmacı olarak Fransa'ya gitti.
1934 - Avusturya başbakanı Engelbert Dollfuß, ülkesindeki Naziler tarafından Viyana'da öldürüldü.
1994 - Ürdün kralı Hüseyin ile İsrail Başbakanı İzak Rabin savaş durumunu sona erdiren deklarasyonu imzaladılar.
Rosalind Franklin (d. 1920)Matt LeBlanc (d. 1967)José Mauro de Vasconcelos (ö. 1984)
24 Temmuz25 Temmuz26 Temmuz
(ArşivYılın günleri listesi)"""

#Karakter Dizilerinin Elemanlarına Erişmek

name = "Murat"
name[0]

name [0:2] #Sıfırıncı karakterden baslayıp 2. harfe kadar git(2 dahil değil)

longStr[0: 10]

#String İçerisinde Karakter Sorgulama

longStr

"Avusturya" in longStr # Avusturya karakteri longStr değişkeninin içinde mi

                    ### String Metodları ###

dir(str)

#len

name = "Murat"

type(len)

len(name) #Değişkenin kaç karakterden oluştugu bılgısını verır

len("askjdfhaksldf")

#upper() & lover() metodları: Büyük,küçük dönüşümleri

"miuul".upper() #Küçük harfleri büyüğe çevirdi

"MİUUL".lower() # Büyük harfleri küçüğe çevirdi

#replace: Karakter Değiştirme

hi = "Hello AI"
hi.replace("l", "p")    #hi değikenindeki "l" harflerini "p" ile değiştirdi.

#split: Böler

"Hello AI Era".split() #Boşluklara göre böldü

#strip: Kırpar

" ofofo ".strip() #Boşlukları kırpar
"ofofo".strip("o") # "o"ları kırptı

#capitalize: İlk harfi büyütür

"foo".capitalize()

                    ### List ###

#Değiştirilebilir
#Sıralıdır.Index işlemleri yapılabılır
#Kapsayıcıdır

notes = [1,2,3,4]
type(notes)

names = ["a","b","c"]

notMix = [1,2,3,4,"a","b",True,[1,2,3]]
notMix[0]

notes[0] = 99   #notes değişkenindeki ilk karakteri 99 olarak değiştirdi
notes[0]

#List Methods

dir(notes)

len(notes)

#append: Eleman ekler

notes.append(100) # notes değişkeninin sonuna 100 ekledi

#pop: indexe göre eleman siler

notes.pop(0) #notes değişkeninde ilk elemanı sildi

#insert: indexe göre eleman ekler

notes.insert(2,88) # notes değişkeninin 2. indexine 88 elemanını ekledi

                    ### Dictionary ###

#Değiştirilebilir
#Sırasız (3.7 sürümünden sonra sıralı ozellıgı kazanmıstır)
#Kapsayıcı  (Birden fazla veri türünü içerisinde tutabilir)

#Key-Value

dictionary = {"Reg": ["Regression", 10],
              "Log": "Logistic Regression",
              "Cart":"Classification and Reg"}

dictionary["Reg"]

#Key Sorgulama

"Reg" in dictionary #Reg karakteri dictionary ıcerısınde mı

#Value Değiştirmek

dictionary["Reg"] = ["YSA", 10]

#Tüm Key'lere Erişmek

dictionary.keys() #dictionay değişkenindeki tüm key'leri çağırır

dictionary.values() #dictionay değişkenindeki tüm value'ları çağırır

#Tüm Çiftleri Tuple Formatında Listeye Çevirme

dictionary.items()

#Key-Value Değerini Güncelleme

dictionary.update({"Reg": 11}) #Reg anahtarının değerini 11 olarak güncelledi
dictionary.update({"ABC": 99}) #ABC diye bir key olmadıgı ıcın sıfırdan olusturup degerını de 99 yaptı

                    ### Tuple ###

#Değiştirilemez
#Sıralıdır  (Elemanlarına erişilebiliyor anlamına geliyor)
#Kapsayıcıdır

t = ("john","mark", 1, 2)
type(t)

t[0]
t[0:3]
t[0] = 99 #Hata verir çünkü tuple değiştirilemezdir

                    ### Set ###

#Değiştirilebilir
#Sırasız + Eşsizdir
#Kapsayıcıdır

#difference(): İki kümenin farkı

set1 = set([1, 2, 5])
set2 = set([1, 2, 3])

type(set1)

#set1'de olup set2'de olmayanlar elemanlar

set1.difference(set2)  

#set2'de olup set1'de olmayan elemanlar

set2.difference(set1)

#symmetric_difference(): İki kümede de birbirlerine göre olmayanlar

set1.symmetric_difference(set2)

set2.symmetric_difference(set1)

#intersection(): İki kümenin kesişimi

set1.intersection(set2)

#union(): İki kümenin birleşimi

set1.union(set2)

#isdisjoint(): İki kümenin kesişimi boş mu

set1.isdisjoint(set2)

#issubset(): Bir küme diğer kümenin alt kümesi mi

set1.issubset(set2)

set2.issubset(set1)

#issuperset(): Bir küme diğer kümeyi kapsıyor mu

set1.issuperset(set2)

set2.issuperset(set1)