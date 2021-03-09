#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import mods
import time as bekle
import colorama
from colorama import Fore, Back, Style
import webbrowser

maincount = 1

os.system("clear")

try:
    os.system("clear")
    while(maincount<2):
        mods.banner()
        print("""
\033[1;31m1) \033[1;37mCewl Aracı(Eksikleri Var)  
\033[1;31m2) \033[1;37mCrunch Aracı
\033[1;31m3) \033[1;37mTHC-HYDRA Aracı  
\033[1;31m4) \033[1;37mJohn The Ripper Aracı
\033[1;31m5) \033[1;37mMedusa Aracı
\033[1;34m6) \033[1;36mKomutlar
\033[1;31m7) \033[1;37mSitemiz 
\033[1;31m""")
        secim = input("rht>\033[1;37m ")
        if secim == "exit":
            sys.exit()
        elif secim == "home":
            os.system("clear")
        elif secim == "clear":
            os.system("clear")
        elif secim == "1":
            os.system("clear")
            count=1
            while(count<2):
                mods.banner()
                print("""
\033[1;31m1) \033[1;37mNormal WordList Oluşturma  
\033[1;31m2) \033[1;37mNormal WordList Oluşturma(Proxyli)
\033[1;31m3) \033[1;37mSitedeki Mail Adreslerini Tarar
\033[1;31m4) \033[1;37mSitedeki Mail Adreslerini Tarar(Proxyli)
\033[1;31m5) \033[1;37mSitedeki Meta Verileri Toplar
\033[1;31m6) \033[1;37mSitedeki Meta Verileri Toplar(Proxyli)
\033[1;31m7) \033[1;37mSitenin Login Panelinden WordList Oluşturur
\033[1;31m8) \033[1;37mSitenin Login Panelinden WordList Oluşturur(Proxyli) 
\033[1;31m """)
                a = input("rht>\033[1;37m ")
                if a == "home":
                    os.system("clear")
                    count+=1
                elif a == "clear":
                    os.system("clear")
                elif a == "exit":
                    sys.exit()
                elif a == "1":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31m rht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    mods.normalword(derinlik,uzunluk,link,kayit)
                elif a == "2":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31m rht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxy = input("""
\033[1;33mProxy Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxyport = input("""
\033[1;33mProxynin Portu  Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    yesorno = input("""
\033[1;33mProxyde Username Ya Da Şifresi Var mı(y/n)  

\033[1;31mrht>\033[1;37m """)
                    if yesorno == "y" or yesorno == "Y":
                        mods.normalworldproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"y")
                    elif yesorno == "n" or yesorno == "N":
                        mods.normalworldproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"n")
                    elif yesorno == "exit":
                        sys.exit()
                    elif yesorno == "home":
                        count+=1
                    elif yesorno == "clear":
                        os.system("clear")
                    else:
                        print("Geçersiz Argüman")
                        continue
                elif a == "3":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31m rht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    mods.emailworld(derinlik,uzunluk,link,kayit)
                elif a == "4":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxy = input("""
\033[1;33mProxy Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxyport = input("""
\033[1;33mProxynin Portu  Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    yesorno = input("""
\033[1;33mProxyde Username Ya Da Şifresi Var mı(y/n)  

\033[1;31mrht>\033[1;37m  """)
                    if yesorno == "y" or yesorno == "Y":
                        mods.emailworldproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"y")
                    elif yesorno == "n" or yesorno == "N":
                        mods.emailworldproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"n")
                    elif yesorno == "exit":
                        sys.exit()
                    elif yesorno == "home":
                        count+=1
                    elif yesorno == "clear":
                        os.system("clear")
                    else:
                        print("Geçersiz Argüman")
                        continue
                elif a == "5":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    mods.metadump(derinlik,uzunluk,link,kayit)
                elif a == "6":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31m rht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxy = input("""
\033[1;33mProxy Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxyport = input("""
\033[1;33mProxynin Portu  Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    yesorno = input("""
\033[1;33mProxyde Username Ya Da Şifresi Var mı(y/n)  

\033[1;31mrht>\033[1;37m """)
                    if yesorno == "y" or yesorno == "Y":
                        mods.normalworldproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"y")
                    elif yesorno == "n" or yesorno == "N":
                        mods.normalworldproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"n")
                    elif yesorno == "exit":
                        sys.exit()
                    elif yesorno == "home":
                        count+=1
                    elif yesorno == "clear":
                        os.system("clear")
                    else:
                        print("Geçersiz Argüman")
                        continue
                elif a == "3":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31m rht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    mods.emailworld(derinlik,uzunluk,link,kayit)
                elif a == "4":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxy = input("""
\033[1;33mProxy Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxyport = input("""
\033[1;33mProxynin Portu  Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    yesorno = input("""
\033[1;33mProxyde Username Ya Da Şifresi Var mı(y/n)  

\033[1;31mrht>\033[1;37m  """)
                    if yesorno == "y" or yesorno == "Y":
                        mods.metadumpproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"y")
                    elif yesorno == "n" or yesorno == "N":
                        mods.metadumpproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"n")
                    elif yesorno == "home":
                        count+=1
                    elif yesorno == "exit":
                        sys.exit()
                    elif yesorno == "clear":
                        os.system("clear")
                    else:
                        print("Geçersiz Seçim")

                elif a == "7":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    mods.authdump(derinlik,uzunluk,link,kayit)
                    

                elif a == "8":
                    os.system("clear")
                    mods.banner()
                    derinlik = input("""
\033[1;33mDerinlik Oranını Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    uzunluk = input("""
\033[1;33mKelime uzunluğunu giriniz

\033[1;31mrht>\033[1;37m  """)
                    link = input("""
\033[1;33mHedef Linki Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    kayit = input("""
\033[1;33mKayıt edilecek dosyanın adını giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxy = input("""
\033[1;33mProxy Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    proxyport = input("""
\033[1;33mProxynin Portu  Giriniz 

\033[1;31mrht>\033[1;37m  """)
                    yesorno = input("""
\033[1;33mProxyde Username Ya Da Şifresi Var mı(y/n)  

\033[1;31mrht>\033[1;37m  """)
                    if yesorno == "y" or yesorno == "Y":
                        mods.authdupproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"y")
                    elif yesorno == "n" or yesorno == "N":
                        mods.authdupproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,"n")
                    elif yesorno == "home":
                        count+=1
                    elif yesorno == "exit":
                        sys.exit()
                    elif yesorno == "clear":
                        os.system("clear")
                    else:
                        print("Geçersiz Argüman")
        elif secim== "2":
            os.system("clear")
            count2 = 1
            while(count2<2):
                mods.banner()
                minimum = input("""
\033[1;33mMinimum Hangi Uzunlukta Olmasını İstiyorsunuz?

\033[1;31mrht>\033[1;37m """)
                maksimum = input("""
\033[1;33mMaksimum Hangi Uzunlukta Olmasını İstiyorsunuz?

\033[1;31mrht>\033[1;37m """)
                hangikarakterler = input("""
\033[1;33mHangi Karakterler Ya Da Sayıların Dahil Olmasını İsterseniz?

\033[1;31mrht>\033[1;37m """)
                kayit2 = input("""
\033[1;33mKaydedilecek dosyanın adını giriniz

\033[1;31mrht>\033[1;37m """)
                mods.crunch(minimum,maksimum,hangikarakterler,kayit2)
                count2+=1

        elif secim == "3":
            os.system("clear")
            count3 = 1
            while(count3<2):
                mods.banner()
                print("""
\033[1;31m1) \033[1;37mLogin Paneli İçin Brute Force  
\033[1;31m2) \033[1;37mSSH Servisine Brute Force
\033[1;31m3) \033[1;37mFTP Servisine Brute
\033[1;31m4) \033[1;37mRDP Servisine Atak
\033[1;31m5) \033[1;37mVNC Servisine Atak
\033[1;31m6) \033[1;37mTelnet Servisine Atak
\033[1;31m7) \033[1;37mHTTP Basic Auth Korumalı Sitelere Yönelik Brute Force
\033[1;31m8) \033[1;37mFirewall Brute Force,Usernamesiz(cisco AAA)
\033[1;31m9) \033[1;37mFirewall Brute Force , Usernameli(cisco AAA)
\033[1;31m10) \033[1;37mSMB Servisine Atak
\033[1;31m11) \033[1;37mSNMP Servisine Atak
\033[1;31m12) \033[1;37mSNMP ATAK(ENCODING EDITION)
\033[1;31m13) \033[1;37mIMAP Servisine Atak
\033[1;31m """)
                b = input("rht>\033[1;37m ")
                if b == "home":
                    os.system("clear")
                    count3+=1
                elif b == "exit":
                    sys.exit()
                elif b == "clear":
                    os.system("clear")
                elif b == "1":
                    os.system("clear")
                    mods.banner()
                   

                    useradet = input("""
\033[1;33mUser Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                    if useradet == "home":
                        os.system("clear")
                        count3+=1
                    elif useradet == "exit":
                        sys.exit()
                    elif useradet == "clear":
                        os.system("clear")
                    elif useradet == "y":
                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            user = input("""
\033[1;33mKullanıcı Adı Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            paneldizini = input("""
\033[1;33mSitede Login Panelinin Dizinini Giriniz

\033[1;31mrht>\033[1;37m """)
                            userform = input("""
\033[1;33mFormda ki kullanıcı adı alanına verilen isim nedir(örneğin : username)

\033[1;31mrht>\033[1;37m """)
                            passform = input("""
\033[1;33mFormda ki şifre alanına verilen isim nedir(örneğin : password)

\033[1;31mrht>\033[1;37m """)
                            failmessage = input("""
\033[1;33mYanlış Giriliğinde Gelen Hata Mesajını Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.panelbrute(user,passlists,target,userform,passform,failmessage,2,1,paneldizini)
                        else:
                            user = input("""
\033[1;33mKullanıcı Adı Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifre Barındıran Wordlistin Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            paneldizini = input("""
\033[1;33mSitede Login Panelinin Dizinini Giriniz

\033[1;31mrht>\033[1;37m """)
                            userform = input("""
\033[1;33mFormda ki kullanıcı adı alanına verilen isim nedir(örneğin : username)

\033[1;31mrht>\033[1;37m """)
                            passform = input("""
\033[1;33mFormda ki şifre alanına verilen isim nedir(örneğin : password)

\033[1;31mrht>\033[1;37m """)
                            failmessage = input("""
\033[1;33mYanlış Giriliğinde Gelen Hata Mesajını Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.panelbrute(user,passlists,target,userform,passform,failmessage,2,2,paneldizini)
                                


                            
                    else:
                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            user = input("""
\033[1;33mKullanıcı Adı Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            paneldizini = input("""
\033[1;33mSitede Login Panelinin Dizinini Giriniz

\033[1;31mrht>\033[1;37m """)
                            userform = input("""
\033[1;33mFormda ki kullanıcı adı alanına verilen isim nedir(örneğin : username)

\033[1;31mrht>\033[1;37m """)
                            passform = input("""
\033[1;33mFormda ki şifre alanına verilen isim nedir(örneğin : password)

\033[1;31mrht>\033[1;37m """)
                            failmessage = input("""
\033[1;33mYanlış Giriliğinde Gelen Hata Mesajını Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.panelbrute(user,passlists,target,userform,passform,failmessage,2,1,paneldizini)
                        else:
                            user = input("""
\033[1;33mKullanıcı Adını Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifre Barındıran Wordlistin Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            paneldizini = input("""
\033[1;33mSitede Login Panelinin Dizinini Giriniz

\033[1;31mrht>\033[1;37m """)
                            userform = input("""
\033[1;33mFormda ki kullanıcı adı alanına verilen isim nedir(örneğin : username)

\033[1;31mrht>\033[1;37m """)
                            passform = input("""
\033[1;33mFormda ki şifre alanına verilen isim nedir(örneğin : password)

\033[1;31mrht>\033[1;37m """)
                            failmessage = input("""
\033[1;33mYanlış Giriliğinde Gelen Hata Mesajını Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.panelbrute(user,passlists,target,userform,passform,failmessage,1,2,paneldizini)
                                
                       
                                

                        












                        
                        








                        
                            
                elif b == "2":
                    os.system("clear")
                    mods.banner()
                   

                    useradet = input("""
\033[1;33mUser Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                    if useradet == "home":
                        os.system("clear")
                        count3+=1
                    elif useradet == "clear":
                        os.system("clear")
                    elif useradet == "exit":
                        sys.exit()
                    elif useradet == "y":
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.sshbrute(user,passlists,target,2,1)
                            

                        else:
                            user = input("""
\033[1;33mKullanıcı Adı Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifre Barındıran Wordlistin Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.sshbrute(user,passlists,target,2,2)
                            

                    else:
                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            user = input("""
\033[1;33mKullanıcı Adını Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.sshbrute(user,passlists,target,1,1)
                            

                        else:
                            user = input("""
\033[1;33mKullanıcı Adını Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifre Barındıran Wordlistin Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.sshbrute(user,passlists,target,1,2)
                            

                elif b == "3":
                    os.system("clear")
                    mods.banner()
                   

                    useradet = input("""
\033[1;33mUser Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                    if useradet == "home":
                        os.system("clear")
                        count3+=1
                    elif useradet == "clear":
                        os.system("clear")
                    elif useradet == "exit":
                        sys.exit()
                    elif useradet == "y":
                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            user = input("""
\033[1;33mKullanıcı Adı Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.ftpbrute(user,passlists,target,2,1)
                            

                        else:
                            user = input("""
\033[1;33mKullanıcı Adı Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifre Barındıran Wordlistin Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.ftpbrute(user,passlists,target,2,2)
                            

                    else:
                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            user = input("""
\033[1;33mKullanıcı Adını Giriniz

\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.ftpbrute(user,passlists,target,1,1)
                            

                        else:
                            user = input("""
\033[1;33mKullanıcı Adını Giriniz
\033[1;31mrht>\033[1;37m """)
                            passlists = input("""
\033[1;33mŞifre Barındıran Wordlistin Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedef Siteyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.ftpbrute(user,passlists,target,1,2)
                            
                elif b == "4":
                    os.system("clear")
                    mods.banner()

                    passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                    if passadet == "home":
                        os.system("clear")
                        count3+=1
                    elif passadet == "exit":
                        sys.exit()
                    elif passadet == "clear":
                        os.system("clear")
                    elif passadet == "n":
                        os.system("clear")
                        mods.banner()
                        target = input("""
\033[1;33mHedef RDP Serveri Giriniz

\033[1;31mrht>\033[1;37m """)
                        port = input("""
\033[1;33mHedef RDP Serverin Portunu Giriniz

\033[1;31mrht>\033[1;37m """)
                        wordlist = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                        mods.rdpatak(wordlist,port,target,1)
                    
                    
                    
                    else:
                        os.system("clear")
                        mods.banner()
                        target = input("""
\033[1;33mHedef RDP Serveri Giriniz

\033[1;31mrht>\033[1;37m """)
                        port = input("""
\033[1;33mHedef RDP Serverin Portunu Giriniz

\033[1;31mrht>\033[1;37m """)
                        wordlist = input("""
\033[1;33mŞifreyi Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                        mods.rdpatak(wordlist,port,target,2)
                    

                elif b == "5":
                    os.system("clear")
                    mods.banner()

                    passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                    if passadet == "home":
                        os.system("clear")
                        count3+=1
                    elif passadet == "exit":
                        sys.exit()
                    elif passadet == "clear":
                        os.system("clear")
                    elif passadet == "n":
                        os.system("clear")
                        mods.banner()
                        target = input("""
\033[1;33mHedef RDP Serveri Giriniz

\033[1;31mrht>\033[1;37m """)
                        port = input("""
\033[1;33mHedef RDP Serverin Portunu Giriniz

\033[1;31mrht>\033[1;37m """)
                        wordlist = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                        mods.vncatak(wordlist,port,target,1)
                    
                    
                    
                    else:
                        os.system("clear")
                        mods.banner()
                        target = input("""
\033[1;33mHedef RDP Serveri Giriniz

\033[1;31mrht>\033[1;37m """)
                        port = input("""
\033[1;33mHedef RDP Serverin Portunu Giriniz

\033[1;31mrht>\033[1;37m """)
                        wordlist = input("""
\033[1;33mŞifre Lİstesini Giriniz

\033[1;31mrht>\033[1;37m """)
                        mods.vncatak(wordlist,port,target,2)
                #Telnet Atak
                elif b == "6":
                    os.system("clear")
                    mods.banner()
                   

                    useradet = input("""
\033[1;33mUser Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                    if useradet == "home":
                        os.system("clear")
                        count3+=1
                    elif useradet == "exit":
                        sys.exit()
                    elif useradet == "clear":
                        os.system("clear")
                    elif useradet == "y":
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "n":
                            os.system("clear")
                            mods.banner()
                            target = input("""
\033[1;33mTelnet Serverin Hedefini Giriniz

\033[1;31mrht>\033[1;37m """)
                            port = input("""
\033[1;33mTelnet Serverin Portu Giriniz

\033[1;31mrht>\033[1;37m """)
                            username = input("""
\033[1;33mUsername Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.telnetatak(username,password,port,target,2,1)



                        else:
                            target = input("""
\033[1;33mTelnet Serverin Hedefini Giriniz

\033[1;31mrht>\033[1;37m """)
                            port = input("""
\033[1;33mTelnet Serverin Portu Giriniz

\033[1;31mrht>\033[1;37m """)
                            username = input("""
\033[1;33mUsername Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.telnetatak(username,password,port,target,2,2)



                    else:
                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "n":
                            target = input("""
\033[1;33mTelnet Serverin Hedefini Giriniz

\033[1;31mrht>\033[1;37m """)
                            port = input("""
\033[1;33mTelnet Serverin Portu Giriniz

\033[1;31mrht>\033[1;37m """)
                            username = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.telnetatak(username,password,port,target,1,1)



                        else:
                            target = input("""
\033[1;33mTelnet Serverin Hedefini Giriniz

\033[1;31mrht>\033[1;37m """)
                            port = input("""
\033[1;33mTelnet Serverin Portu Giriniz

\033[1;31mrht>\033[1;37m """)
                            username = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.telnetatak(username,password,port,target,1,2)

                        
                        




                        
                #Http Basic Brute Force
                elif b == "7":
                    os.system("clear")
                    mods.banner()
                   

                    useradet = input("""
\033[1;33mUser Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                    if useradet == "home":
                        os.system("clear")
                        count3+=1
                    elif useradet == "clear":
                        os.system("clear")
                    elif useradet == "exit":
                        sys.exit()
                    elif useradet == "y":
                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "n":
                            target = input("""
\033[1;33mHedef Linki Giriniz

\033[1;31mrht>\033[1;37m """)
                            username = input("""
\033[1;33mUsername Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.basicauth(username,password,target,2,1)
                        else:
                            target = input("""
\033[1;33mHedef Linki Giriniz

\033[1;31mrht>\033[1;37m """)
                            username = input("""
\033[1;33mUsername Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.basicauth(username,password,target,2,2)

                    else:

                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "n":
                            target = input("""
\033[1;33mHedef Linki Giriniz

\033[1;31mrht>\033[1;37m """)
                            username = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.basicauth(username,password,target,1,1)
                        else:
                            target = input("""
\033[1;33mHedef Linki Giriniz

\033[1;31mrht>\033[1;37m """)
                            username = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.basicauth(username,password,target,1,2)
                        
                        
                        

                    



                elif b == "8":
                        os.system("clear")
                        mods.banner()
                        passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count3+=1
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "n":
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            port = input("""
\033[1;33mPortu Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.firewallbrute(password,target,1,port)
                        else:
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            port = input("""
\033[1;33mPortu Giriniz

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.firewallbrute(password,target,2,port)

                elif b == "9":
                        os.system("clear")
                        mods.banner()
                        useradet = input("""
\033[1;33mEğer Kullanıcı Adı Denemeniz Birden Fazla Olcaksa y'ye basın ama tek olacaksa n'ye basın [Varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                        if useradet == "home":
                            os.system("clear")
                            count3+=1
                        elif useradet == "exit":
                            sys.exit()
                        elif useradet == "clear":
                            os.system("clear")
                        elif useradet == "y":
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.firewallbrutepass(user,pasword,target,2,1)
                            else:
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.firewallbrutepass(user,pasword,target,2,2)

                
                        else:
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUsernameyi Giriniz
\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.firewallbrutepass(user,pasword,target,1,1)
                            else:
                                user = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.firewallbrutepass(user,pasword,target,1,2)





                elif b == "10":
                        os.system("clear")
                        mods.banner()
                        useradet = input("""
\033[1;33mEğer Kullanıcı Adı Denemeniz Birden Fazla Olcaksa y'ye basın ama tek olacaksa n'ye basın [Varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                        if useradet == "home":
                            os.system("clear")
                            count3+=1
                        elif useradet == "exit":
                            sys.exit()
                        elif useradet == "clear":
                            os.system("clear")
                        elif useradet == "y":
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.smbatak(user,pasword,target,2,1)
                            else:
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.smbatak(user,pasword,target,2,2)

                
                        else:
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUsernameyi Giriniz
\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.smbatak(user,pasword,target,1,1)
                            else:
                                user = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.smbatak(user,pasword,target,1,2)
                    





                elif b == "11":
                        os.system("clear")
                        mods.banner()
                        useradet = input("""
\033[1;33mEğer Kullanıcı Adı Denemeniz Birden Fazla Olcaksa y'ye basın ama tek olacaksa n'ye basın [Varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                        if useradet == "home":
                            os.system("clear")
                            count3+=1
                        elif useradet == "exit":
                            sys.exit()
                        elif useradet == "clear":
                            os.system("clear")
                        elif useradet == "y":
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.snmpbrute(user,pasword,target,2,1)
                            else:
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.snmpbrute(user,pasword,target,2,2)

                
                        else:
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUsernameyi Giriniz
\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.snmpbrute(user,pasword,target,1,1)
                            else:
                                user = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.snmpbrute(user,pasword,target,1,2)
                    





                elif b == "12":
                        os.system("clear")
                        mods.banner()
                        useradet = input("""
\033[1;33mEğer Kullanıcı Adı Denemeniz Birden Fazla Olcaksa y'ye basın ama tek olacaksa n'ye basın [Varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                        if useradet == "home":
                            os.system("clear")
                            count3+=1
                        elif useradet == "exit":
                            sys.exit()
                        elif useradet == "clear":
                            os.system("clear")
                        elif useradet == "y":
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.snmpencode(user,pasword,target,2,1)
                            else:
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.snmpencode(user,pasword,target,2,2)

                
                        else:
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUsernameyi Giriniz
\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.snmpencode(user,pasword,target,1,1)
                            else:
                                user = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.snmpencode(user,pasword,target,1,2)
                    








                elif b == "13":
                        os.system("clear")
                        mods.banner()
                        useradet = input("""
\033[1;33mEğer Kullanıcı Adı Denemeniz Birden Fazla Olcaksa y'ye basın ama tek olacaksa n'ye basın [Varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                        if useradet == "home":
                            os.system("clear")
                            count3+=1
                        elif useradet == "exit":
                            sys.exit()
                        elif useradet == "clear":
                            os.system("clear")
                        elif useradet == "y":
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.imapbrute(user,pasword,target,2,1)
                            else:
                                user = input("""
\033[1;33mUser name Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.imapbrute(user,pasword,target,2,2)

                
                        else:
                            os.system("clear")
                            mods.banner()

                            passadet = input("""
\033[1;33mŞifre Sayısı birden fazla mı?(y/n) [varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                            if passadet == "home":
                                os.system("clear")
                                count3+=1
                            elif passadet == "exit":
                                sys.exit()
                            elif passadet == "clear":
                                os.system("clear")
                            elif passadet == "n":
                                user = input("""
\033[1;33mUsernameyi Giriniz
\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifreyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.imapbrute(user,pasword,target,1,1)
                            else:
                                user = input("""
\033[1;33mUsernameyi Giriniz

\033[1;31mrht>\033[1;37m """)
                                pasword = input("""
\033[1;33mŞifre Listesini Giriniz

\033[1;31mrht>\033[1;37m """)
                                target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                                mods.imapbrute(user,pasword,target,1,2)
                    








                else:
                    print("Geçersiz Argüman")
                
        elif secim == "4":
            os.system("clear")
            count4 = 1
            mods.banner()
            while(count4<2):
                
                
                print("""
\033[1;31m1) \033[1;37mPasswd Ve Shadow Dosyalarını Çeker
\033[1;31m2) \033[1;37mPasswd Ve SHadow Dosyalarını Alır, Birleştirir Ve Kullanıcıların Şiresini Çalar
\033[1;31m3) \033[1;37mMD5 Şifre Kırıcı
\033[1;31m4) \033[1;37mHASH Tipini Tespit Edip Ona göre kırma işlemi yapar
\033[1;31m5) \033[1;37mDaha Fazla Şifreleme Tipi Kullanmak İstiyorsanız
\033[1;31m""")
                c = input("rht>\033[1;37m ")
                if c == "home":
                    os.system("clear")
                    count4+=1
                elif c == "exit":
                    sys.exit()
                elif c == "clear":
                    os.system("clear")
                elif c == "1":
                    mods.dumppassshadow()
                elif c == "2":
                    shadow = input("""
\033[1;33mShadow Dosyasının Konumunu Giriniz

\033[1;31mrht>\033[1;37m """)
                    passwd = input("""
\033[1;33mPasswd Dosyasının Konumunu Giriniz

\033[1;31mrht>\033[1;37m """)
                    kayit = input("""
\033[1;33mDosyanın Kaydedilecek Adını Giriniz

\033[1;31mrht>\033[1;37m """)
                    mods.birlestirvekir(passwd,shadow,kayit) 
                elif c == "3":
                    dosyayolu = input("""
\033[1;33mDosya Yolunu Giriniz

\033[1;31mrht>\033[1;37m """)
                    mods.md5pass(dosyayolu)
                elif c == "4":
                    dosyayolu = input("""
\033[1;33mDosya Yolunu Giriniz

\033[1;31mrht>\033[1;37m """)
                    mods.unkwonpass(dosyayolu)
                elif c == "5":
                    dosyayolu = input("""
\033[1;33mDosya Yolunu Giriniz

\033[1;31mrht>\033[1;37m """)
                    mods.secimpass(dosyayolu)

                else:
                    print("Geçersiz Argüman")
                
                
        
                mods.banner()

        elif secim == "6":
            print("""
1)Çıkış yapmak için : "exit" 
2)Ana sayfaya dönmek için : "home" 
3)Ekranı Temizlemek İçin : "clear" """)
            bekle.sleep(3)
        elif secim == "7":
            
            print("Site Açılıyor")
            bekle.sleep(1)
            mods.redhackaze()
            bekle.sleep(3)
            os.system("clear")
        elif secim == "5":
            os.system("clear")
            count7 = 1
            while(count7<2):
                mods.banner()
                print("""
\033[1;31m1) \033[1;37mFTP Servisine Atak
\033[1;31m2) \033[1;37mSSH Servisine Atak
\033[1;31m3) \033[1;37mSMTP Servisine Atak
\033[1;31m""")
                d = input("rht>\033[1;37m ")
                if d == "home":
                    os.system("clear")
                    count7+=1
                elif d == "exit":
                    sys.exit()
                elif d == "clear":
                    os.system("clear")

                #FTP Brute    
                elif d == "1":
                    os.system("clear")
                    mods.banner()
                    useradet = input("""
\033[1;33mEğer Birden Fazla Kullanıcı Adı Deneycek İseniz y'ye basın tam tersini istiyorsanız n'ye basın [Varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                    if useradet == "y" or useradet == "y":
                        passadet = input("""
\033[1;33mEğer Birden Fazla Şifre Deniycek İseniz y'ye Tek Bir Şifre Deneyecek İseniz n'ye basın [Varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count7+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPaswordu Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.ftpbrutemedusa(user,password,2,1,a=target)
                        else:
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPasword Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.ftpbrutemedusa(user,password,2,2,a=target)

                    elif useradet == "home":
                        os.system("clear")
                        count7+=1
                    elif useradet == "clear":
                        os.system("clear")
                    elif useradet == "exit":
                        sys.exit()
                    else:
                        passadet = input("""
\033[1;33mEğer Birden Fazla Şifre Deniycek İseniz y'ye Tek Bir Şifre Deneyecek İseniz n'ye basın [Varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count7+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPaswordu Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.ftpbrutemedusa(user,password,1,1,a=target)
                        else:
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPasword Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.ftpbrutemedusa(user,password,1,2,a=target)
                        




                        

                #SSH Brute                                                                                                                        
                elif d == "2":
                    os.system("clear")
                    mods.banner()
                    useradet = input("""
\033[1;33mEğer Birden Fazla Kullanıcı Adı Deneycek İseniz y'ye basın tam tersini istiyorsanız n'ye basın [Varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                    if useradet == "y" or useradet == "y":
                        passadet = input("""
\033[1;33mEğer Birden Fazla Şifre Deniycek İseniz y'ye Tek Bir Şifre Deneyecek İseniz n'ye basın [Varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count7+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPaswordu Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.medusashhbrute(user,password,2,1,a=target)
                        else:
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPasword Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.medusashhbrute(user,password,2,2,a=target)

                    elif useradet == "home":
                        os.system("clear")
                        count7+=1
                    elif useradet == "clear":
                        os.system("clear")
                    elif useradet == "exit":
                        sys.exit()
                    else:
                        passadet = input("""
\033[1;33mEğer Birden Fazla Şifre Deniycek İseniz y'ye Tek Bir Şifre Deneyecek İseniz n'ye basın [Varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count7+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPaswordu Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.medusashhbrute(user,password,1,1,a=target)
                        else:
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPasword Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.medusashhbrute(user,password,1,2,a=target)
                        
                    




                #SMTP BRUTE
                elif d == "3":
                    os.system("clear")
                    mods.banner()
                    useradet = input("""
\033[1;33mEğer Birden Fazla Kullanıcı Adı Deneycek İseniz y'ye basın tam tersini istiyorsanız n'ye basın [Varsayılan : "n" ]

\033[1;31mrht>\033[1;37m """)
                    if useradet == "y" or useradet == "y":
                        passadet = input("""
\033[1;33mEğer Birden Fazla Şifre Deniycek İseniz y'ye Tek Bir Şifre Deneyecek İseniz n'ye basın [Varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count7+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPaswordu Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.medusasmtpbrute(user,password,2,1,a=target)
                        else:
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPasword Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.medusasmtpbrute(user,password,2,2,a=target)

                    elif useradet == "home":
                        os.system("clear")
                        count7+=1
                    elif useradet == "clear":
                        os.system("clear")
                    elif useradet == "exit":
                        sys.exit()
                    else:
                        passadet = input("""
\033[1;33mEğer Birden Fazla Şifre Deniycek İseniz y'ye Tek Bir Şifre Deneyecek İseniz n'ye basın [Varsayılan : "y" ]

\033[1;31mrht>\033[1;37m """)
                        if passadet == "home":
                            os.system("clear")
                            count7+=1
                        elif passadet == "exit":
                            sys.exit()
                        elif passadet == "clear":
                            os.system("clear")
                        elif passadet == "n":
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPaswordu Giriniz

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.medusasmtpbrute(user,password,1,1,a=target)
                        else:
                            os.system("clear")
                            mods.banner()
                            user = input("""
\033[1;33mKullanıcı Adı Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            password = input("""
\033[1;33mPasword Listesinin Bulunduğu Dosyanın Yolunu Yazınız

\033[1;31mrht>\033[1;37m """)
                            target = input("""
\033[1;33mHedefi Giriniz

\033[1;31mrht>\033[1;37m """)
                            mods.medusasmtpbrute(user,password,1,2,a=target)
        else:
            print("Geçersiz Seçim")
            bekle.sleep(2)
            os.system("clear")
                                            
except KeyboardInterrupt:
    print("""
Görüşmek üzere""")
except ImportError:
    print("Kütüphane hatası")
except ImportWarning:
    print("Kütüphane Hatası")
except OSError:
    print("Linux/Unix desteklemektedir")
        

            