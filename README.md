# Obrona

## jak wygląda

Jak wygląda obrona? Macie wyznaczoną godzinę, przychodzicie do sali, jest 3-osobowa komisja i zadają Wam 3 pytania z zakresu egzaminu dyplomowego (ze strony wydziału lub programu studiów). Opracowania tych zagadnień Wam wyślę, mamy klika wersji, w zależności kto w jaką ocenę celuje, ale sprawdźcie, czy jakieś nowe zagadnienia Wam nie wskoczą. Pytań do Waszego ZPI na obronie nie ma, z racji tego, że to nie jest inżynierka, tylko zwykły kurs, więc przygoda z ZPI się kończy w połowie grudnia i już się do tego nie wraca (no chyba że chcecie sprzedawać ten projekt gdzieś, tak też można xd), ale na obronie są tylko 3 pytania ze studiów. Pytania dobierane są różnie, niektóre komisje losują, niektóre wybierają pod siebie, czyli takie tematy, na których się znają, a niektóre nawet pozwalają sobie wybrać pytania xd. Jak traficie? nie wiadomo, ale jak już będziecie znali składy komisji, to mogę tam o co niektórych powiedzieć jakieś wskazówki. Ale w większości przypadków pytania wybierane są przez komisję i z takich tematów, z których się znają, więc polecam się wtedy z takich pytań najlepiej przygotować, bo bardzo duża szansa, że padną. Jak już wybiorą pytania, to dają Wam kartkę z tymi zaznaczonymi, albo każą Wam zaznaczać no i możecie zacząć odpowiadać w dowolnej kolejności na nie. Mówicie tyle co wiecie i dopóki nie powiedzą Wam, że można przejść dalej. Czasem o coś dopytają, to też zależy od komisji, na ile miłe te pytania będą, ale starajcie się mówić cały czas, niekoniecznie wszystko musi być w 100% poprawne, ale ważne, żeby “brzmiało mądrze” i nie mieli kiedy Wam przerwać, bo wtedy ryzyko, że zadadzą jakieś pytanie, na które możecie nie znać odpowiedzi. Ważne, żeby cokolwiek powiedzieć i nie zacinać się. Po odpowiedzeniu na te 3 pytania poproszą Was na chwilkę o wyjście z sali, naradzą się i poproszą Was z powrotem, gdzie pogratulują, ogłoszą ostateczną ocenę i 3 uściski prezesów z gratulacjami dla nowego inżyniera :))) Możecie wtedy iść i robić sobie uroczystą fotkę pod A-1 z logiem PWr, tylko pamiętajcie, że my nie mamy żadnej pracy inżynierskiej, więc jeśli chcecie taką fotkę z pracą, to albo musicie od kogoś pożyczyć, albo samemu sobie wydrukować jakąś Waszą dokumentację projektu, albo kupić samą okładkę xd

## todo

### 1. Układy cyfrowe (s. 1-2)

* **Przerzutnik RS:** W tabeli prawdy jest stan `1 1` oznaczony jako "stan zabroniony". Warto wiedzieć **dlaczego**.
  * *Wyjaśnienie:* W zależności od tego, czy RS jest na bramkach NOR czy NAND, podanie dwóch aktywnych sygnałów (np. dwóch jedynek dla NOR) wymusza na obu wyjściach ($Q$ i $\neg Q$) ten sam stan (np. 0), co jest logicznie sprzeczne (bo jedno ma być negacją drugiego). Po zaniku sygnału układ wchodzi w stan nieustalony (losowy).
* **Przerzutnik D:** W opisie jest napisane "W przerzutniku D ustawienie samego pinu D... nie wystarczy".
  * *Doprecyzowanie:* Przerzutnik D (Data) zatrzaskuje stan wejścia D na wyjście Q w momencie **zbocza zegara** (narastającego lub opadającego). To jest kluczowe – działa synchronicznie.
* **Hazard:** Definicja jest poprawna, ale warto dodać, że hazard eliminuje się np. poprzez dodawanie nadmiarowych termów w funkcjach logicznych lub stosowanie układów synchronicznych (zegarowanych), gdzie stan ustala się przed zboczem zegara.

