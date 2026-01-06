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
Dla S i R = 1 stan nie jest zdefiniowany (może być losowy)
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
