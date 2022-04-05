import turtle
import random
from  colorama import *
print(" Sayı Bilme Oyununa Hoşgeldiniz")
x=int(input("Sayı Giriniz==>:"))
z=random.randint(1,15)

if x==z:
    print("Sayılar eşit sayıyı bildiniz tebrikler!!:",x)
    print("Tahmin Edilen Sayı:",z)

elif x>z:
    print(Fore.RED)
    print("Girdiğiniz Sayı Daha  Küçük Az Kaldı Sayıyı Bulucaksın:",x)
    print("Bulman  Gereken Sayı Buydu :",z)

elif z>x:
    print(Fore.GREEN)
    print("Girdiğiniz Sayı Daha Büyük Biraz Daha Yükseltebilirsin Sayıyı :))",x)
    print("Bulman Gereken Sayı Buydu :",z)


