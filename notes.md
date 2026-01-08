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
Bardzo prosty i asynchroniczny (czyli nie wymaga obecności zegara)\
S ustawia stan układu (Q) na wysoki dla S = 1\
R ustawia stan układu na niski dla R = 1\
Dla S i R = 0 stan pozostaje taki sam, czyli Q[n] = Q[n-1]\
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

## 4. Programowanie obiektowe - podstawowe pojęcia, zastosowania

Paradygmat obiektowy to jeden z najpopularniejszych paradygmatów. Jest on intuicyjny, ponieważ może tłumaczyć zjawiska ze świata rzeczywistego na obiekty i klasy, np. każdy człowiek posiada imię, ale konkretny człowiek ma własne imię.

Podstawowe pojęcia:

- Obiekt: zbiór własności tego obiektu oraz metod
- Klasa: instrukcja wykorzystywana do instancjonowania obiektów. Jest to blueprint z polami, metodami
- Pole/atrybut: "zmienne" klasy. Klasa definiuje pola (zazwyczaj z typami), a obiekty typu tej klasy mogą zazwyczaj mieć różne wartości danego pola, oraz mogą je zmieniać w czasie (przy zmianie, klasa jest mutowalna, niezmienne typy to np. record czy struct z C\#)
- Metoda: "funkcja" klasy. O ile nie jest oznaczona jako statyczna, to wykonując ją na instancji klasy mamy dostęp do jej pól zazwyczaj przez mechanizm self/this itd. W wielu językach jest to niejawne, w Python trzeba przekazać self do takiej metody. Metoda działa jak zwykła funkcja, może zwracać coś, może mutować pola klasy, może instancjonować itd itd
- Dziedziczenie: klasa może dziedziczyć po innej klasie. Oznacza to, że wszystkie pola, metody klasy dziedziczonej są jakby "kopiowane" do klasy dziedziczącej. Bardzo przydatne, ale w praktyce można potem wpaść na ograniczenia tego i próbę upychania zbyt wielu rzeczy w klasę. Często stosuje się composition (kompozycję), czyli klasa ma inne instancje klas jako pola i w ten sposób rozszerza się jej możliwości (przykład z gier: gracz i wrogowie mają zdrowie i atak. to można by zrobić jako jedną klasę character i dziedziczyć. ale potem krzesła mają zdrowie bo reagują na wybuchy, no i przez dziedziczenie musiałyby w nieładny sposób nadpisać pewnie metody ataku. a przy kompozycji to osobne moduły, nie powiązane w sposób ścisły ze sobą)
- Interfejsy: kontrakt zobowiązujący klasę do implementacji metod z interfejsu i sprawiający, że inne części kodu mogą prawidłowo oczekiwać, że klasa potrafi wszystko w kontrakcie
- Klasa abstrakcyjna: klasa oznaczona keywordem ```abstract```. Pewnie posiada metody abstrakcyjne z samą sygnaturą metody (nazwa, argumenty, return value). Nie można bezpośrednio instancjonować, dopiero nieabstrakcyjne klasy dziedziczące mogą.
- Przesłanianie metody: nadpisanie działania metody w klasie dziedziczącej. Często wykorzystuje się np. ```base().TaMetoda();```, ale nie trzeba
- Przeciążanie metody: zdefiniowanie metody parę razy w klasie, ale każda z różnymi argumentami. Przydatne, gdy klasa akceptuje różne metody wywołania. Częstą praktyką jest to, że wszystkie te metody zwracają wynik z jednej, głównej, wybranej, która przyjmuje argumenty w dogodnej postaci. Np. w Unity instancja obiektu w scenie może mieć pozycję, rotację, rodzica... różnego rodzaju typ layera... każda metoda przekazuje argumenty jakiejś jednej.\
- Polimorfizm: jak kot dziedziczy po zwierzęciu to można traktować go tak i tak, czyli wsadzić do listy zwierząt i traktować jak zwierzę, bez zwracania uwagi na konkretny typ.
- Modyfikator dostępu: metody i pola w klasach mogą być public, private, protected. Public wiadomo metoda dostępna dla innych klas, private tylko dla klasy (inna instancja może w kodzie metody korzystać z metody prywatnej innej instancji). Protected to jak private, ale dodatkowo dostępne dla klas dziedziczących.
- Hermetyzacja: modyfikatory dostępu, interfejsy przydają się do implementacji hermetyzacji. Chodzi o to, aby dla innych klas najważniejszy był głównie wynik którego potrzebują od klasy, a nie wewnętrzna implementacja. Czyli klasa powinna udostępniać minimum metod i publicznych pól, aby inne klasy musiały w kontrolowany sposób ją mutować / uzyskiwać z niej wynik.

Programowanie obiektowe można stosować praktycznie wszędzie. Prawie wszystkie większe gry komputerowe są napisane w tym paradygmacie, ale też dużo aplikacji desktopowych, mobilnych, backendów, frontendów, systemy operacyjne...

## 5. Podstawowe operacje na zbiorach, funkcjach i relacjach. Rachunek zdań. Rachunek kwantyfikatorów

Podstawowe operacje na zbiorach:

Suma zbiorów A + B czyli zbiór do którego należą wszystkie elementy w zbiorze A i w zbiorze B
Różnica zbiorów A - B czyli wszystkie elementy zbioru A, poza tymi, które są w zbiorze B (jest też różnica symetryczna taki xor)
Iloczyn A i B czyli wszystkie elementy będące naraz w zbiorze A i B
Dopełnienie A czyli wszystkie elementy, które są poza A w jakimś zbiorze dostępnych wartości U (czyli U - A) (U to zbiór wszystkich możliwych wartości)
Iloczyn kartezjański A x B czyli wszystkie możliwe pary każdy element a R b zebrane w pary uporządkowane.
Pary uporządkowane to takie, że jeśli (a,b) = (c,d), to a=c i b=d
Przynależność A e B gdy każdy element A znajduje się również w zbiorze B

Własności działań na zbiorach:
Operacje sumy, różnicy są przemienne

```txt
A * (B + C) = (A * B) + (A * C)
A + (B * C) = (A + B) * (A + C)
A + (B + C) = (A + B) + C
A * (B * C) = (A * B) * C
A \ B = A * B`
(A * B)` = A` + B`
(A + B)` = A` * B`
```

Potoczna definicja funkcji: Jeśli mamy 2 zbiory X i Y, i stworzymy relację dla każdego X dokładnie jeden Y, to takie przyporządkowanie to funkcja.
Funkcje mozna składać, np h(x) = f(g(x)) = (f o g)(x)
Funkcje to relacje, więc można na nich wykonywać operacje mnogościowe, ale nie zawsze wyjdzie z tego funkcja\

Relacja to podzbiór iloczynu kartozjańskiego
Relacje mogą mieć wiele własności

- Symetryczna - jeśli x R b, to b R x
- Zwrotna - każde x jest x R x
- Przechodnia - jeśli x R y i y R z, to x R z
- Antysymetryczna - jeśli x R y i y R x, to x = y (takie wnioskowanie z symetrii)
- Spójna - wszystkie elementy są w parze z wszystkimi innymi (przynajmniej w jedną stronę)

Relacja jest relacją równoważności, gdy jest zwrotna, symetryczna i przechodnia (taki graf trochę niekierunkowy)

Rachunek zdań

```txt
                    implikacja        xnor
ab  a ∧ b  a ∨ b    a => b  b => a    a <=> b (a => b) ∧ (b => a)    
00  0      0        1       1         1                             
10  0      1        0       1         0
01  0      1        1       0         0
11  1      1        1       1         1
```

negacja to wiadomo

zdania są równoważne, gdy mają równe wartości logiczne dla wszystkich możliwości np. a = a * a
tautologia jest zawsze prawdziwa np. p + p` = 1

Mamy kwantyfikatory A; V (dla każdego; istnieje)
Czyli np. Ax; x w zbiorze R; x*x >= 0
Vx; x w zbiorze R; x = 123.25
Oba to prawda

## 6. Deterministyczne automaty skończone - definicja, zastosowania

Chodzi o takie fajne rzeczy jak regex czy lekser.
Jest to abstrakcyjna maszyna stanów o skończonej liczbie stanów, która na podstawie aktualnie czytanej litery i aktualnego stanu (na początku pusty) przechodzi do kolejnego stanu. Gdy znajdzie się w stanie oznaczonym jako akceptujący (końcowy), przerywa działanie, klasyfikując czytane słowo/tekst do języka regularnego, do rozpoznawania którego jest zbudowane.

![alt text](imgs/6/deterministyczny_automat_skonczony.png)

Formalnie, automat skończony to uporządkowana piątka ```A = <K, T, M, K0, H>```
K = niepusty skończony zbiór - stanów
T = niepusty skończony zbiór - alfabet
M = relacja przejścia K x T -> K
K0 e K - stany początkowe
H e K - stany końcowe/akceptowalne

Lekser jest używany w kompilatorach i interpreterach.
Regex jest wykorzystywany przy wytwarzaniu oprogramowania głównie do walidacji inputu użytkownika, znalezienie odpowiedniego tekstu/tekstów, zamienienia fragmentów tekstu.

Przykłady regexa:
znalezienie wszystkich słów w tekście (litery między innymi znakami)

```regex
[a-zA-Z]+
```

znalezienie wszystkich słów zaczynającego się na "pies"

```regex
pies[a-zA-Z]*
```

znalezienie liczb o długości 5

```regex
\d\d\d\d\d
```

walidacja maila lvl easy

```regex
.+@.+\..+
```

## 7. Przykładowe architektury komputerów: von Neumana, Princeton, Harvard

Komputer składa się z CPU (jednostki centralnej), magistrali, pamięci. CPU składa się z rejestrów, ALU (matematyka) i jednostki sterującej.

Ze względu na liczbę strumieni danych a instrukcji powstała Taksonomia Flynna o 4 rodzajach:

- SISD - najprostsze, jeden ciąg instrukcji i jeden danych
- SIMD - np. GPU, te same instrukcje są wywoływane dla różnych porcji danych (ale CPU też może być)
- MISD - dąży do zmniejszenia marginesu błędu przez redundancję obliczeń (bardzo rzadkie, misje kosmiczne)
- MIMD - wiele programów ma różne dane (komputery osobiste)

von Neumann / Princeton
Von Neumann i Princeton to dwie różne nazwy na tą samą architekturę komputerów. Charakteryzuje się przechowywaniem instrukcji razem z danymi. Instrukcje mogą łatwo modyfikować inne instrukcje. Problem, jaki występuje, to von Neumann/Princeton bottleneck, czyli ograniczenie wykonywania instrukcji przez czytanie danych (bottleneck). System powinien mieć skończoną i kompletną listę instrukcji.

Harvardzka
Rozdzielenie instrukcji od danych do osobnych szyn. Łagodzi to wcześniej opisany problem bottleneck.

Większość komputerów i GPU korzysta ze zmodyfikowanej architektury Harvardzkiej, optymalizującej działanie. Logicznie jest to von Neumann, ale fizycznie ścieżki i cache są rozdzielone dla instrukcji i danych.

## 8. Procesory typu RISC i CISC - charakterystyka, różnice

RISC a CISC to dwa podejścia do projektowania procesorów, różniące się filozofią wobec tego, ile cykli zegara mogą zajmować instrukcje.

CISC (Complex Instruction Set Computing) zakłada, że niektóre operacje mogą trwać kilka do nawet kilkunastu cykli zegara - złożone, specjalistyczne rozkazy. Dodatkowo, instrukcje mogą operować na danych z pamięci, a nie tylko na tych z rejestrów. Jest to swego rodzaju abstrakcja dla programisty. Przez to wszystko dekoder rozkazów jest skomplikowany.

RISC (Reduced Instruction Set Computing) starał się zoptymalizować CISC, po zauweżeniu, jak niewielki procent ogólnie operacji faktycznie był wykonywany dłużej niż 1 cykl zegara. Jest to architektura mikroprocesorów. Zmniejsza o rząd wielkość liczbę możliwych operacji do parudziesięciu. Upraszcza to dekoder rozkazów. Każda operacja zajmuje 1 cykl zegara. Dane nie mogą operować bezpośrednio na danych z pamięci, dlatego stosuje się proces Load, Process, Store. Czyli załadowanie do jednego z wielu rejestrów w takim procesorze (może być ich 30 do ponad setki), przeprowadzenie obliczeń, i zapisanie wyniku.

RISC są szybkie, ale trudniejsze bez abstrakcji CISC dla programisty. Dlatego niektóre procesory (x86) logicznie to CISC, a tak naprawdę mają wewnątrz jednostkę RISC. ARM to rodzaj procesorów, które są RISC, i są znane z małego poboru prądu i szybkości.

Dodatkowe porównanie:
RISC: 1 zegar i ograniczony tryb adresowania. CISC wykorzystuje wielodostępne tryby adresowania.
RISC: ustalony format instrukcji 32 bity. CISC: zmienne zakresy od 16-64 bitów na instrukcję.
RISC: sterowana na stałe bez konieczności pamięci sterującej. CISC kiedyś wymagało pamięci kontrolnej (ROM), ale teraz można tak jak RISC

## 9 Grafy. Drzewa rozpinające. Cykle Eulera i Hamiltona. Spójność. Algorytmy przechodzenia po grafie

Graf to taka struktura danych, która składa się z wierzchołków, połączonych z innymi wierzchołkami krawędziami. Wierzchołki, krawędzie i same grafy mogą mieć różne własności, w zależności od typu grafu.

Typy grafów:

- etykietowane: wierzchołki są podpisane
- ważone: każda krawędź ma wagę (liczba, zazwyczaj pozytywna, ale może być też ujemna/zerowa, choć niektóre algorytmy przestają wtedy działać)
- skierowane: krawędź ma początkowy wierzchołek i końcowy wierzchołek (mogą być te same, ale jest kierunek)
- nieskierowane: krawędź łączy 2 wierzchołki w 2 strony, można nim przejść w obie strony
- spójne: z każdego wierzchołka można się dostać do każdego innego
- niespójne: istnieją wierzchołki, między którymi nie da się wyznaczyć drogi
- Eulerowskie: ma cykl Eulera
- Hamiltonowski: ma cykl Hamiltona
- regularne: każdy wierzchołek tego samego stopnia, czyli równa ilość krawędzi z każdego wierzchołka

Droga: lista krawędzi od wierzchołka początkowego do końcowego
Ścieżka: droga co nie powtarza wierzchołków
Cykl (droga zamknięta): A -> B -> A
Pętla: A -> A
Drzewo: graf spójny acykliczny (czyli nie ma żadnego cyklu)

Drzewo rozpinające: podgraf grafu zawierający wszystkie jego wierzchołki, ale pomijając krawędzie tworzące cykle. Dzięki temu jest niecykliczny i jest spójny. Dany graf może mieć wiele drzew rozpinających

W drzewach binarnych (są drzewami rozpinającymi) krawędzie mają najwyżej (i zazwyczaj dokładnie) dwójkę dzieci. Są one oznaczone jako lewe i prawe. Krawędzie, które nie mają dzieci, to liście (leaf). Korzeniem jest główny rodzic.

Cykle Eulera i Hamiltona
Cykl Eulera: można stworzyć drogę, rozpoczynającą się w jakimś wierzchołku, i przejść przez wszystkie krawędzie dokładnie raz
Cykl Hamiltona: można stworzyć drogę, rozpoczynającą się w jakimś wierzchołku, przechodzącą przez wszystkie wierzchołki raz, prócz początkowego, w którym trzeba skończyć.
Ścieżka Hamiltona:

Spójność: chodzi o to, że z każdego wierzchołka można by się dostać do każdego innego.

Algorytmy przechodzenia po drzewie rozpinającym (w akademii zazwyczaj dotyczą drukowania etykiet/indeksów w jakiejś kolejności grafu):

- DFS (depth first search): chciwe, eksplorują ściężki jak najgłębiej, zanim sprawdzą inne (rekurencyjne)
  - pre order: zaczyna w głównym wierzchołku i wykonuje dla niego taki sam algorytm jak dla reszty, czyli najpierw operuje na sobie, potem idzie ciągle do lewego dziecka, jak je wyczerpie, to prawe, a potem wraca do rodzica (noo w przypadku korzenia rodzica nie ma, to koniec algorytmu).
  - post order: pre order, ale operacja na wierzchołku dopiero na końcu, najpierw dzieci
  - in order: najpierw wykonuje algorytm dla lewego dziecka, potem wypisuje siebie, potem prawego
- BFS (breadth first search): jakby założenie, że każda ścieżka ma tyle samo potencjału (iteracyjne)
  - często takie drzewa binarne są w postaci idealnie skonstruowanej do takiej iteracji, bo korzeń ma indeks 0, lewe dziecko 1, prawe 2, lewe lewego 3 itd.
  - level order - zwykły bfs

Są inne ale te najwazniejsze

Niektóre starają się stworzyć minimalne drzewo rozpinające, czyli dla grafu ważone takie, których suma wag krawędzi jest najmniejsza możliwa (minimalna)

Djikstra to algorytm zachłanny (BFS), mający szybko znaleźć połączenie dwóch krawędzi o najmniejszej wadze. Działa tylko dla wag nieujemnych

Travelling Salesman problem można wspomnieć, mrówczano-feromonowe rozwiązanie

## 10. Pojęcie algorytmu. Algorytmy sortowania. Algorytmy wyszukiwania

Algorytm (definicja nieformalna) to sposób postępowania (przepis), jak rozwiązać zadanie (klasę zadań), podany w postaci skończonego zestawu czynności, ze wskazaniem ich następstwa.

Komputery korzystają z algorytmów, aby przetworzyć przekazane im dane. Każdy poprawny algorytm można przełożyć na zestaw instrukcji dla teoretycznego modelu komputera - maszyny Turinga.

Algorytmy typowo przyjmują parametry wejściowe, modyfikują stan wewnętrzny w komputerze i zwracają wynik. Niektóre programy korzystają z algorytmów, których jedynym zadaniem jest modyfikacja tego stanu wewnętrznego.

Algorytm musi mieć skończoną i kompletną liczbę instrukcji, w języku jednoznacznie zrozumiałym przez komputer. Ludzie komunikują się niejednoznacznie, kod musi być jednoznacznie interpretowany przez komputer. Aby program był obliczalny, jego wykonanie musi być możliwe w akceptowalnym czasie na konkretnej maszynie z określoną mocą obliczeniową i pamięcią. Komputery, z których korzystamy, są skończonym przybliżeniem maszyny Turinga, min. bo mają ograniczoną pamięć. Nowoczesne języki programowania, za to, są Turing complete.

Algorytmy sortowania: często występuje potrzeba uporządkowania obiektów według pewnego klucza/algorytmu. Dla lepszej prezentacji dla człowieka, uporządkowania danych, do innych algorytmów (np. wyszukiwania). Zazwyczaj sortuje się obiekty po jednym z ich atrybutów, często numerycznym. Ale można w wielu językach zdefiniować własną funkcję/lambdę sortującą, której zadaniem jest wzięcie dwóch elementów. Konwencja: zwrócenie 0 jeśli są równe jeśli chodzi o to, po czym sortujemy, x>0 jeśli np. lewy element jest większy, x<0 jeśli prawy. Algorytmy sortowania generalnie wspierają sortowanie rosnąco i malejąco. Algorytmy mogą sortować stabilnie (kolejność oryginalna będzie zachowana dla równych elementów). In place - sortuje bezpośrednio na oryginalnej tablicy.

Przedstawię algorytmy sortowania, posortowane malejąco po ich własności - średniej złożoności czasowej.

- Bubble sort - przechodzi od lewej do prawej, sprawdzając po drodze, czy sąsiedzi są w dobrej kolejności. Jeśli nie, zamienia ich kolejność. Bubble, bo jeśli duża wartość jest na początku, to bąbelkuje do góry.\
Czas: O(n^2). Pamięć: O(1)
- Insertion sort - jak karty w ręce. Bierzemy kartę do posortowanej listy, potem kolejno bierzemy karty, umieszczającym je w odpowiednie miejsce, między jakieś karty.\
Czas: O(n^2). Pamięć: O(1)
- Selection sort: za każdym razem szukamy minimum/maksimum i umieszczamy na końcu/początku posortowanej listy.\
Czas: O(n^2). Pamięć: O(1)
- Quick sort: bierzemy pivota, dajemy wszystkie mniejsze na lewo, wszystkie większe na prawo. Rekurencyjnie.\
Czas: średnia O(n*log n). Pesymistyczna: O(n^2). Pamięć: O(log n), pesymistycznie O(n)
- Heap sort: użycie kolejki priorytetowej przy wykorzystaniu binarnego kopca zupełnego (które mają dostęp łatwy do min i max, szybkie wstawianie i usuwanie elementów - logarytmiczny czas). Najpierw się kopcujesz, potem właściwe sortowanie.\
Czas: O(n*log n). Pamięć: O(n) lub O(1) dla mądrej implementacji
- Merge sort: Ciągle dzielimy ciąg na 2 równe części, aż mamy tylko 1 element (posortowany jest), a potem ciągle w górę i możemy scalać, bo łatwo scalić 2 posortowane ciągi w 1.
Czas: O(n*log n). Pamięć: O(n)
- Counting sort: bardzo fajny algorytm. Jeśli znamy zakres liczb, to możemy po prostu zrobić listę prewypełnioną zerami o długości max-min (= k). Potem przechodzimy przez każde do posortowania i robimy ```sorted[num]++;```. Overkill dla paru liczb, działa na całkowitych liczbach tylko\
Czas: O(n + k). Pamięć: O(n + k)

Algorytmy wyszukiwania:

- liniowy: porównujemy każdy element, aż znajdziemy. O(n)
- logarytmiczny: dzielimy posortowany array na mniejsze połówki, patrząc, gdzie byłby szukany element. O(log n)

Jeszcze inne fajne struktury danych

- hash table - aby znaleźć element, obliczasz hash, i wiesz, że jeśli jest w tabeli, to w liście, która jest pod hashem obliczonym. Generalnie O(1), ale przez to, że kompresuje się różne hashe przy użyciu modulo do 1 listy, może być O(n) (kolizja)
- bst - binarne drzewo przeszukiwań: mamy drzewo, gdzie dla każdego węzła dziecko po lewej jest mniejsze, dziecko po prawej większe. Warto równoważyć drzewa - AVL i Red-Black, to mamy O(log n)
- linked list - lista z obiektów, przechowujących następny i poprzedni element. Bardzo łatwe usuwanie i dodawanie elementów, niezależnie czy w środku itd

## 11. Podstawy analizy algorytmów. Złożoność obliczeniowa

Algorytmy warto analizować pod kątem ich złożoności obliczeniowej - czasu i pamięci. Wykorzystuje się do tego 3 notacje, oraz pojęcia złożoności średniej, pesymistycznej i optymistycznej. Złożoność średnia liczona jest względem przyjętego rozkładu danych, zazwyczaj jednostajnego. Pesymistyczna zakłada najgorszy możliwy zbiór danych wejściowych. Optymistyczna najlepszy możliwy.

Złożoności przedstawia się jako funkcja od liczby danych wejściowych. Nie jest to dokładna funkcja, ma przedstawić rząd złożoności. Tak więc np. f(n) = (n/100000000000)^3 + 3*n^2 + 92.5 => O(n^3). Można by powiedzieć, że to lim n->nieskończoność. Nie ma również potrzeby podawać bazy logarytmu. Służy więc to głównie porównywaniu algorytmów, ale trzeba mieć na uwadze, że niższa złożoność nie gwarantuje fizycznie szybszego czasu wykonania dla niektórych danych (np. algorytm szybki może wymagać kosztownych operacji matematycznych, przygotowania odpowiedniej struktury danych itd.).

Typowe rzędy złożoności (przykłady czasu):

- O(1): natychmiastowy, np. lista[0]
- O(log n): wyszukiwanie logarytmiczne
- O(n): wyszukiwanie liniowe
- O(n*log n): merge sort (szybkie są, rosną powoli wraz ze wzrostem n)
- O(n^2): bubblesort
- O(n^k): wielomianowa (stałe k)
- O(k^n): wykładnicza (stałe k)
- O(n!): silnia (superwykładnicza - proste rozwiązanie travelling salesman)

Przyjmuje się, że akceptowalna jest <= wielomianowa. Niektóre problemy są jednak prawdopodobnie zbyt skomplikowane, aby opracować takie algorytmy, np. optymalne rozwiązanie travelling salesman. Wtedy innym rozwiązaniem może być szukanie nienajlepszego, ale akceptowalnego rozwiązania (mrówki)

Wykorzystuje się 3 notacje:
Notacja O: najlepsze górne ograniczenie, czyli jak O(n^2), to algorytm też jest być O(n^3), ale Big O = O(n^2)
Notacja Omega: asymptotyczne dolne ograniczenie złożoności, czyli lepiej niż O(n) nie będzie, ale może być O(n^2)
Notacja Theta: ścisłe ograniczenie. Może być tylko, kiedy Omega=O. Wtedy Theta=Omega=O.
