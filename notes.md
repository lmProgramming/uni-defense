# Obrona

## 1. Podstawowe układy cyfrowe: bramki logiczne, przełączniki, układy sekwencyjne

Układy cyfrowe to zbiór połączonych elementów elektronicznych, w którym informacje reprezentowane są w sposób binarny. Jeśli chodzi o binarność stanu, to ma on dwa stany: stan wysoki (1 lub H), oznaczający potencjał względem masy bliski napięciu zasilania, i stan niski (0 lub L), potencjał względem masy bliski 0V. W logice stan wysoki reprezentowałby prawdę, a niski fałsz.

Do obliczeń można wykorzystać algebrę boole'a, z oczywistymi przykładami, jak

1 ∧ 0 = 0
1 ∨ 0 = 0

Zasady:

A ∧ A = A
A ∨ A = A
A ∧ (A ∨ B) = A ∧ B

lub zapis
AB = A ∧ B
A + B = A ∨ B

Przykładowe bramki:

AND = A ∧ B
OR = A ∨ B
NOT = !A
XOR = (A ∨ B) ∧ !(A ∧ B)
NOR = !(A ∨ B) odwrotność OR
NAND = !(A ∧ B) odwrotność AND
XNOR = (A ∧ B) ∨ (!A ∧ !B)

Bramki Nxyz działają jak bramki xyz, ale z negacją wyjścia

Przełączniki to urządzenia wejścia - elementy mechaniczne lub elektromechaniczne.
Niektóre utrzymują swój stan (stabilne - np. przełącznik światła nie zmienia sam stanu), a inne, jak klawisze klawiatury (chwilowe), wracają do domyślnego stanu.

Ze względu na inercyjność, rozróżniamy układy na kombinacyjne i sekwencyjne.
W układach sekwencyjnych wyjścia w nich zależą nie tylko od wejść, ale też od wewnętrznego stanu.
A w kombinacyjnych, wyjścia zależą bezpośrednio od wejść (funkcja wejść na wyjścia).

Przerzutniki - układy sekwencyjne, które są w stanie zapamiętać stan i przekazać go dalej. Czyli nie są prostą funkcją wejść na wyjścia, bo do takiej funkcji jako argument trzeba dołączyć ich aktualny stan. Czyli posiadają wewnętrzny stan, który może zmieniać się w czasie i wpływa na działanie takiego układu (wyjście będzie rózne dla tych samych wejść przy różnych stanach)
kombinatoryjne

Przykłady:

Przerzutnik RS (flip flop) - wejścia SR, wyjścia Q i !Q
Bardzo prosty i asynchroniczny (czyli nie wymaga obecności zegara)  
S ustawia stan układu (Q) na wysoki dla S = 1  
R ustawia stan układu na niski dla R = 1  
Dla S i R = 0 stan pozostaje taki sam, czyli Q[n] = Q[n-1]  
Dla S i R = 1 stan nie jest zdefiniowany (może być losowy przez sprzeczność logiczną układu)
Przerzutnik JK flip flop to prawie przerzutnik SR, różni się tym, że dla J i K = 1 => Q = !Q

Przerzutniki D (Delay) flip flop i T (Toggle) flip flop - podstawowe przerzutniki synchroniczne. Wymagają sygnału zegara do ustawiania stanu. Dzięki temu ograniczone są zakłócenia ze strony danych wejściowych (debouncing)
Delay: ustawia Q=D, gdy CLK ma stan opadający lub narastający. Korzysta wewnętrznie z SR flip flop
Toggle: ustawia Q=!Q, gdy T=1 i CLK ma stan opadający lub narastający

Inne układy sekwencyjne to na przykład:
Licznik, który liczy liczbę zmian sygnału wejściowego
Rejestr, który przechowuje wartość bitu

Przykładami układów kombinacyjnych są:
Komparator, który zwraca, który z sygnałów jest większy, czy też są równe (taki if)
Multiplekser, który przekazuje jedno z wejść na wyjście w zależności od wejścia sterującego (taki switch)

