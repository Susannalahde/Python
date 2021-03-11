# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Susanna Lähde
# Opiskelijanumero: 0570397
# Päivämäärä: 18.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: 

#Tuodaan moduulit

import datetime
import sys
import numpy 

#Määritellään luokka

class TIEDOT():
    paisteaika = 0
    paivamaara = ""
    nimi = ""
    vuosiluku = ""
    tunnit = ""
    kuukausi = ""
    paiva = ""
    vuosi = ""

#Ensimmäinen aliohjelma pyytää käyttäjältä valintaa siitä, mitä hän haluaa tehdä.

def Valikko():
    print("Mitä haluat tehdä:")
    print("1) Anna havaintoasema ja vuosi")
    print("2) Lue säätilatiedosto")
    print("3) Analysoi päivittäiset säätilatiedot")
    print("4) Tallenna päivittäiset säätilatiedot")
    print("5) Lue Ilmatieteen laitoksen tiedosto")
    print("6) Analysoi kuukausittaiset säätilatiedot")
    print("7) Tallenna kuukausittaiset säätilatiedot")
    print("8) Analysoi tuntikohtaiset säätilatiedot")
    print("9) Tallenna tuntikohtaiset säätilatiedot")
    print("0) Lopeta")
    try:
        valinta = int(input("Valintasi: "))
    except ValueError:
        print("Anna valinta kokonaislukuna.")
        return None
    if valinta < 0 or valinta > 9:
        print("Valintaa ei tunnistettu, yritä uudestaan.")
        return None
    return valinta

  
#Toinen aliohjelma pyytää käyttäjältä havaintoaseman ja analysoitavan vuoden.        

def Anna_havaintoasema_ja_vuosi():
    tiedot = TIEDOT()
    tiedot.nimi = input("Anna havaintoaseman nimi: ")
    try:
        tiedot.vuosiluku = int(input("Anna analysoitava vuosi: "))
    except ValueError:
        print("Anna vuosiluku kokonaislukuna.")
        return None
    return tiedot

#Kolmas aliohjelma lukee käyttäjän antamien tietojen perusteella tiedoston, sekä lisää tarpeellisia tietoja listaan analysointia varten.

def Lue_saatilatiedosto(tiedot):
    lista = []
    if tiedot == (None):
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        return lista
    rivienmaara = 0
    tiedostonimi = (str(tiedot.nimi) + str(tiedot.vuosiluku)+'.txt')
    try:
        tiedosto = open(tiedostonimi, "r")
    except OSError:
        print("Tiedoston '"+str(tiedostonimi)+"' avaaminen epäonnistui.")
        sys.exit(0)
    rivienmaara += 1
    try:
        poistettu_rivi = tiedosto.readline()
        while (True):
            tiedot = TIEDOT()
            rivienmaara += 1
            rivi = tiedosto.readline()
            if len(rivi) == 0:
                break
            jaettu_rivi = rivi[:-1].split(";")
            tiedot.paivamaara = datetime.datetime.strptime(jaettu_rivi[0],"%Y-%m-%d")
            tiedot.tunnit = (jaettu_rivi[1])
            tiedot.paisteaika = int(jaettu_rivi[2])
            lista.append(tiedot)
    except OSError:
        print("Tiedoston '"+str(tiedostonimi)+"' lukeminen epäonnistui.")
        sys.exit(0)
    tiedosto.close()
    print("Tiedosto '"+str(tiedostonimi)+"' luettu. Tiedostossa oli",rivienmaara,"riviä.")
    return lista

#Neljäs aliohjelma analysoi luetun tiedoston ja erottelee sekä laskee siitä tarpeelliset tiedot kirjoittamista varten.

def Analysoi_paivittaiset_saatilatiedot(lista):
    try:
        lista[0]
    except IndexError:
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return lista
    alkiolista = []
    paiva = lista[0].paivamaara
    kumulatiivinensumma = 0
    for alkio in lista:
        if (alkio.paivamaara == paiva):
            kumulatiivinensumma += int(alkio.paisteaika)
        else:
            tiedot = TIEDOT()
            tiedot.paivamaara = paiva
            tiedot.paisteaika = kumulatiivinensumma
            alkiolista.append(tiedot)
            paiva = alkio.paivamaara
            kumulatiivinensumma += int(alkio.paisteaika)
    tiedot = TIEDOT()
    tiedot.paivamaara = paiva
    tiedot.paisteaika = kumulatiivinensumma
    alkiolista.append(tiedot)
    print("Data analysoitu ajalta",alkiolista[0].paivamaara.strftime("%d.%m.%Y"),"-",str(alkiolista[-1].paivamaara.strftime("%d.%m.%Y"))+".")
    return alkiolista

#Viides aliohjelma kirjoittaa analysoidut tiedot käyttäjän syöttämään tiedostoon.

