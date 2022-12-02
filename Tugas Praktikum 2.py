#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
while( True ) : 
    start = input("\nKetik [mulai] :")
    while(start!= "mulai" ) :
        start = input ("\nMaaf inputan anda salah. Silahkan coba lagi.\n")
    if start == "mulai" :
        kesempatan = 8
        angka_random = random.randint(1,50)
    print ( "\nKesempatan menebak :", kesempatan, "\nAnda harus memilih angka antara 1 dan 50\n" )
    while (kesempatan >= 0) :
        if kesempatan == 0 :
            print("Angkanya :", angka_random)
            print("Maaf anda belum beruntung")
            break
        else :
            
            angka_tebakan = int(input("Masukkan angka : "))
            if angka_tebakan == angka_random :
                print("anda Benar: angka tebakan adalah :", angka_tebakan)
                break
            elif angka_tebakan > angka_random :
                 print("\nAngkanya di bawah", angka_tebakan)
                 kesempatan -=1
            elif angka_tebakan < angka_random :
                 print("\nAngkanya di atas", angka_tebakan)
                 kesempatan -=1
        print("\nKesempatan menebak :", kesempatan)

    #konfirmasi ulang
    ulang = input("\nMau main lagi? [ya/tidak]: \n")
    while( ulang != "ya" and ulang != "tidak") :
        ulang = input("Maaf inputan anda salah. \nSilahkan coba lagi.\nMau main lagi? : ")

    if ulang == "ya" :
        print("\nSilahkan main lagi.\n")
    elif ulang == "tidak" :
        print("\nTerimakasih sudah main.\n")
        break


# In[ ]:




