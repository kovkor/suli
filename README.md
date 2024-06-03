
# Általános Iskolai Feladatlapokat Generáló Scriptek

## Áttekintés

Ez a repository Python scripteket tartalmaz, amelyek feladatokat generálnak általános iskolás tanulók számára.

## Elérhető scriptek

## Matek

### alapmuveletek_egyenlet.py
Hiányzó számok beírása, hogy igaz legyen az egyenlet.

### muveleti-jelek.py
Hiányzó műveleti jelek pótlása

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
python muveleti-jelek.py --max_result 20 --num_problems 50 --operations +,-,*,/
```

### Paraméterek

- `--max_result`: A műveletek maximális eredménye (alapértelmezett: 20).
- `--num_problems`: A generálandó feladatok száma (alapértelmezett: 50).
- `--operations`: A megengedett műveletek, vesszővel elválasztva (alapértelmezett: +,-,*,/).

### Példa

```sh
python muveleti-jelek.py --max_result 20 --num_problems 50 --operations +,-
```

Ez a parancs 50 feladatot generál, ahol az eredmény maximum 20 lehet, és csak összeadás és kivonás műveletek szerepelnek.

## alapmuveletek-egyenlet.py

Ez a script olyan egyenleteket generál, ahol az egyik szám helyét kell kitalálni az alapműveletek segítségével.

### Használat

```sh
python alapmuveletek-egyenlet.py --max_result 20 --num_problems 50 --operations +,-,*,/
```

### Paraméterek

- `--max_result`: Az egyenletek maximális eredménye (alapértelmezett: 20).
- `--num_problems`: A generálandó feladatok száma (alapértelmezett: 50).
- `--operations`: A megengedett műveletek, vesszővel elválasztva (alapértelmezett: +,-,*,/).

### Példa

```sh
python alapmuveletek-egyenlet.py --max_result 20 --num_problems 50 --operations +,-,*,/
```

Ez a parancs 50 egyenletet generál, ahol az eredmények maximum 20 lehetnek, és az összes alapművelet megengedett.

## Kimenet

Mindkét script egy PDF fájlt generál a generatedPdfs mappába, amely a megadott matematikai feladatokat tartalmazza.

## Megjegyzések

- Győződj meg arról, hogy a `FreeSans.ttf` fájl elérhető a script könyvtárában.
- A parancssori argumentumokat az igényeid szerint módosíthatod, hogy testreszabott feladatokat generálj.

## Licenc

Ez a projekt nyílt forráskódú és a MIT licenc alatt érhető el.

## Kapcsolat
https://codeone.hu