### 2. Arytmetyka i BCD (s. 3)

* **Kod BCD:** Przykład `49 -> 0100 1001` jest poprawny.
* *Pułapka:* Pytanie o "nadmiarowość". W BCD używamy 4 bitów (16 kombinacji) do zapisu cyfr 0-9 (10 opcji). 6 kombinacji (1010-1111) jest niewykorzystanych. To jest strata pamięci, ale ułatwienie przy wyświetlaniu wyników (nie trzeba dzielić przez 10, by wyświetlić cyfrę).

### 4. Programowanie obiektowe (s. 5)

* **Polimorfizm:** Definicja w notatkach jest bardzo ogólna ("wielopostaciowość"). Na obronie musisz rozróżnić:
  * **Polimorfizm statyczny (czasu kompilacji):** Przeciążanie metod (overloading) – ta sama nazwa, inne parametry.
  * **Polimorfizm dynamiczny (czasu działania):** Przesłanianie metod (overriding) – metoda w klasie pochodnej nadpisuje metodę w klasie bazowej (wymaga mechanizmu funkcji wirtualnych w C++ lub jest domyślne w Java/Python).
* **Interfejs vs Klasa Abstrakcyjna:**
  * Klasa abstrakcyjna może mieć zmienne (pola) i metody z implementacją.
  * Interfejs (w czystej teorii) to tylko kontrakt (same metody publiczne bez ciała), choć w nowszych wersjach Javy/C# to się zaciera (default methods).

### 5. Relacje (s. 7)

* **Antysymetria:** Definicja "jeśli xRy oraz yRx to x=y" jest poprawna.
* **Relacja Równoważności:** Zwrotna, Symetryczna, Przechodnia. (W notatkach jest OK).
* **Relacja Częściowego Porządku:** Zwrotna, **Antysymetryczna**, Przechodnia. Warto o tym pamiętać, bo to częste pytanie dodatkowe.

### 7. Architektury (s. 9-11)

* **Von Neumann vs Harvard:**
  * Kluczowa różnica: Von Neumann ma **wspólną szynę i pamięć** dla danych i instrukcji (wąskie gardło). Harvard ma **oddzielne**.
  * *Doprecyzowanie:* Współczesne procesory x86/ARM to hybrydy. Na zewnątrz wyglądają jak Von Neumann (jedna pamięć RAM), ale wewnątrz (cache L1) mają rozdzielenie na cache instrukcji i cache danych (Architektura Harvardzka wewnątrz CPU).

### 8. RISC vs CISC (s. 12-13)

* *Bardzo ważne:* W punkcie o RISC jest napisane "Load, execute, store".
  * RISC to architektura **Load/Store**. Oznacza to, że operacje arytmetyczne (dodawanie, mnożenie) dzieją się **tylko na rejestrach**. Nie można dodać liczby bezpośrednio z pamięci RAM (co jest możliwe w CISC). Najpierw trzeba załadować do rejestru (LOAD), policzyć, a potem zapisać (STORE).

### 11. Złożoność obliczeniowa (s. 19)

* **Problem komiwojażera:** W notatkach jest napisane "O(n^2 2^n)". To jest złożoność dla programowania dynamicznego. Dla brute-force to jest **O(n!)**. Warto to rozróżnić.

### 14. Protokoły sieciowe (s. 21-22)

* **TCP vs UDP:** To jest "pewniak" na obronie.
  * **TCP:** Połączeniowy, gwarantuje dostarczenie, kolejność pakietów i kontrolę przepływu (flow control). Wolniejszy (handshake).
  * **UDP:** Bezpołączeniowy, "wyślij i zapomnij". Szybszy, ale może gubić pakiety. Używany w streamingu, grach, DNS.

### 17. Zarządzanie pamięcią (s. 23-24)

