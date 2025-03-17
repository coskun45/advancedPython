# for döngülerin kisa ve etkili hali

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cift_sayilar = [sayi for sayi in sayilar if sayi %2==0]

print(cift_sayilar)



birden_yüze_liste = [i for i in range(1,100) if i %2==0]
print(birden_yüze_liste)

text = "Python Ögreniyorum"

kücük_harf = [i.upper() for i in text ]
print(kücük_harf)