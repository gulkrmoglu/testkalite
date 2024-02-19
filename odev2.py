# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacci=[1,1]
i=2 
while i<20:
          fibonacci.append(fibonacci[-1]+ fibonacci[-2])
          i+=1
print(fibonacci)

# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

sayi= int(input("Lütfen bir sayi giriniz: "))
carpanToplam=0
i=1
while i<sayi:
     if sayi%i==0:
          carpanToplam+=i
     i+=1
if sayi==carpanToplam:
     print("Tebrikler mükemmel sayıyı buldunuz.")          
else:
     print ("Yeni bir sayı ile deneyiniz")
    
# 3- Kullanıcıdan alınan sayıların Ebob ve Ekokunu bulunuz.
     
import math 
birinciSayi = int(input("Birinci sayiyi giriniz:"))
ikinciSayi = int(input("İkinci sayiyi giriniz: "))

ebob = math.gcd (birinciSayi, ikinciSayi)
ekok = (birinciSayi*ikinciSayi)/ebob

print ("EBOB:", ebob)
print ("EKOK:", ekok)

# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
     
sayi = int(input("Lütfen bir sayı giriniz:"))
if sayi>1:

    for i in range(2,sayi):
        if sayi%i == 0:
            print("Asal sayı değildir.")
            break
    else:
        print("Asal sayıdır.")
else:
    print("Asal sayı değildir.")


# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
     
sayi= int(input("Lütfen asal çarpanlarını bulmak istediğiniz sayıyı giriniz: "))
asalCarpan=[]
i=2
while i<=sayi:
      if sayi%i==0:
          asalCarpan.append(i)
          sayi//=i
      else:
       i+=1
print(asalCarpan)




