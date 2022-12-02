import random
#Cerita Berantai

#WAKTU CERITA
kalimat_starter = random.randint(1,4)
if kalimat_starter == 1:
    kalimat1 = ("Pada suatu pagi yang cerah, ")
elif kalimat_starter == 2:
    kalimat1 = ("Ditengah teriknya matahari, ")
elif kalimat_starter == 3:
    kalimat1 = ("Di kala sore menerpa, ")
else:
    kalimat1 = ("Di tengah gelapnya malam, ")

#KARAKTER UTAMA
karakter = random.randint(1,4)
if karakter == 1:
    karakter1 = ("Rudi yang tengah kelelelahan ")
elif karakter == 2:
    karakter1 = ("Andi yang sedang bersemangat ")
elif karakter == 3:
    karakter1 = ("Rani yang moodnya sedang rusak ")
else:
    karakter1 = ("Ayu yang sangat bergembira ")

#HARI CERITA
waktu = random.randint(1,4)
if waktu == 1:
    waktu1 = ("Senin ")
elif waktu == 2:
    waktu1 = ("Rabu ")
elif waktu == 3:
    waktu1 = ("Jumat ")
else:
    waktu1 = ("Kamis ")

#PLOT CERITA
story_plot = random.randint(1,4)
if story_plot == 1:
    story_plot1 = ("Mereka berbelanja bersama di ")
elif story_plot == 2:
    story_plot1 = ("Mereka mengerjakan proyek tugas akhir mereka di ")
elif story_plot == 3:
    story_plot1 = ("Mereka makan dadar gulung bersama di ")
else:
    story_plot1 = ("Mereka bermain bulu tangkis di ")

#TEMPAT CERITA
tempat = random.randint(1,4)
if tempat == 1:
    tempat1 = ("Pasar Pondok Labu")
elif tempat == 2:
    tempat1 = ("Taman Cilandak")
elif tempat == 3:
    tempat1 = ("alun-alun kota Bandung")
else:
    tempat1 = ("halaman rumah Presiden")

#KARAKTER KEDUA
second_character = random.randint(1,4)
if second_character == 1:
    second_character1 = ("Amina")
elif second_character == 2:
    second_character1 = ("Damar")
elif second_character == 3:
    second_character1 = ("Sulis")
else:
    second_character1 = ("Yanto")

print (kalimat1, karakter1, "bertemu dengan ", second_character1, ". ", story_plot1, tempat1, ".")