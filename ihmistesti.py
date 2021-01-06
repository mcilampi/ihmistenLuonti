from os import close, replace, write
import secrets
import codecs
import sys
# luetaan miesten ja naisten nimet listoista ja palautetaan yksi
# kaksi eri listaa, jotta säilyy mahdollisuus muuttaa ohjelmaa
# arpomaan vain toista



def lueEtuNimet():
    etuNimet = []
    with open("etunimilista_miehet.txt", "r", encoding="utf-8") as etu:
        for line in etu:
            etuNimet.append(line)
    with open ("etunimilista_naiset.txt", "r", encoding="utf-8") as etu:
        for line in etu:
            etuNimet.append(line)
    return etuNimet

# arvotaan etunimilistasta etunimen index-numero
def arvoEtuNimi(etuNimiLista):
    etuNimenNumero = secrets.choice(range(0, len(etuNimiLista)))
    #etuNimi = etuNimiLista[secrets.choice(range(0, len(etuNimiLista)))].replace("\n", "")
    return etuNimenNumero

# valitaan etunimilistasta arvoEtuNimi-function palauttaman indexin nimi
def maaritaArvottuEtunimi(etuNimiLista,etuNimenNumero):
    etuNimi = etuNimiLista[etuNimenNumero]
    return etuNimi

# lueataan listasta sukunimiä, arvotaan yksi ja palautetaan
def arvoSukuNimi():
    sukuNimet = []
    with open ("sukunimilista.txt", "r", encoding="utf-8") as suku:
        for line in suku:
            sukuNimet.append(line)
    sukuNimi = sukuNimet[secrets.choice(range(0, len(sukuNimet)))].replace("\n", "")
    return sukuNimi

#arvotaan syntymävuosi, -kuukausi ja -päivä
def syntymaVuosi():
    vuosi = secrets.choice(range(1940,2015))
    return vuosi

def syntymaKuukausi():
    kuukausi = secrets.choice(range(1,12))
    return kuukausi

def syntymaPaiva():
    paiva = secrets.choice(range(1,29))
    return paiva

# yhdistetään syntymävuosi, -kuukausi ja -päivä ja palautetaan stringinä
def syntymaAika():
    syntymaAika = f'{syntymaPaiva():02d}-{syntymaKuukausi():02d}-{syntymaVuosi()}'
    return syntymaAika

# yhtdistetään hetun alkuosaksi päivä, kuukausi ja vuosi, palautetaan stringinä
def hetuAlku(paiva,kuukausi,vuosi):
    uusiVuosi = 0
    if vuosi >= 2000:
        uusiVuosi = vuosi-2000
    elif vuosi < 2000: 
        uusiVuosi = vuosi-1900
    hetuAlku = f'{paiva:02d}{kuukausi:02d}{uusiVuosi:02d}'
    return hetuAlku

# määritetään välimerkki hetun alkuosan kahden viimeisen luvun perusteella
def valiMerkki(hetuAlku):
    valiMerkki = ""
    if int(hetuAlku[4:6]) < 40:
        valiMerkki = "A"
    elif int(hetuAlku[4:6]) >= 40:
        valiMerkki = "-"
    return valiMerkki

# arvotaan loppuosan kolme ensimmäistä numeroa, miehille pariton ja naisille parillinen
def loppuOsanAlku(etuNimenIndex):
    loppuOsanAlkuNumero = 0
    miestenNimet = []
    with open("etunimilista_miehet.txt", "r") as m:
        for line in m:
            miestenNimet.append(line)
    if etuNimenIndex < len(miestenNimet):
        loppuOsanAlkuNumero = secrets.choice(range(2,449)) * 2 + 1
    elif etuNimenIndex >= len(miestenNimet):
        loppuOsanAlkuNumero = secrets.choice(range(2,449)) * 2
    return f'{loppuOsanAlkuNumero:03d}'

# muodostetaan yksi luku alkuosasta ja loppuosan alusta, lasketaan tarkiste ja
# haetaan dictionarysta, palautetaan
def laskeTarkiste(alkuOsa,loppuOsa):
    yhteisLuku = str(alkuOsa)+str(loppuOsa)
    tarkisteenAvain = int(yhteisLuku) % 31
    return tarkisteenAvain

def kirjoitaTxt():
    pass

def kirjoitaCSV():
    pass


###################
## ohjelma alkaa ##
###################
tarkisteDictionary = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
    "16": "H",
    "17": "J",
    "18": "K",
    "19": "L",
    "20": "M",
    "21": "N",
    "22": "P",
    "23": "R",
    "24": "S",
    "25": "T",
    "26": "U",
    "27": "V",
    "28": "W",
    "29": "X",
    "30": "Y"
}

while True:
    while True:
        try: 
            montako = int(input("Montako nimeä haluat tehdä? "))
            break
        except:
            print("Anna numero!")
    x = 0
    ihmisLista = []
    while x < montako:
        alkuOsa = hetuAlku(syntymaPaiva(),syntymaKuukausi(),syntymaVuosi())
        arvottuEtuNimi = arvoEtuNimi(lueEtuNimet())
        etuNimi = maaritaArvottuEtunimi(lueEtuNimet(),arvottuEtuNimi).replace("\n", "")
        lopunKolmeEkaa = loppuOsanAlku(arvottuEtuNimi)
        tarkiste = str(laskeTarkiste(alkuOsa,lopunKolmeEkaa))
        ihmisenTiedot = f'{etuNimi} {arvoSukuNimi()} {syntymaAika()} {alkuOsa}{valiMerkki(alkuOsa)}{lopunKolmeEkaa}{tarkisteDictionary.get(tarkiste)}'
        print(f'{x + 1}. {ihmisenTiedot}')
        ihmisLista.append(ihmisenTiedot)
        x += 1
    while True:
        try:
            tiedostoonko = input("Haluatko tallentaa nimet tiedostoon? k/e")
            if tiedostoonko != "k" and tiedostoonko != "e":
                raise Exception()
            break
        except:
            print("Valitse k tai e!")
    if tiedostoonko == "k":
        tiedostoNimi = input("Anna tiedostonimi: ")
        while True:
            try:
                print("Haluatko tallentaa tiedoston")
                print("1. Tekstitiedostona (.txt)")
                print("2. CSV-tiedostona (.csv)")
                tiedostoMuoto = int(input("Valintasi: "))
                break
            except:
                print("Valitse 1 tai 2!")

        if tiedostoMuoto == 1:
            with codecs.open(f'{tiedostoNimi}.txt', "w", "utf-8") as txt:
                for i in ihmisLista:
                    txt.write(f'{i}\n')
                txt.close()
        elif tiedostoMuoto == 2:
            with codecs.open(f'{tiedostoNimi}.csv', "w", "utf-8") as csv:
                for i in ihmisLista:
                    csv.write(f'{i.replace(" ", ",")}\n')
                csv.close()
    while True:
        try:
            vielako = input("Haluatko tehdä lisää nimiä? k/e ")
            if vielako != "k" and vielako != "e":
                raise Exception()
            break
        except:
            print("Valitse kyllä tai ei!")
        if vielako == "e":
            print("Heippa!")
            sys.exit(0)
        elif vielako == "k":
            pass
