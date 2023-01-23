
try:
    a = int(input("masukan angka pertama "))
    b = int(input("masukkan angka kedua "))
    print("hasil perkalian nya adalah", a*b)
    
except ZeroDivisionError:
    print("akan eror jika selain angka")