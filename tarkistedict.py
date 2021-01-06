ekaLista = []
tokaLista = []
with open("tarkiste_eka.txt", "r") as eka:
    for line in eka:
        ekaLista.append(line)

with open("tarkiste_toka.txt", "r") as toka:
    for line in toka:
        tokaLista.append(line)

muokattuLista = []
for i in range(0,len(ekaLista)):
    muokattuRivi = f'"{ekaLista[i]}": "{tokaLista[i]}"'.replace("\n","")
    muokattuLista.append(muokattuRivi)

for i in muokattuLista:
    print(i)

with open("tarkistedict.txt", "w") as tar:
    for i in muokattuLista:
        tar.write(f'{i},\n')
    tar.close()