<img src="https://cdn-icons-png.flaticon.com/24/197/197374.png" alt="UK Flag"> <strong>English</strong>

🧠 **Python Functions – Notes from Python Programming for Data Science**  
This section contains structured notes on Python functions, based on the course *Python Programming for Data Science* by Miuul. It covers key concepts, usage patterns, and best practices.

📌 **What is a Function?**  
A function is a reusable block of code designed to perform a specific task. It helps reduce repetition, organizes code better, and improves readability.  
You define a function using the `def` keyword, followed by the function name and parentheses. Inside the parentheses, you can define parameters.

Example:  
```python
def greet():
    print("Hello")
```

Inside the function body, you write the code to be executed.  
You can use `return` to send back a result.

🧱 **Topics Covered**

- **Defining a Function**  
  Syntax: `def function_name(parameters):`  
  Parameters can be optional or required.

  Example:  
  ```python
  def greet(name):
      return f"Hello, {name}"
  ```

- **Calling a Function**  
  ```python
  greet("Murat")  # → "Hello, Murat"
  greet()         # if default is set → "Hello, Guest"
  ```

- **Return Statement**  
  Returns a result from the function to be stored or used directly.

- **Default Parameters**  
  Parameters with default values:
  ```python
  def greet(name="Guest"):
      return f"Hello, {name}"
  ```

- **Flexible Number of Arguments**  
  - `*args`: for variable positional arguments  
  - `**kwargs`: for variable keyword arguments

- **Lambda Functions**  
  Anonymous one-line functions:  
  ```python
  lambda x, y: x + y
  ```

- **Scope and Namespace**  
  - Variables inside functions are local.  
  - Use `global` to access or modify global variables inside functions.

- **Nested Functions**  
  Functions can be defined within functions for encapsulation.

- **Comprehensions within Functions**  
  Use list/dict/set comprehensions inside functions for concise data structure creation.

- **Best Practices**  
  ✅ Use meaningful names  
  ✅ Keep functions short  
  ✅ Add docstrings  
  ✅ Avoid side effects  
  ✅ Reuse logic

🎯 **Why Use Functions?**  
- Organize code into logical units  
- Reuse logic  
- Easier testing and debugging  
- Embrace modular design

📌 **Source**  
Based on the *Python Programming for Data Science* course by [Miuul](https://miuul.com), intended for personal learning.




<br><br><br><br>

<img src="https://twemoji.maxcdn.com/v/latest/svg/1f1f9-1f1f7.svg" width="20"/> <strong>Türkçe</strong>

🧠 **Python Fonksiyonları – Python ile Veri Bilimi Programlaması Notları**  
Bu bölüm, Miuul’un *Python Programming for Data Science* kursuna dayalı olarak Python fonksiyonları hakkında yapılandırılmış notları içermektedir. Temel kavramları, kullanım biçimlerini ve en iyi uygulamaları kapsar.

📌 **Fonksiyon Nedir?**  
Fonksiyon, belirli bir görevi yerine getirmek için tasarlanmış, tekrar kullanılabilir bir kod bloğudur.  
Kod tekrarını azaltır, okunabilirliği artırır ve kodun daha düzenli olmasını sağlar.  
`def` anahtar kelimesi ile tanımlanır, ardından fonksiyon ismi ve parantezler gelir. Parantez içine parametreler tanımlanabilir.

Örnek:  
```python
def greet():
    print("Merhaba")
```

Fonksiyon gövdesine, çalıştırılacak kod yazılır.  
`return` ifadesiyle sonuç geri döndürülebilir.

🧱 **Kapsanan Konular**

- **Fonksiyon Tanımlama**  
  Söz dizimi: `def fonksiyon_ismi(parametreler):`  
  Parametreler isteğe bağlı ya da zorunlu olabilir.

  Örnek:  
  ```python
  def greet(name):
      return f"Merhaba, {name}"
  ```

- **Fonksiyon Çağırma**  
  ```python
  greet("Murat")  # → "Merhaba, Murat"
  greet()         # varsayılan değer varsa → "Merhaba, Misafir"
  ```

- **Return İfadesi**  
  Fonksiyondan bir sonucu geri döndürmek için kullanılır.

- **Varsayılan Parametreler**  
  Parametreye varsayılan bir değer atanabilir:
  ```python
  def greet(name="Misafir"):
      return f"Merhaba, {name}"
  ```

- **Esnek Parametreler**  
  - `*args`: İsteğe bağlı sayıda pozisyonel parametre  
  - `**kwargs`: İsteğe bağlı sayıda anahtar-değer çifti

- **Lambda Fonksiyonları**  
  Küçük, isimsiz fonksiyonlardır:  
  ```python
  lambda x, y: x + y
  ```

- **Scope (Kapsam) ve Namespace (İsim Alanı)**  
  - Fonksiyon içinde tanımlanan değişkenler yereldir.  
  - Dışarıdaki global değişkenlere erişmek için `global` kullanılır.

- **İç İçe Fonksiyonlar (Nested Functions)**  
  Bir fonksiyon içinde başka bir fonksiyon tanımlanabilir.

- **Comprehension Kullanımı**  
  Fonksiyonlar içinde liste/sözlük/küme comprehension kullanılarak kısa ve etkili veri yapıları oluşturulabilir.

- **En İyi Uygulamalar**  
  ✅ Anlamlı fonksiyon isimleri kullanın  
  ✅ Fonksiyonları kısa ve tek işleve odaklı yazın  
  ✅ Açıklayıcı docstring ekleyin  
  ✅ Yan etkilerden kaçının  
  ✅ Tekrar eden kodları fonksiyon haline getirin

🎯 **Neden Fonksiyon Kullanmalı?**  
- Kodu mantıksal parçalara ayırmak için  
- Aynı mantığı tekrar tekrar kullanmak için  
- Test ve hata ayıklamayı kolaylaştırmak için  
- Modüler programlamayı benimsemek için

📌 **Kaynak**  
Notlar, kişisel öğrenim amacıyla hazırlanmış olup, [Miuul](https://miuul.com) tarafından sunulan *Python Programming for Data Science* kursuna dayanmaktadır.