* **Wskaźniki:** W C++ `new` alokuje na **stercie (heap)**. Zmienne lokalne są na **stosie (stack)**.
* **Wyciek pamięci (Memory Leak):** Warto wspomnieć, że w C++ trzeba ręcznie zwolnić (`delete`), a w Java/Python robi to **Garbage Collector**.
* *Pułapka:* Wskaźniki w C++ vs Referencje w Java/Python. W Pythonie wszystko jest obiektem i przekazywane jest "przez referencję do obiektu" (assignment is binding).

### 24. Bazy danych (s. 39-41)

* **Postacie normalne (Normalizacja):**
  * **1NF:** Wartości atomowe (nie ma list w jednej komórce).
  * **2NF:** Wszystkie pola niekluczowe zależą od **całego** klucza głównego (ważne tylko przy kluczach złożonych).
  * **3NF:** Brak zależności przechodnich (pole niekluczowe zależy od innego pola niekluczowego).
  * *Przykład z notatek:* "Zmiana stawki nauczyciela mianowanego pociąga konieczność zmian w całej tabeli" – to typowy problem braku 3NF (tabela powinna być rozbita na `Pracownicy` i `Stanowiska`).

### 29-30. Python vs Java & Równoległość (s. 45-48)

* **GIL (Global Interpreter Lock):** W notatkach (s. 46) jest pytanie "Czego oczekiwać od programów współbieżnych?". W Pythonie (CPython) istnieje GIL, który sprawia, że **wątki (`threading`) nie działają równolegle na wielu rdzeniach CPU** (działają współbieżnie na jednym rdzeniu przez przełączanie kontekstu).
  * *Korekta:* Aby w Pythonie wykorzystać wiele rdzeni (CPU-bound tasks), trzeba użyć `multiprocessing` (procesów), a nie `threading` (wątków). Wątki w Pythonie są dobre tylko do czekania na I/O (sieć, dysk).
* **Kompilacja:** Java kompiluje do Bytecode (uruchamianego przez JVM). Python też kompiluje do Bytecode (pliki `.pyc`), który jest interpretowany przez PVM. Różnica leży głównie w typowaniu (statyczne vs dynamiczne) i momencie sprawdzania błędów.

### 34. Kryptografia (s. 52-53)

* **Błąd logiczny w s. 53:** "MD5... łatwość w odhashowaniu".
  * **KRYTYCZNE:** Hashowania **nie da się odwrócić** ("odhashować"). To funkcja jednokierunkowa. Z hasha nie odzyskasz hasła. Możesz jedynie znaleźć hasło pasujące do hasha metodą prób i błędów (brute-force, słownikowa, tęczowe tablice) lub znaleźć kolizję. Użycie słowa "odszyfrowanie hasha" na obronie to "samobójstwo". Hashowanie to nie szyfrowanie.
* **Sól (Salt):** Dodaje się ją, żeby dwa takie same hasła miały różne hashe (chroni przed tablicami tęczowymi).

### 35. OLTP vs OLAP (s. 54)

* Warto dodać proste rozróżnienie:
  * **OLTP (Online Transaction Processing):** Baza operacyjna, sklep, bank. Dużo małych transakcji (INSERT, UPDATE). Musi być szybka i spójna (ACID).
  * **OLAP (Online Analytical Processing):** Hurtownia danych. Dużo odczytów (SELECT), skomplikowane agregacje (SUM, AVG) na danych historycznych.

### 38. Systemy Ekspertowe (s. 55)

* Warto wspomnieć o metodach wnioskowania:
  * **Wnioskowanie w przód (Forward chaining):** Od faktów do wniosków (mam katar i gorączkę -> mam grypę).
  * **Wnioskowanie wstecz (Backward chaining):** Od hipotezy do faktów (czy mam grypę? sprawdzam czy mam gorączkę).

### Podsumowanie - na co uważać

1. **Język:** Unikaj kolokwializmów typu "po ludzku", "robimy zdjęcia kotkom" (jak w notatkach) podczas oficjalnej odpowiedzi.
2. **Precyzja:** Hashowanie $\neq$ Szyfrowanie. Wątek $\neq$ Proces. Klasa abstrakcyjna $\neq$ Interfejs.
3. **Python:** Pamiętaj o GIL przy pytaniach o wielowątkowość.