def Tallenna_paivittaiset_saatilatiedot(alkiolista,tiedot):
    try:
        alkiolista[0]
    except IndexError:
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        return alkiolista
    tulostiedoston_nimi = input("Anna tulostiedoston nimi: ")
    try:
        tiedosto = open(tulostiedoston_nimi, "w")
    except OSError:
        print("Tiedoston '"+str(tulostiedoston_nimi)+"' avaaminen epäonnistui.")
        sys.exit(0)
    try:
        tiedosto.write("Pvm")
        for indeksi in range(len(alkiolista)):
            tiedosto.write(str(alkiolista[indeksi].paivamaara.strftime(";%d.%m.%Y")))
        tiedosto.write('\n'+str(tiedot.nimi))
        for indeksi in range(len(alkiolista)):
            tiedosto.write(";"+str(int(alkiolista[indeksi].paisteaika/60)))
        tiedosto.write('\n')
    except OSError:
        print("Tiedoston '"+str(tulostiedoston_nimi)+"' kirjoitus epäonnistui.")
        sys.exit(0)
    tiedosto.close()
    print("Paisteaika tallennettu tiedostoon '"+str(tulostiedoston_nimi)+"'.")
    return None

#Kuudes aliohjelma lukee Ilmatieteen laitoksen dataa ja erottelee siitä tarpeelliset tiedot jatkokäsittelyä varten.
        
def Lue_Ilmatieteen_laitoksen_tiedosto(tiedot,lista):
    if tiedot == (None):
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        return tiedot
    lista.clear()
    rivienmaara = 0
    tiedostonimi = (str(tiedot.nimi) + str(tiedot.vuosiluku)+'_fmi.txt')
    try:
        tiedosto = open(tiedostonimi, "r", encoding="utf-8")
    except OSError:
        print("Tiedoston '"+str(tiedostonimi)+"' avaaminen epäonnistui.")
        sys.exit(0)
    rivienmaara += 1
    try:
        poistettu_rivi = tiedosto.readline()
        while (True):
            rivienmaara += 1
            rivi = tiedosto.readline()
            jaettu_rivi = rivi[:-1].split(",")
            if len(rivi) == 0:
                break
            tiedot = TIEDOT()
            tiedot.vuosi = datetime.datetime.strptime(jaettu_rivi[0],"%Y")
            tiedot.kuukausi = datetime.datetime.strptime(jaettu_rivi[1],"%m")
            tiedot.paiva = datetime.datetime.strptime(jaettu_rivi[2],"%d")
            tiedot.tunnit = (jaettu_rivi[3])
            try:
                tiedot.paisteaika = int(jaettu_rivi[5])
            except ValueError:
                tiedot.paisteaika = 0
            lista.append(tiedot)
    except OSError:
        print("Tiedoston '"+str(tiedostonimi)+"' lukeminen epäonnistui.")
        sys.exit(0)
    tiedosto.close()
    if lista[-1].vuosi.strftime("%Y") > lista[-2].vuosi.strftime("%Y"):
        del lista[-1]
    print("Tiedosto '"+str(tiedostonimi)+"' luettu. Tiedostossa oli",rivienmaara,"riviä.")
    return lista

#Seitsemäs aliohjelma analysoi säätilatiedot ja laskee kuukausittaiset paisteajat sekä listaa ne kirjoittamista varten.
    
def Analysoi_kuukausittaiset_saatilatiedot(lista):
    try:
        lista[0]
    except IndexError:
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return lista
    alkiolista = []
    alkiolista.clear()
    kuukausi = lista[0].kuukausi
    paiste_kuukaudessa = 0
    for alkio in lista:
        if (alkio.kuukausi == kuukausi):
            paiste_kuukaudessa += int(alkio.paisteaika)
        else:
            tiedot = TIEDOT()
            tiedot.kuukausi = kuukausi
            tiedot.paisteaika = paiste_kuukaudessa
            alkiolista.append(tiedot)
            kuukausi = alkio.kuukausi
            paiste_kuukaudessa = int(alkio.paisteaika)
    tiedot = TIEDOT()
    tiedot.kuukausi = kuukausi
    tiedot.paisteaika = paiste_kuukaudessa
    alkiolista.append(tiedot)
    paivamaara = str(lista[0].paiva.strftime("%d"))+"."+str(lista[0].kuukausi.strftime("%m"))+"."+str(lista[0].vuosi.strftime("%Y"))
    paivamaara2 = str(lista[-1].paiva.strftime("%d"))+"."+str(lista[-1].kuukausi.strftime("%m"))+"."+str(lista[-1].vuosi.strftime("%Y"))
    print("Data analysoitu ajalta",paivamaara,"-",paivamaara2+".")
    return alkiolista

