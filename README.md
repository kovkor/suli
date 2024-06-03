
# Általános Iskolai Feladatlapokat Generáló Scriptek

## Áttekintés

Ez a repository Python scripteket tartalmaz, amelyek feladatokat generálnak általános iskolás tanulók számára.

## Elérhető scriptek

## Matek

- **matek/alapmuveletek_egyenlet.py**
  - Hiányzó számok beírása, hogy igaz legyen az egyenlet.

- **matek/muveleti-jelek.py**
  - Hiányzó műveleti jelek pótlása

- **matek/nyitott-mondat.py**
  - Nyitott mondatok gyakorlása relációkkal

## Követelmények

- Python 3
- fpdf könyvtár
- FreeSans betűtípus (letölthető innen: [FreeSans](https://www.fontsquirrel.com/fonts/free-sans))

## Telepítés

1. Klónozd a repository-t:
    ```sh
    git clone https://github.com/kovkor/suli.git
    cd suli
    ```

2. Telepítsd a szükséges Python csomagokat:
    ```sh
    pip install fpdf
    ```

3. Helyezd a `FreeSans.ttf` betűtípust a script könyvtárába.

## muveleti-jelek.py

Ez a script olyan feladatokat generál, ahol a műveleti jeleket (összeadás, kivonás, szorzás, osztás) kell beilleszteni a megadott helyre.

### Használat

```sh
python matek/muveleti-jelek.py --max_result 20 --num_problems 50 --operations +,-,*,/
```

### Paraméterek

- `--max_result`: A műveletek maximális eredménye (alapértelmezett: 20).
- `--num_problems`: A generálandó feladatok száma (alapértelmezett: 50).
- `--operations`: A megengedett műveletek, vesszővel elválasztva (alapértelmezett: +,-,*,/).

### Példa

```sh
python matek/muveleti-jelek.py --max_result 20 --num_problems 50 --operations +,-
```

Ez a parancs 50 feladatot generál, ahol az eredmény maximum 20 lehet, és csak összeadás és kivonás műveletek szerepelnek.

## alapmuveletek-egyenlet.py

Ez a script olyan egyenleteket generál, ahol az egyik szám helyét kell kitalálni az alapműveletek segítségével.

### Használat

```sh
python matek/alapmuveletek-egyenlet.py --max_result 20 --num_problems 50 --operations +,-,*,/
```

### Paraméterek

- `--max_result`: Az egyenletek maximális eredménye (alapértelmezett: 20).
- `--num_problems`: A generálandó feladatok száma (alapértelmezett: 50).
- `--operations`: A megengedett műveletek, vesszővel elválasztva (alapértelmezett: +,-,*,/).

### Példa

```sh
python matek/alapmuveletek-egyenlet.py --max_result 20 --num_problems 50 --operations +,-,*,/
```

Ez a parancs 50 egyenletet generál, ahol az eredmények maximum 20 lehetnek, és az összes alapművelet megengedett.


## nyitott-mondat.py
Ez a script olyan nyitott mondat típusú feladatokat generál, ahol a keresett számok helyére különböző szimbólumok kerülnek, és az egyenlőtlenségek igazak maradnak. A feladatok generálása során a script figyel arra, hogy a megadott paraméterek szerint és a meghatározott maximális darabszámú érvényes eredménye legyen a feladatoknak.

### Használat

```sh
python matek/nyitott-mondat.py --max_result 20 --num_problems 50 --max_valid_numbers 4
```

### Paraméterek

- `--max_result`: Az egyenletek maximális eredménye (alapértelmezett: 20).
- `--num_problems`: A generálandó feladatok száma (alapértelmezett: 50).
- `--max_valid_numbers`: Az érvényes számok maximális száma (alapértelmezett: 4).

### Példa

```sh
python matek/nyitott-mondat.py --max_result 20 --num_problems 50 --max_valid_numbers 4
```

Ez a parancs 50 nyitott mondat típusú feladatot generál, ahol az eredmények összege maximum 20 lehet, és legfeljebb 4 érvényes szám lesz a keresett számok helyén.


## Kimenet

Minden script PDF fájloket generál a generatedPdfs mappába, amely a megadott feladatokat tartalmazza.

## Megjegyzések

- Győződj meg arról, hogy a `FreeSans.ttf` fájl elérhető a script könyvtárában.
- A parancssori argumentumokat az igényeid szerint módosíthatod, hogy testreszabott feladatokat generálj.

## Licenc

Ez a projekt nyílt forráskódú és a MIT licenc alatt érhető el.

## Kapcsolat
https://codeone.hu


