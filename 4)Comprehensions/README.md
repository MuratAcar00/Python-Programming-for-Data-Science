<img src="https://twemoji.maxcdn.com/v/latest/svg/1f1ec-1f1e7.svg" width="20"/> English – List and Dictionary Comprehensions
This section contains concise notes on list and dictionary comprehensions in Python, based on the Python Programming for Data Science course by Miuul. Comprehensions offer a powerful and readable way to create and manipulate collections.

📋 What is a Comprehension?
A comprehension is a short syntax for generating sequences like lists, dictionaries, or sets.
Instead of using a loop and append() method, comprehensions allow you to express the same logic in a single line.

📌 List Comprehensions
List comprehensions are used to create a new list by applying an expression to each item in an existing iterable.

Basic syntax:
[expression for item in iterable]
You can also include a condition:
[expression for item in iterable if condition]

Examples:

Creating a list of squares of numbers from 0 to 9.

Filtering even numbers from a list.

Applying string transformations to a list of names.

📌 Dictionary Comprehensions
Dictionary comprehensions allow you to build dictionaries using a compact syntax.

Basic syntax:
{key_expression: value_expression for item in iterable}
With condition:
{key: value for key, value in iterable if condition}

Examples:

Creating a dictionary of numbers and their squares.

Filtering dictionary items.

Swapping keys and values in a dictionary.

🎯 Why Use Comprehensions?
More concise and readable code

No need for extra temporary variables or loops

Faster execution

Ideal for data cleaning and transformation

📌 Source
These notes are based on the Python Programming for Data Science course by Miuul, and reflect my own practice and understanding of Python comprehensions.<br><br><br><br>




<img src="https://twemoji.maxcdn.com/v/latest/svg/1f1f9-1f1f7.svg" width="20"/> Türkçe – Liste ve Sözlük Üreteçleri (Comprehensions)
Bu bölümde Miuul tarafından verilen Python Programming for Data Science eğitimi kapsamında işlenen liste (list) ve sözlük (dictionary) comprehensions (üreteçler) konusuna dair özet notlar yer almaktadır.

📋 Comprehension (Üreteç) Nedir?
Comprehension, listeler, sözlükler veya kümeler gibi veri yapılarını tek satırda ve sade bir şekilde oluşturmak için kullanılan bir yazım şeklidir.
for döngüsüyle yazılabilecek işlemler comprehension ile daha kısa ve okunabilir hale gelir.

📌 Liste Üreteçleri (List Comprehension)
Liste üreteçleri, bir iterable (örneğin liste veya range) içindeki her öğeye bir işlem uygulayarak yeni bir liste oluşturur.

Temel yazım şekli:
[ifade for öğe in iterable]
Şartlı kullanım:
[ifade for öğe in iterable if şart]

Örnekler:

0'dan 9'a kadar olan sayıların karelerini alma

Bir listeden sadece çift sayıları seçme

Bir isim listesinde her ismi büyük harfe çevirme

📌 Sözlük Üreteçleri (Dictionary Comprehension)
Sözlük üreteçleri, anahtar-değer çiftlerinden oluşan sözlükleri kısa yoldan oluşturmak için kullanılır.

Temel yazım şekli:
{anahtar_ifadesi: değer_ifadesi for öğe in iterable}
Şartlı kullanım:
{anahtar: değer for anahtar, değer in iterable if şart}

Örnekler:

Sayılar ve karelerinden oluşan bir sözlük oluşturma

Belirli anahtar-değer çiftlerini filtreleme

Anahtar ve değerleri yer değiştirme

🎯 Neden Comprehension Kullanılır?
Daha okunabilir ve sade kod yazmak için

Ek döngü veya geçici değişken kullanmadan işlem yapmak için

Performansı artırmak için

Veri temizleme ve dönüştürme işlemleri için ideal

📌 Kaynak
Bu notlar, Miuul tarafından verilen Python Programming for Data Science eğitimi kapsamında edinilen kişisel öğrenim sürecime dayanmaktadır.