#Kahdeksas aliohjelma kirjoittaa käyttäjän antamaan tulostiedostoon kuukausittaisen paisteajan.

def Tallenna_kuukausittaiset_saatilatiedot(alkiolista, Lippu, tiedot):
    try:
        alkiolista[0]
    except IndexError:
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        return alkiolista
    kirjoitettava_tiedosto = input("Anna kuukausitiedoston nimi: ")
    try:
        if Lippu == (True):
            tiedosto = open(kirjoitettava_tiedosto, "w")
        else:
            tiedosto = open(kirjoitettava_tiedosto, "a")
    except OSError:
        print("Tiedoston '"+str(kirjoitettava_tiedosto)+"' avaaminen epäonnistui.")
        sys.exit(0)
    nimi_ja_vuosi = str(tiedot.nimi)+" "+str(tiedot.vuosiluku)
    try:
        if Lippu == (True):
            tiedosto.write("Kk")
            for indeksi in range(len(alkiolista)):
                tiedosto.write(";"+str(alkiolista[indeksi].kuukausi.strftime("%m")))
            tiedosto.write("\n"+str(nimi_ja_vuosi))
            for indeksi in range(len(alkiolista)):
                tiedosto.write(";"+str(int(alkiolista[indeksi].paisteaika / 60)))
            tiedosto.write("\n")
            Lippu = False
        else:
            tiedosto.write(str(nimi_ja_vuosi))
            for indeksi in range(len(alkiolista)):
                tiedosto.write(";"+str(int(alkiolista[indeksi].paisteaika / 60)))
            tiedosto.write("\n")
    except OSError:
        print("Tiedoston '"+str(kirjoitettava_tiedosto)+"' kirjoitus epäonnistui.")
        sys.exit(0)
    print("Paisteaika tallennettu tiedostoon '"+str(kirjoitettava_tiedosto)+"'.")
    tiedosto.close()
    return Lippu

#Yhdeksäs aliohjelma analysoi tuntikohtaiset säätilatiedot ja laskee sekä listaa ne kirjoittamista varten.

def Analysoi_tuntikohtaiset_saatilatiedot(lista):
    try:
        lista[0]
    except IndexError:
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return lista
    tiedot = TIEDOT()
    matriisi = numpy.zeros((24, 12), int)
    for alkio in lista:
        jako = alkio.tunnit.split(":")
        tunti = int(jako[0])
        kuukausi = int(alkio.kuukausi.strftime("%m")) - 1
        matriisi[tunti][kuukausi] += alkio.paisteaika
    paivamaara = str(lista[0].paiva.strftime("%d"))+"."+str(lista[0].kuukausi.strftime("%m"))+"."+str(lista[0].vuosi.strftime("%Y"))
    paivamaara2 = str(lista[-1].paiva.strftime("%d"))+"."+str(lista[-1].kuukausi.strftime("%m"))+"."+str(lista[-1].vuosi.strftime("%Y"))
    print("Data analysoitu ajalta",paivamaara,"-",paivamaara2+".")
    return matriisi

#Kymmenes aliohjelma kirjoittaa tuntikohtaisen paisteajan kuukaudessa aliohjelman määrittelemään tulostiedostoon.

def Tallenna_tuntikohtaiset_saatilatiedot(matriisi,lista,tiedot):
    try:
        matriisi[0][0]
    except IndexError:
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        return matriisi
    tiedosto_nimi = (str(tiedot.nimi) + str(tiedot.vuosiluku)+'tunnit.txt')
    try:
        tiedosto =  open(tiedosto_nimi, "w")
    except OSError:
        print("Tiedoston '"+str(tiedosto_nimi)+"' avaaminen epäonnistui.")
        sys.exit(0)
    try:
        tiedosto.write(str(tiedot.nimi) +" "+ str(tiedot.vuosiluku)+" tuntipohjainen paisteaika:\n")
        for tunti in range(24):
            tiedosto.write(";"+str(tunti))
        tiedosto.write("\n")
        for tunti in range(12):
            tiedosto.write(str(tunti+1))
            for kuukausi in range(24):
                tiedosto.write(";"+str(int(matriisi[kuukausi][tunti]/60)))
            tiedosto.write("\n")
        tiedosto.write("Yht.")
        for kuukausi in range(24):
            tiedosto.write(";"+str(int(sum(matriisi[kuukausi]/60))))
        tiedosto.write("\n")
    except OSError:
        print("Tiedoston '"+str(tiedosto_nimi)+"' kirjoitus epäonnistui.")
        sys.exit(0)
    print("Paisteaika tallennettu tiedostoon '"+str(tiedosto_nimi)+"'.")
    tiedosto.close()
    return None


    
        
            
#############################################################################################################################
######eof        
    

        
    