Notatki są dobrą bazą, ale wymagają "przefiltrowania" przez bardziej formalny język techniczny. Powodzenia na obronie!

## komisja

---

### 1. Dr inż. Paweł Myszkowski ("Ten wymagający")

**Profil:** Specjalista od Sztucznej Inteligencji (SI), algorytmów metaheurystycznych i optymalizacji. Znany z tego, że jest konkretny, nie lubi "lania wody" i ceni zrozumienie tematu, a nie regułki. Bywa sarkastyczny.
**Czego szuka:** Czy rozumiesz złożoność obliczeniową? Czy wiesz, jak działa algorytm "pod maską"?

**Najbardziej prawdopodobne pytania z PDF (Priorytet Wysoki):**

* **Pytanie 21: Metody optymalizacji.** To jest jego "konik". Musisz znać różnicę między metodami gradientowymi a bezgradientowymi.
  * *Klucz:* Zrozumieć, o co chodzi w metodzie najszybszego spadku vs. algorytmy genetyczne.
* **Algorytmy genetyczne i ewolucyjne.**
  * *Klucz:* Znać pojęcia: genotyp, fenotyp, mutacja, krzyżowanie, funkcja przystosowania.
* **Pytanie 11: Złożoność obliczeniowa (Big O).**
  * *Klucz:* Nie myl O(n) z O(n^2). Pamiętaj, że dla niego wydajność jest kluczowa (w opiniach narzekał na brak profilera w projektach).
* **Pytanie 10: Algorytmy sortowania.**
  * *Klucz:* Złożoność QuickSort vs BubbleSort. Dlaczego QuickSort jest zazwyczaj szybszy?
* **Pytanie 21 (Str. 27-28): Identyfikacja obiektów / Modele.**
  * *Klucz:* Rozróżnienie modelu statycznego i dynamicznego.

**Jak odpowiadać:** Krótko, zwięźle, technicznie. Używaj fachowego słownictwa (iteracja, zbieżność, funkcja celu). Jeśli zapyta o kod/algorytm, opisz kroki logiczne.

---

### 2. Dr inż. Marcin Pietranik ("Ten od Baz Danych")

**Profil:** Specjalista od baz danych, systemów webowych i integracji systemów. Pro-studencki, ale ceniący logiczne myślenie. Nie cierpi archaicznych rozwiązań (jak MS Access w profesjonalnych zastosowaniach) i "szkolnych" definicji, które nie mają pokrycia w praktyce. Fan nowoczesnych rozwiązań (NoSQL).
**Czego szuka:** Czy rozumiesz, dlaczego używasz danej bazy? Relacyjna czy NoSQL?

**Najbardziej prawdopodobne pytania z PDF (Priorytet Wysoki):**

* **Pytanie 24: Modele baz danych (Relacyjne vs NoSQL).**
  * *Klucz:* To jest pewniak. Musisz wiedzieć, kiedy użyć SQL (spójność, ACID), a kiedy NoSQL (skalowalność, elastyczność schematu).
* **Normalizacja.**
  * *Klucz:* Znać postacie normalne (1NF, 2NF, 3NF), ale – uwaga – Pietranik ceni wiedzę praktyczną, więc wspomnij o **denormalizacji** w celach wydajnościowych (w systemach OLAP lub NoSQL).
* **Pytanie 35: OLAP i wielowymiarowe modelowanie.**
  * *Klucz:* Różnica między OLTP (transakcyjne, bieżące) a OLAP (analityczne, historyczne).
* **Pytanie 22: Internet Rzeczy (IoT) i Big Data.**
  * *Klucz:* Jak przechowywać ogromne ilości danych z sensorów? (Tu wchodzi NoSQL/Big Data).
* **Pytanie 15: Protokoły warstwy aplikacji (HTTP, REST).**
  * *Klucz:* Jako webowiec może zapytać o REST API.

**Jak odpowiadać:** Praktycznie. Możesz powiedzieć: "Teoretycznie robi się tak, ale w praktyce przy dużych systemach robi się tak...". To zaplusuje.

