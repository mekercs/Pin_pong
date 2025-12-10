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
A projekt fő logikája egy Ping Pong játék megvalósítása Pygame segítségével. A program létrehozza a játékteret, két játékos ütőt (bal és jobb oldali) és a pattogó labdát. A játék működését az alábbi elemek adják:

Játék logika:
A fő ciklus folyamatosan frissíti a játék állapotát, kirajzolja az ütőket, a labdát és a középső választóvonalat.

Billentyűvezérlés:
Az 1. játékos a W és S billentyűkkel mozog fel és le.
A 2. játékos a fel/le nyíl gombokkal irányítja a saját ütőjét.

Labda mozgatása:
A labda minden képkockában elmozdul, a sebességet a Ping_x és ping_y változók határozzák meg.

Ütközés és visszapattanás:
A labda visszapattan:

ha eléri az egyik játékos ütőjét,

ha nekiütközik a képernyő tetejének vagy aljának.
Ha a labda kimegy bal vagy jobb oldalon, újra középre kerül, és véletlenszerű irányba indul.

Frissítés, FPS és renderelés:
A pygame.display.update() rajzolja újra a képernyőt,
a clock.tick(fps) szabályozza az FPS-t, ami itt nagyon magas (500).

A projekt struktúrája egyszerű — minden a fő mappában található.

Nincsenek extra függőségek (vagy ha vannak: sorold fel őket).

👤 Készítette
mekercs
