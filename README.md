# Križić-kružić (Tic Tac Toe) igra s prilagođenim vizualnim postavkama

Ovo je jednostavna igra Križić-kružić napravljena u Pythonu koristeći Tkinter GUI biblioteku. Prije početka igre, korisnik unosi željene vizualne parametre za prilagodbu izgleda igre.

## Značajke

- Unos vizualnih postavki prije pokretanja igre (boje pozadine, gumba, križića, kružića, pobjedničkih gumbiju, fontova i stilova teksta).
- Jednostavno grafičko sučelje za igru s gumbima.
- Semafor rezultata koji pokazuje trenutni rezultat igrača X i O.
- Automatsko prepoznavanje pobjednika i označavanje pobjedničkih polja.
- Mogućnost ponovne igre ili zatvaranja aplikacije nakon završetka partije.

## Kako pokrenuti

1. Provjerite imate li instaliran Python (verzija 3.x).
2. Pokrenite skriptu u terminalu ili komandnoj liniji:

```bash
python naziv_datoteke.py
```

3. Slijedite upute za unos željenih postavki igre.
4. Igra će se otvoriti u prozoru s odabranim bojama i fontovima.

## Primjer unosa parametara

- Boja pozadine: `white`
- Boja gumba: `lightgrey`
- Font simbola: `Arial`
- Stil simbola: `bold`
- Boja križića (X): `red`
- Boja kružića (O): `blue`
- Boja pobjedničkih gumbiju: `yellow`
- Boja teksta semafora: `black`
- Font teksta semafora: `Arial`
- Veličina teksta semafora (u pikselima): `20`
- Stil teksta semafora: `normal`

## Struktura koda

- Funkcija `unesi_parametre()` dohvaća vizualne parametre od korisnika putem konzole.
- Klasa `KrizicKruzic` implementira samu igru, logiku i GUI elemente.
- `main()` funkcija inicijalizira Tkinter prozor i pokreće igru.

## Zahtjevi

- Python 3.x
- Tkinter (ugrađen u standardnu Python instalaciju)

## License

Ovaj projekt je otvorenog koda i slobodno ga možete koristiti i prilagođavati.

---

Ako imaš dodatnih pitanja ili želiš pomoći u razvoju igre, slobodno otvori issue ili PR.
