# Obrona

## jak wygląda

Jak wygląda obrona? Macie wyznaczoną godzinę, przychodzicie do sali, jest 3-osobowa komisja i zadają Wam 3 pytania z zakresu egzaminu dyplomowego (ze strony wydziału lub programu studiów). Opracowania tych zagadnień Wam wyślę, mamy klika wersji, w zależności kto w jaką ocenę celuje, ale sprawdźcie, czy jakieś nowe zagadnienia Wam nie wskoczą. Pytań do Waszego ZPI na obronie nie ma, z racji tego, że to nie jest inżynierka, tylko zwykły kurs, więc przygoda z ZPI się kończy w połowie grudnia i już się do tego nie wraca (no chyba że chcecie sprzedawać ten projekt gdzieś, tak też można xd), ale na obronie są tylko 3 pytania ze studiów. Pytania dobierane są różnie, niektóre komisje losują, niektóre wybierają pod siebie, czyli takie tematy, na których się znają, a niektóre nawet pozwalają sobie wybrać pytania xd. Jak traficie? nie wiadomo, ale jak już będziecie znali składy komisji, to mogę tam o co niektórych powiedzieć jakieś wskazówki. Ale w większości przypadków pytania wybierane są przez komisję i z takich tematów, z których się znają, więc polecam się wtedy z takich pytań najlepiej przygotować, bo bardzo duża szansa, że padną. Jak już wybiorą pytania, to dają Wam kartkę z tymi zaznaczonymi, albo każą Wam zaznaczać no i możecie zacząć odpowiadać w dowolnej kolejności na nie. Mówicie tyle co wiecie i dopóki nie powiedzą Wam, że można przejść dalej. Czasem o coś dopytają, to też zależy od komisji, na ile miłe te pytania będą, ale starajcie się mówić cały czas, niekoniecznie wszystko musi być w 100% poprawne, ale ważne, żeby “brzmiało mądrze” i nie mieli kiedy Wam przerwać, bo wtedy ryzyko, że zadadzą jakieś pytanie, na które możecie nie znać odpowiedzi. Ważne, żeby cokolwiek powiedzieć i nie zacinać się. Po odpowiedzeniu na te 3 pytania poproszą Was na chwilkę o wyjście z sali, naradzą się i poproszą Was z powrotem, gdzie pogratulują, ogłoszą ostateczną ocenę i 3 uściski prezesów z gratulacjami dla nowego inżyniera :))) Możecie wtedy iść i robić sobie uroczystą fotkę pod A-1 z logiem PWr, tylko pamiętajcie, że my nie mamy żadnej pracy inżynierskiej, więc jeśli chcecie taką fotkę z pracą, to albo musicie od kogoś pożyczyć, albo samemu sobie wydrukować jakąś Waszą dokumentację projektu, albo kupić samą okładkę xd

## czego nie będzie

```txt
37. Wyrażenia i dyrektywy MDX.
```

## todo

## komisja

### Oto strategia "snajperska" pod tę konkretną komisję

---

#### 1. Dr hab. inż. Paweł Myszkowski ("Mózg Operacji / Algorytmik")

**Analiza profilu:**
Jego tematy prac to: *„Problemy trasowania pojazdów” (VRP)*, *„Szeregowanie zadań”*, *„Metody ewolucyjne”*, *„Metaheurystyki”*, *„Problemy czarno-skrzynkowe”*.
Jest to czysta algorytmika i optymalizacja. Nie zapyta Cię o bazy danych ani o Scruma. Zapyta o to, jak komputer rozwiązuje trudne problemy matematyczne.

**Strzały w dziesiątkę (Pytania z PDF):**

1. **Pytanie 30 (Str. 30): Metody optymalizacji.**
    * **Dlaczego:** To jest definicja jego kariery naukowej.
    * **Co musisz wiedzieć:** Rozróżnienie metody **gradientowej** (szukanie lokalnego ekstremum, "schodzenie z górki") od metod **bezgradientowych/metaheurystycznych** (jak algorytmy genetyczne, przeszukiwanie globalne).
2. **Pytanie 31 (Str. 31): Algorytmy genetyczne i ewolucyjne.**
    * **Dlaczego:** Promuje prace o metodach ewolucyjnych.
    * **Co musisz wiedzieć:** Pojęcia: **Populacja, Genotyp vs Fenotyp, Funkcja Przystosowania (Fitness function), Krzyżowanie, Mutacja**. Musisz umieć opowiedzieć ten proces jako cykl.
3. **Pytanie 9 (Str. 13): Grafy. Cykle Eulera i Hamiltona.**
    * **Dlaczego:** Jego ulubiony problem badawczy – *Problem Trasowania Pojazdów (VRP)* – to wariacja Problemu Komiwojażera, który opiera się na cyklach Hamiltona w grafach.
    * **Co musisz wiedzieć:** Czym się różni cykl Eulera (wszystkie krawędzie raz) od Hamiltona (wszystkie wierzchołki raz). Że problem Hamiltona jest trudny obliczeniowo (NP-trudny).
4. **Pytanie 11 (Str. 19): Złożoność obliczeniowa.**
    * **Dlaczego:** Przy szeregowaniu zadań i VRP kluczowe jest to, że dla dużych danych nie da się znaleźć rozwiązania idealnego w skończonym czasie (dlatego używamy heurystyk).