---

### 3. Dr inż. Marcin Kawalerowicz ("Ten z Biznesu")

**Profil:** CEO firmy software'owej, programista .NET, ekspert od inżynierii oprogramowania i jakości kodu. Człowiek z przemysłu, nie akademicki teoretyk.
**Czego szuka:** Inżynierii oprogramowania, Wzorców Projektowych, testowania, cyklu życia oprogramowania (Agile).

**Najbardziej prawdopodobne pytania z PDF (Priorytet Wysoki):**

* **Pytanie 32: Wzorce projektowe.**
  * *Klucz:* To jego chleb powszedni. Naucz się 3 przykładów na pamięć: Singleton (i dlaczego jest zły), Fabryka, Obserwator. Wiedza, kiedy ich użyć, jest kluczowa.
* **Pytanie 26: Cykl życia oprogramowania (Waterfall vs Agile/Scrum).**
  * *Klucz:* Kawalerowicz jest "agile'owcem". Zna Scruma na wylot. Różnice między podejściem zwinnym a kaskadowym.
* **Pytanie 4: Programowanie obiektowe (OOP).**
  * *Klucz:* Polimorfizm, Hermetyzacja, Dziedziczenie. Podstawy, ale w kontekście C#/Java.
* **Pytanie 16: Techniki efektywnego programowania / Zarządzanie pamięcią.**
  * *Klucz:* Unikanie wycieków pamięci, alokacja na stosie vs stercie.
* **Pytanie 31: UML.**
  * *Klucz:* Diagramy klas i sekwencji. Używane w dokumentacji projektowej.

**Jak odpowiadać:** Biznesowo i inżyniersko. Odwołuj się do pracy w zespole, utrzymania kodu (maintainability) i testowalności.

---

### Szybka "ściąga" przygotowawcza (Plan działania)

1. **Dla Myszkowskiego:**
    * Otwórz **stronę 30** PDFa. Wykuj na blachę metody optymalizacji (Gradientowe vs Ewolucyjne).
    * Otwórz **stronę 19**. Zrozum "O duże".
    * Otwórz **stronę 16**. Zrozum QuickSort.

2. **Dla Pietranika:**
    * Otwórz **stronę 38**. Zrozum ACID.
    * Otwórz **stronę 37**. Zrozum różnicę SQL vs NoSQL.
    * Otwórz **stronę 39-41**. Przypomnij sobie 3 postacie normalne (to jest baza, którą musisz znać, żeby zdać u "bazodanowca").

3. **Dla Kawalerowicza:**
    * Otwórz **stronę 51-52**. Wybierz jeden wzorzec z każdego typu (Kreacyjny, Strukturalny, Behawioralny) i umiej go opisać.
    * Otwórz **stronę 44**. Zrozum Model Spiralny i Kaskadowy (i dlaczego w IT wolimy Agile/Scrum, mimo że w PDF jest Kaskadowy).

### Symulacja obrony (Przykładowy scenariusz)

* **Myszkowski:** "Proszę omówić metody gradientowe w optymalizacji. Jak wyznaczamy kierunek spadku?" (Odpowiedź ze str. 30 – antygradient).
* **Pietranik:** "Mamy system dla sklepu internetowego. Jaką bazę danych Pan wybierze i dlaczego? Co to jest transakcyjność?" (Odpowiedź: Relacyjna dla płatności ze względu na ACID/Spójność - str. 38, ewentualnie NoSQL dla koszyka/katalogu produktów).
* **Kawalerowicz:** "Proszę wymienić i omówić wzorzec projektowy, który ułatwia tworzenie obiektów bez określania ich konkretnej klasy." (Odpowiedź: Fabryka - str. 52).

Powodzenia! To dobra komisja, o ile nie będziesz ściemniać. Jak czegoś nie wiesz, spróbuj wydedukować lub nawiązać do praktyki – Pietranik i Kawalerowicz to docenią. Myszkowski może kręcić nosem, ale 2/3 głosów masz po swojej stronie.
