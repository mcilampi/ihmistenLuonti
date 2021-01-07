import secrets
import codecs

# luetaan miesten ja naisten nimet listoista ja palautetaan yksi
# kaksi eri listaa, jotta säilyy mahdollisuus muuttaa ohjelmaa
# arpomaan vain toista

# arvotaan etunimilistasta etunimen index-numero
def arvoEtuNimi(etuNimiLista):
    etuNimenNumero = secrets.choice(range(0, len(etuNimiLista)))
    return etuNimenNumero

# valitaan etunimilistasta arvoEtuNimi-function palauttaman indexin nimi
def maaritaArvottuEtunimi(etuNimiLista,etuNimenNumero):
    etuNimi = etuNimiLista[etuNimenNumero]
    return etuNimi

def arvoSukuNimi(sukuNimet):
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
def syntymaAika(paiva,kuukausi,vuosi):
    syntymaAika = f'{paiva:02d}-{kuukausi:02d}-{vuosi}'
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

# arvotaan postinumerolistasta numero ja toimipaikka, palautetaan 
def arvoPostiNro(postiNroLista):
    henkilonPostiNro = postiNroLista[secrets.randbelow(len(postiNroLista))]
    return henkilonPostiNro

#arvotaan tielistasta tie, kadunnumero ja tietyllä todennäköisyydellä rappu ja asunnonnumero
def arvoOsoite(tieLista):
    rappuKirjaimet = ["A", "B", "C", "D", "E", "F", "G", "H"]
    tie = tieLista[secrets.randbelow(len(tieLista))]
    rappu =""
    asunnonNro = ""
    katuNumero = f'{secrets.randbelow(30) + 1} '
    rappuKo = secrets.randbelow(3)
    if rappuKo > 0:
        rappu = f'{rappuKirjaimet[secrets.randbelow(len(rappuKirjaimet))]} '
        asunnonNumeroKo = secrets.randbelow(2)
        if asunnonNumeroKo > 0:
            asunnonNro = f'{secrets.randbelow(20) + 1} '
    katuOsoite = f'{tie} {katuNumero}{rappu}{asunnonNro}'
    return katuOsoite

# arvotaan listasta suuntanumero ja loppuosa tietyltä väliltä
def puhelinNumero():
    suuntaNroLista = ["040", "050", "045", "041", "044"]
    suuntaNro = suuntaNroLista[secrets.randbelow(len(suuntaNroLista))]
    loppuOsa = secrets.choice(range(1100000,9500000))
    puhelinNumero = f'{suuntaNro}{loppuOsa}'
    return puhelinNumero

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
# luetaan miesten ja naisten etunimet tiedostoista ja tehdään yksi lista
etuNimet = []
with open("etunimilista_miehet.txt", "r", encoding="utf-8") as etu:
    for line in etu:
        etuNimet.append(line)
with open ("etunimilista_naiset.txt", "r", encoding="utf-8") as etu:
    for line in etu:
        etuNimet.append(line)

# luetaan sukunimet tiedostosta listaan
sukuNimet = []
with open ("sukunimilista.txt", "r", encoding="utf-8") as suku:
    for line in suku:
        sukuNimet.append(line)

postiNroLista = []
with open("postinrotsuodatettu.csv", "r") as pn:
    for line in pn:
        postiNroLista.append(line.replace(","," ").replace("\n",""))
    pn.close()

tieLista = []
with open("tiet.txt", "r") as tiet:
    for line in tiet:
        tieLista.append(line.replace("\n", ""))
    tiet.close()

kaynnissa = True

while kaynnissa:
    while True:
        try: 
            montako = int(input("Montako nimeä haluat tehdä? "))
            break
        except:
            print("Anna numero!")
    x = 0
    ihmisLista = []
    ihmisListaCSV = []
    while x < montako:
        sVuosi = syntymaVuosi()
        sKuukausi = syntymaKuukausi()
        sPaiva = syntymaPaiva()
        alkuOsa = hetuAlku(sPaiva,sKuukausi,sVuosi)
        sAika = syntymaAika(sPaiva,sKuukausi,sVuosi)
        arvottuEtuNimi = arvoEtuNimi(etuNimet)
        etuNimi = maaritaArvottuEtunimi(etuNimet,arvottuEtuNimi).replace("\n", "")
        lopunKolmeEkaa = loppuOsanAlku(arvottuEtuNimi)
        tarkiste = str(laskeTarkiste(alkuOsa,lopunKolmeEkaa))
        katuOsoite = arvoOsoite(tieLista)
        postiNroToimipaikka = arvoPostiNro(postiNroLista)
        ihmisenTiedot = f'{etuNimi} {arvoSukuNimi(sukuNimet)} {sAika} {alkuOsa}{valiMerkki(alkuOsa)}{lopunKolmeEkaa}{tarkisteDictionary.get(tarkiste)} {katuOsoite}{postiNroToimipaikka} {puhelinNumero()}'
        ihmisenTiedotCSV = f'{etuNimi},{arvoSukuNimi(sukuNimet)},{sAika},{alkuOsa}{valiMerkki(alkuOsa)}{lopunKolmeEkaa}{tarkisteDictionary.get(tarkiste)},{katuOsoite},{postiNroToimipaikka},{puhelinNumero()}'
        print(f'{x + 1:07d}. {ihmisenTiedot}')
        ihmisLista.append(ihmisenTiedot)
        ihmisListaCSV.append(ihmisenTiedotCSV)
        x += 1
    while True:
        try:
            tiedostoonko = input("Haluatko tallentaa nimet tiedostoon? k/e ")
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
                for i in ihmisListaCSV:
                    csv.write(f'{i}\n')
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
        kaynnissa = False