---

#### 2. Dr inż. Marcin Pietranik ("Architekt Systemów / Integrator")

**Analiza profilu:**
Jego tematy to: *„Architektura mikroserwisowa”*, *„Migracja z monolitu”*, *„Grafy wiedzy”*, *„Ciągłe wdrażanie”*.
Pietranik to człowiek od "dużego obrazka". Interesuje go, jak systemy są zbudowane i jak dane wędrują między nimi. Jest praktykiem – nienawidzi teorii, która nie działa w produkcji.

**Strzały w dziesiątkę (Pytania z PDF):**

1. **Pytanie 32 (Str. 50-51): Wzorce architektoniczne (Architektura wielowarstwowa vs SOA/Mikroserwisy).**
    * **Dlaczego:** Jego tematy dyplomowe krzyczą "Mikroserwisy vs Monolit".
    * **Co musisz wiedzieć:** Wady monolitu (skalowalność, wdrażanie całości na raz) vs zalety mikroserwisów (niezależne wdrażanie, skalowanie, ale trudniejsza komunikacja).
2. **Pytanie 24 (Str. 37) i Pytanie 38 (Str. 38): Modele baz danych (Relacyjne vs NoSQL/Grafowe).**
    * **Dlaczego:** Zajmuje się grafami wiedzy. To domena baz grafowych (NoSQL).
    * **Co musisz wiedzieć:** Kiedy użyć SQL (transakcje finansowe, spójność ACID), a kiedy NoSQL/Grafowych (media społecznościowe, rekomendacje, IoT, elastyczny schemat).
3. **Pytanie 13 (Str. 20) i 23 (Str. 34): Integracja i warstwy (OSI / Protokoły).**
    * **Dlaczego:** Prowadzi kurs "Integracja systemów informacyjnych".
    * **Co musisz wiedzieć:** Jak systemy gadają ze sobą? REST, JSON (Pytanie 15), może wspomnieć o kolejkach wiadomości (RabbitMQ - uczy tego na wykładzie).

---

#### 3. Dr inż. Marcin Kawalerowicz ("Pan od Jakości i Weba")

**Analiza profilu:**
Jego tematy to: *„Webowe biblioteki UI (Core Web Vitals)”*, *„CI/CD (Continuous Integration/Deployment)”*, *„Agile/TDD”*, *„Bezpieczeństwo aplikacji webowych”*.
Jest CEO firmy software'owej. Patrzy na programowanie z perspektywy biznesu, jakości kodu i nowoczesnego Weba.

**Strzały w dziesiątkę (Pytania z PDF):**

1. **Pytanie 26 i 27 (Str. 43-44): Cykl życia oprogramowania (Metodyki zwinne Agile vs Kaskadowe).**
    * **Dlaczego:** Jego doktorat dotyczył "Agile Experimentation". To jego konik.
    * **Co musisz wiedzieć:** Dlaczego Waterfall (kaskada) rzadko działa w dzisiejszym biznesie? Dlaczego Scrum/Agile jest lepszy (iteracje, szybki feedback od klienta).
2. **Pytanie 15 (Str. 22): Protokoły warstwy aplikacji (WWW, HTTP).**
    * **Dlaczego:** Zajmuje się "Core Web Vitals" i bibliotekami UI.
    * **Co musisz wiedzieć:** Jak działa HTTP? Co to jest REST? (Może zapytać o różnicę między GET a POST).
3. **Pytanie 33 (Str. 52): Bezpieczeństwo (Ochrona danych, Aplikacje webowe).**
    * **Dlaczego:** Wypisany temat: "Metody oceny bezpieczeństwa aplikacji webowych".
    * **Co musisz wiedzieć:** SQL Injection, XSS (Cross-Site Scripting), dlaczego HTTPS jest ważny.
4. **Pytanie 16 (Str. 23): Techniki efektywnego programowania / Czysty kod.**
    * **Dlaczego:** Zajmuje się jakością w procesach CI/CD.
    * **Co musisz wiedzieć:** Zarządzanie pamięcią, unikanie wycieków, czytelność kodu.

---

#### Plan Bitwy (Jak zdać)

1. **Gdy pyta Myszkowski:** Odpowiadaj **precyzyjnie matematycznie**. Nie mów "algorytm szuka rozwiązania", mów "algorytm iteracyjnie minimalizuje funkcję celu". Skup się na **grafach (9)** i **optymalizacji (30, 31)**.
2. **Gdy pyta Pietranik:** Odpowiadaj **architektonicznie**. Używaj słów kluczy: "skalowalność", "utrzymanie", "mikroserwisy", "bazy grafowe". Pokaż, że wiesz, co jest nowoczesne. Skup się na **bazach danych (24, 38)** i **architekturze (32)**.
3. **Gdy pyta Kawalerowicz:** Odpowiadaj **procesowo i webowo**. Mów o "jakości", "testowaniu", "zadowoleniu klienta (Agile)" i "wydajności strony". Skup się na **metodykach (26, 27)** i **webie (15)**.

To bardzo kompetentna komisja. Nie będą Cię "gnębić" o detale z lat 90., ale bardzo szybko wyczują, czy rozumiesz temat, czy tylko wykułeś regułkę. Powodzenia!

## tools

```sh
pdftk docs/*wlasne.pdf cat 236-244 output tmp.pdf
```
