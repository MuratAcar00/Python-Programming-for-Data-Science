                    ### Functions ###

# Fonksiyon okuryazarlığı

print("a", "b", sep="__")

help(print)

#Fonksiyon Tanımlama

def calculate(x):
    print(x * 2)

calculate(5)

#İki argümanlı/parametreli fonksiyon tanımlama

def summer(arg1, arg2):
    print(arg1 + arg2)

summer(8, 7)

summer(arg2 = 5, arg1 = 8)

                    ### Docstring ###
#Fonksıyonun altında 3 tırnak acıp gırdıgmız bılgıler o fonksıyonun docstring'i olur


def summer(arg1, arg2):
    """
    Sum of two numbers


    Parameter
    ---------
    arg1: int, float

    arg2: int, float

    Returns:
        int, float
    ---------

    """
    print(arg1 + arg2)

summer() #fonksiyonun uzerıne gelınce yazdıgımız docstring geliyor

                    ### Fonksiyonların Statement/Body Bölümü ###

def sayHi():
    print("Merhaba")
    print("Hi")
    print("Hello")

sayHi()

def sayHi(string):
    print(string)
    print("Hi")
    print("Hello"),

sayHi("miuul")


def carpim(x, y):
    carpim = x * y
    print(carpim)

carpim(5, 8)


#Girilen değerleri çarpıp çıkan sonucu liste içinde saklayacak bir fonksiyon tanımlama

listStore = []

def saklama(arg1, arg2):
    a = arg1 * arg2
    listStore.append(a)
    print(listStore)

saklama(5, 8)       
print(listStore)

                    ### Ön Tanımlı Argümanlar/Parametreler (Default Arguments/Parameters) ###

def divide(a, b):
    print(a / b)

divide(10, 2)

#Ne Zaman Fonksiyon Yazma İhtiyacı Duyarız
#DRY (Don't Repeat Yourself)

# varm(sıcaklık), moisture(nem), charge(sarj)


def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

calculate(98, 12, 78)

#Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

#calculate(98, 12, 78) * 10  #Hata verir cunku calculate fonksiyonunu "none type" olarak algılıyor


def calculate(varm, moisture, charge):
    return((varm + moisture) / charge)

calculate(98, 12, 78) * 10 #Return olarak cıkardıgımız ıcın bır sorun yok

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output

varm, moisture, charge, output = calculate(98, 12, 78) # 4 tane cıktı oldugu ıcın 4 tane degısken verıyoruz

# Fonksiyon içerisinde fonksiyon cağırmak

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

calculate(98, 12, 78)

def standardization(a, p):
    return a * 10 / 100 * p * p

standardization(10, 5)

def allCalculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

allCalculation(1, 9, 5, 8)

# Local & Global Variables

listStore = [1, 2]  #Global

def addElement(a, b):
    c = a * b   # c is local
    listStore.append(c)
    print(listStore)

addElement(10, 5)
