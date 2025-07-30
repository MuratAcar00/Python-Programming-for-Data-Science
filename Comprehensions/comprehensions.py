import seaborn as sns

                    ### COMPREHENSIONS ###

#List Comprehensions


        #Without List comprehensions 

salaries = [1000, 2000, 3000, 4000, 5000]

def newSalary(x):
    return x * 20 / 100 + x

nullList = []

for salary in salaries:
    nullList.append(newSalary(salary))
print(nullList)

for salary in salaries:
    if salary > 3000:
        nullList.append(newSalary(salary))
    else:
        nullList.append(newSalary(salary * 2))

print(nullList)

#With List Comprehensions *** ÇOK ÖNEMLİ ###


[newSalary(salary * 2) if salary < 3000 else newSalary(salary) for salary in salaries]

#Maaslar listesindeki her maası 2 ile carp

[salary * 2 for salary in salaries]

#Maası 3 binden az olanları 2 ile çarp
[salary * 2 for salary in salaries if salary < 3000 ]

#else olmadan sadece if kullandıgımızda if sagda kullanılır.Else ile birlikte 
#kullanıldıgında solda yazılır


#Maası 3 binden az olanları ıkı ıle carp dusuk olanları ise 0'la carp

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]


#Belirli bir fonksiyonu bu blogun ıcınde kullan

[newSalary(salary * 2) if salary < 3000 else newSalary(salary * 0.2) for salary in salaries]


#İstenen ogrencılerın ısımlerını buyuk harfle yazıp, istenmeyen ogrencılerın ısımlerını kucuk harfle yaz

students =  ["John", "Mark", "Venessa", "Mariam"]

studentsNo = ["John", "Venessa"]

[student.lower() if student in studentsNo else student.upper() for student in students]

#Bir farklı yazılısı

[student.upper() if student not in studentsNo else student.lower() for student in students]


            ### Dict Comprehension ###

dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}

dictionary.keys()
dictionary.values()
dictionary.items()

#Value degerlerının karesini alma

{k: v ** 2 for k, v in dictionary.items()}

#Key degerlerını buyutmek
{k.upper(): v for k,v in dictionary.items()}

#İkisi birden
{k.upper(): v ** 2 for k,v in dictionary.items()}

            ### Uygulama - Mülakat Sorusu ###

#Amaç: Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir

numbers = range(10)
newDict = {}

for n in numbers:
    if n % 2 == 0:
        newDict[n] = n ** 2
print(newDict)

#Dict Comprehension kullanarak yapma

{n: n ** 2 for n in numbers if n % 2 == 0}


#List % Dict Comprehension Uygulamalar

#Bir veri setindeki değişken isimlerini değiştirmek

#Before:
#["total", "speeding", "alcohol", "not-distracted", "no-previous", "ins-premium","ins-losses", "abbrev"]

#After:
#["TOTAL", "SPEEDING", "ALCOHOL", "NOT-DISTRACTED", "NO-PREVIOUS", "INS-PREMIUM", "INS-LOSSES", "ABBREV"]

df = sns.load_dataset("car_crashes")
df.columns

A = []
for col in df.columns:
   A.append(col.upper())

df.columns = A
df.columns

#List Comprehensions ile 

df.columns = [col.upper() for col in df.columns]


#İsminde "INS" olan degıskenlerın basına "FLAG" diğerlerine "NO_FLAG" ekle

[col for col in df.columns if "INS" in col]


["FLAG_" + col for col in df.columns if "INS" in col]


["FLAG_" + col  if "INS" in col else "  NO_FLAG_" + col for col in df.columns]


df.columns = ["FLAG_" + col  if "INS" in col else "  NO_FLAG_" + col for col in df.columns]


#Amaç key'i string, value'su aşağıdaki gibi bir liste olan oluşturmak
#Sadece sayısal degıskenler ıcın yapmak istiyoruz

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
# 'speeding': ['mean', 'min', 'max', 'var'],
# 'alcohol': ['mean', 'min', 'max', 'var'],
# 'not_distracted': ['mean', 'min', 'max', 'var'],
# 'no_previous': ['mean', 'min', 'max', 'var'],
# 'ins_premium': ['mean', 'min', 'max', 'var'],
# 'ins_losses': ['mean', 'min', 'max', 'var']}

df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]

soz = {}
agg_list = {"mean", "min", "max", "sum"}

for col in num_cols:
    soz[col] = agg_list

#Kısa Yol
new_dict = {col: agg_list for col in num_cols}

#Ne işe yarar
df[num_cols].head()
df[num_cols].agg(new_dict)