Hazard to zjawisko, gdzie wynik układu może być chwilowo niepoprawny przez nienatychmiastową naturę prądu. Można walczyć z tym zjawiskiem wykorzystując zegar (układy synchroniczne) lub przez wprowadzenie redundancji elementów.

## 2. Arytmetyka dwójkowa, funkcje boolowskie, tablice Karnaugh

Arytmetyka dwójkowa dotyczy arytmetyki na liczbach o bazie 2, czyli cyfry to tylko 0 lub 1. Liczby konstruuje się analogicznie do bazy dziesiętnej, gdzie każda ważniejsza cyfra ma bazę razy większą wagę (czyli w przypadku dwójkowego 2 razy większą).

Dodawanie, odejmowanie, dzielenie i mnożenie można rozpisać przy dokładnie tym samym algorytmie jak dla operacji pisemnych w systemie dziesiętnym. Czyli

```txt
  1
  1 +
---
  2
---
1 0
```

itd.

Arytmetyka dwójkowa jest wykorzystywana w elektronice, i przez to w komputerach, z racji prostego wykrywania stanu 0 a 1 (reprezentowane przez potencjał względem masy zbliżonym do 0 dla 0 i potencjale względem masy zbliżonym do napięcia zasilania dla 1)

Naturalny kod binarny NKB - liczby są zapisywane w formie słów o konkretnej długości, np. 8, co oznacza, że liczbę np. 115 (1110011[2])zapisałoby się jako 01110011, dopełniając po lewej zera, aby słowo miało tą długość. Wtedy długość słowa określa przedział możliwych do reprezentacji liczb w zbiorze N + <1;2^N>

Kod dwójkowo-dziesiętny - reprezentacja osobno każdej cyfry w liczbie dziesiętnej słowami o długości 4 (bo 2^4>9). Niektóre wartości np. 1111 są niemożliwe, przez co występuje redundancja (nadmiarowość). Wg. mnie naturalnie przekłada się to w system 16stkowy, gdzie 10=A, 15=F.

Funkcje boolowskie: funkcje o n argumentach 0 lub 1 i o 1 wyjściu równym 0 lub 1. Układy elektroniczne realizujące funkcje boolowskie to układy kombinacyjne.

Funkcje boolowskie można przedstawić na 4. sposoby:

1. Przykładowa funkcja: F(a, b, c, d) = ab + (c + !d)
2. Iloczyn sum ```F(A,B,C,D) = (A+!C)(!A+B+!D)``` lub suma iloczynów ```F(A,B,C,D) = (AB!D)+(!A!C). No wiadomo, iloczyn sum jest prawdziwy tylko, jak spełnimy w każdym nawiasie choć jeden, a suma iloczynów jak w choć jednym nawiasie każdy warunek.
3. Tabele prawdy
![alt text](imgs/2/tabela_prawdy.png)
wartość dziesiętna to liczba jakby postawić a jako cyfrę najbardziej znaczącą i b jako najmniej.
4. Zbiory wartości dla F=1 albo dla F=0
Dodatkowo, jeśli jakieś wartości są niepewne, to funkcja jest niezupełna i też możne te wartości podać
![alt text](imgs/2/zbiory_wartosci.png)

Tablice Karnaugh można wykorzystać do uproszczenia, czyli minimalizacji funkcji boolowskich. Najlepiej działa, gdy liczba wejść jest niewielka, więc zacznę od przypadku cztero argumentowego. Gdy rozpiszemy tabelę prawdy dla cztero argumentowej funkcji z zachowaniem kodu grey'a (czyli kolumny i wiersze różnią się od sąsiadów wartością tylko 1 argumentu - bez tego te prostokąty byłyby bez sensu), to mamy te 0 i 1. Typowo kolumny to AB, a wiersze CD, bo można grupować w takiej tablicy argumenty w takie ciągi. Zaczynamy od narysowania największego prostokąta/ów, którego każdy bok jest potęgą 2 (1, 2, 4...), i wszystkie komórki wewnątrz są 1 (lub X dla niezdefiniowanych). Każdy krok algorytmu to wzięcie aktualnego N (pole tego kwadratu), znajdowanie kwadratów o takim polu które mają 1 lub X tylko w sobie. Potem dzielimy N przez 2 i ciągle robimy to samo, aż wszystkie 1 będą w prostokącie/prostokątach (mogą być naraz w dwóch, jeśli to optymalne). No i wynik to na logikę można zauważyć, że w takich prostokątach 1/2... argumenty się nie zmieniają i przedstawić funkcję np. jako ```Y = B*!C*D + A*B*!D```. Na logikę jak jest 1 w kwadracie gdzie A=0 i C=1 no to (!A*C). Prostokąty mogą przechodzić przez "ściany" tabeli na drugą stronę.
Alternatywnie mozna zrobić to samo, ale szukać 0 to ```Y = !(B*D) + !(!A*CD)```
Tablice Karnaugh do max 4-6 zmiennych. Dla więcej niż 4 zmiennych, trzeba brać pod uwagę osie symetrii.

## 3. Programowanie strukturalne - zasady. Przegląd instrukcji strukturalnych

Programowanie strukturalne to podstawa nowoczesnego programowania. Jej zasady pozwalają pisać kod, który ma jasny przepływ logiczny.
Liniowy przepływ najważniejszy, czyli ogólnie z góry do doły.

Warto wspomnieć, że programowanie strukturalne jest podparadygmatem programowania imperatywnego. Często przedstawia się je jako przekazanie instrukcji komputerowi, co ma zrobić, w kontrze do programowania deklaratywnego, gdzie instrukcja dotyczy tego, co chcemy osiągnąć. Czyli programowanie imperatywne to po prostu ciąg instrukcji, które ma wykonać komputer i zmienia jego stan.

W programowaniu strukturalnym program składa się z bloków, grupujące operacje, które będą wykonane od góry do dołu. Zwyczajowo zmienne definiowane w bloku nie są dostępne poza nim, są za to dostępne w zagnieżdżonych blokach, o ile nie wystąpi mechanizm maskowania (zmienna o tej samej nazwie przesłoni inną). Blok powinien mieć 1 punkt wejścia i 1 punkt wyjścia. Po wykonaniu wszystkich instrukcji wychodzimy z bloku. W większości języków blok oznaczony jest przez curly brackets {} (w Pythonie przez indentację). Bloki można zagnieżdżać w sobie, ale dla czytelności głęboko zagnieżdżone bloki warto wyciągać do funkcji, klas itd.

Główne elementy (są blokami, więc powinny mieć 1 punkt wejścia i wyjścia itd.):

- Instrukcje warunkowe: if; switch
- Iteracja - loop'y (while i for), z jasnymi warunkami zakończenia

W bloku operatorem sekwencji/konkatenacji operacji jest często średnik.

Należy ograniczyć korzystanie z break (w switch oczywiście dalej zezwolone), ograniczenie continue. W ewolucji względem Assemblera, absolutny zakaz goto, który sprawia, że przepływ nie jest liniowy. Chodzi o to, aby przepływ był jasny i ustrukturyzowany, nie tylko dla siebie, ale też dla innych programistów w zespole.

Można wspomnieć o wielu dobrych praktykach, jak

- wydzielanie zagnieżdżonych bloków do funkcji o jasnych nazwach
- dzielenie długich bloków na funkcje
- jasne nazywanie zmiennych i struktur (idealnie, brak potrzeby komentarzy, zamiast tego dobrze nazwane funkcje)
- unikanie zmiennych globalnych
- unikaj nadmiernego powtarzania się
- unikaj złożonych instrukcji warunkowych i iteracyjnych

Jeszcze jedna ciekawostka - instrukcja wiążąca. Np. zamiast

```cs
var p1 = new Person();
p1.name = "miki";
p1.surname = "fiki";
```

to

```cs
var p1 = new Person { name = "miki", surname = "fiki" };
```

Dla kolekcji też od razu dane (dla C\# to i tak syntactic sugar)
