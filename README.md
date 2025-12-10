# Pin_pong 🏓

## Rövid leírás  
Pin_pong egy egyszerű játék — vagy program (attól függ, mit valósít meg a kód) — amit én készítettem. A célja, hogy … *(ide jöhet röviden: pl. egy Pong-szerű játék, ping-pong mechanikával / fájlrendezés / bármi, amit a projekt valójában csinál — módosítsd tetszés szerint)*.

## ⚙️ Mire jó / Mi a célja  
- Saját szórakoztatásra / tanulásra készült projekt.  
- Bemutatja, hogy hogyan tudok … *(pl. grafikus játék, logika, GUI, stb — attól függően, mit valósít Pin_pong)*.  
- Jó kiindulási alap későbbi fejlesztésekhez, bővítésekhez.  

## 🚀 Indítás / használat  

1. Klónozd a repót:  
   ```bash
   git clone https://github.com/mekercs/Pin_pong.git
Lépj be a projekt könyvtárába:

bash
Kód másolása
cd Pin_pong
Indítsd el a programot (ha Python — vagy: a megfelelő fájlt futtathatod):

bash
Kód másolása
python main.py      # vagy: python3 main.py
(Ha más nyelv / fájlnév — módosítsd a parancsot a projektnek megfelelően.)

🛠️ Hogyan működik / Mi van benne
A projekt fő logikája egy egyszerű Pong / Ping-Pong játék megvalósítása a Pygame könyvtár segítségével. A kód létrehozza a játék pályáját, a két játékos ütőit és a labdát, majd a fő ciklusban folyamatosan frissíti és kirajzolja ezeket. A játékosok billentyűzettel irányíthatják az ütőiket (W–S illetve fel–le nyilak).
A labda folyamatosan mozog, visszapattan az ütőkről és a falakról, és pontgyűjtés helyett újra középre kerül, ha valamelyik oldalon túljut. A program ezen kívül ütközésvizsgálatot, egyszerű fizikai visszapattanást, valamint képernyő-frissítést és FPS-szabályozást is tartalmaz.

A projekt struktúrája egyszerű — minden a fő mappában található.

Nincsenek extra függőségek (vagy ha vannak: sorold fel őket).

👤 Készítette
mekercs
