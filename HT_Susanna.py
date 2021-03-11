# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Susanna Lähde
# Opiskelijanumero: 0570397
# Päivämäärä: 18.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: 

#Tuodaan kirjasto ja moduuli

import HT_kirjasto as kirjasto
import sys

#Määritellään paaohjelma()

def paaohjelma():
    tiedot = None
    lista = []
    alkiolista = []
    matriisi = []
    Lippu = True
    while (True): 
        valinta = kirjasto.Valikko()
        if valinta == 1:
            tiedot = kirjasto.Anna_havaintoasema_ja_vuosi()
        elif valinta == 2:
            lista = kirjasto.Lue_saatilatiedosto(tiedot)
        elif valinta == 3:
            alkiolista = kirjasto.Analysoi_paivittaiset_saatilatiedot(lista)
        elif valinta == 4:
             kirjasto.Tallenna_paivittaiset_saatilatiedot(alkiolista,tiedot)
        elif valinta == 5:
            lista = kirjasto.Lue_Ilmatieteen_laitoksen_tiedosto(tiedot,lista)
        elif valinta == 6:
            alkiolista = kirjasto.Analysoi_kuukausittaiset_saatilatiedot(lista)
        elif valinta == 7:
            Lippu = kirjasto.Tallenna_kuukausittaiset_saatilatiedot(alkiolista, Lippu, tiedot)
        elif valinta == 8:
            matriisi = kirjasto.Analysoi_tuntikohtaiset_saatilatiedot(lista)
        elif valinta == 9:
            kirjasto.Tallenna_tuntikohtaiset_saatilatiedot(matriisi,lista,tiedot)
        elif valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            sys.exit(0)
        print("")
    return None
                    
paaohjelma()
  
       
#############################################################################################################################
######eof
