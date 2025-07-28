                    ### KOŞULLAR (CONDITIONS) ###

#True - False

1 == 1 #True

1 == 2 #False

#if

if 1 == 1:
    print("something") #cıktı verır cunku kosulu saglar

if 1 == 2:
    print("something") #cıktı vermez cunku kosul saglanmaz


number = 11

if number == 10:
    print("number is 10")


number = 10

if number == 10:
    print("number is 10")


def numberCheck(number):
    if number == 10:
        print("Something")

numberCheck(10)

#else

def numberCheck(number):
    if number == 10:
        print("Something")
    
    else:
        print("Wrong number") # Eger ki sart saglanmazsa bunu yap

numberCheck(11)

#elif

def numberCheck1(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:   
        print("less than 10")
    else:
        print("equal to 10")

numberCheck1(10)
numberCheck1(9)
numberCheck1(11)

            ### DÖNGÜLER (LOOPS) ###

#for loop

students = ["John", "Mark", "Venessa", "Mariam"]

students[0]
students[1]
students[2]
students[3]


for x in students:  # students listesindeki elemanların her birini gezip x'e atayarak yazdırmaya yaradı
    print(students)

for x in students:
    print(x.upper())    # x değerlerinin tamamını buyuk harflere cevırdı


salaries = [1000, 2000, 3000, 4000, 5000]

for x in salaries:
    print(x)

for x in salaries:
    print(int(x * 20/100 + x))   #Her maasa %20 zam yaptı aynı zamanda integera çevirdi


def newSalary(salary, rate):    #Maası ve verilecek zammı girdiğimizded bize zamlı maası veren fonksiyon
    return int(salary * rate / 100 + salary)

newSalary(1000, 10)


for x in salaries:
    print(newSalary(x, 10)) #Tüm maaslara yüzdelik zam veren döngü

salaries2 = [50, 100, 200, 300, 400]

for x in salaries2:
    print(newSalary(x, 10))

for x in salaries:      #Maası 3000'den fazla olanlara yüzde 50 zam verirken 3000'den dusuk olanlara 80 zam veren fonksıyon
    if x > 3000:
        print(newSalary(x,50))
    else:
        print(newSalary(x,80))



            ### Uygulama - Mülakat Sorusu

#Amac: Asagıdakı sekılde string degıstıren fonksiyon yazmak

#before: "hi my name is john and i am learning python"
#after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"


def alternating(string):
    newString = ""
    #Girilen string'in index'lerinde gez
    for stringIndex in range(len(string)):  #range fonksiyonu içerisine giren değerin uzunluğu kadar calısır
        #Index çift ise buyuk harfe cevir
        if stringIndex % 2 == 0:
            newString += string[stringIndex].upper()
        #Index tek ise kucuk harfe cevir
        else:
            newString += string[stringIndex].lower()
    print(newString)

alternating("hi my name is john and i am learning python")

# break & continue & while

salaries = [1000, 2000, 3000, 4000, 5000]

for x in salaries:  # 3000'i bulana kadar devam et 3000'i bulunca donguyu durdur
    if x == 3000:
        break
    print(x)

for x in salaries:  #Devam eder,görmezden gelir
    if x == 3000:
        continue
    print(x)#3000 harici hepsi yazdırıldı


number = 1

while number < 5:   #Numara 5'ten kucuk oldugu müddetçe yazdırmaya devam edecek fakat her turda numaraya 1 ekleyecek
    print(number)
    number += 1


#Enumerate: Otomatik Counter/Indexer ile for loop

studenets = ["John," "Mark," "Venessa," "Mariam,"]

for x in students:
    print(x)


#index değeri çift olanları list1'e tek olanları list2'ye atayan fonksiyon
list1 = []
list2= []

for index, student in enumerate(students):  #0'dan baslayarak tum degerlere index atar
    print(index, student)
    if index % 2 == 0:
        list1.append(student)
    else:
        list2.append(student)
print(list1)
print(list2)


for index, student in enumerate(students, 1):  #1'den baslayarak tum degerlere index atar
    print(index, student)


            ### Uygulama - Mülakat Sorusu

#divideStudents fonksiyonu yazınız
#Çift indexte yer alan öğrencileri bir listeye alınız
#Tek indexte yer alan öğrencileri başka bir listeye alınız
#Fakat bu iki liste tek bir liste olarak return olsun

students = ["John", "Mark",  "Venessa", "Mariam"]


def divideStudents(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

divideStudents(students)


#alternating fonksiyonunun enumerate ile yazılması


def alternating(string):
    newString = ""
    for index, harf in enumerate(string):
        if index % 2 == 0:
            newString += harf.upper()
        else:
            newString += harf.lower()
    print(newString)

alternating("hi my name is john and i am learning python")


#Zip: Listeleri eşlemeye yarar

students = ["John", "Mark", "Venessa", "Mariam"]
departments = ["mathematics", "statistics", "physics", "astronomy"]
ages = [23, 30, 26, 22]

list(zip(students, departments, ages))


            ### lambda, map, filter, reduce ###

#lambda: kullan at fonksiyondur,diğer örnekler ile birlikte kullanıldıgında işe yarar ve mantık kazanır

#map

salaries = [1000, 2000, 3000, 4000, 5000]

def newSalary(x):
    return x * 20 / 100 + x

newSalary(5000)

for salary in salaries:
    print(newSalary(salary))


list(map(newSalary, salaries))

list(map(lambda x: x * 20 / 100 + x, salaries))


#filter: Sorguya yarar.Bir değer listesini tek bir sonuca indirgemeye yardımcı olur

listStore = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x  % 2 == 0, listStore))

#reduce: Kütüphane indirmek gerekiyor
#from functools import reduce

reduce(lambda a, b: a + b, listStore)
