Paralelní zpracování CSV souborů a generování reportu
=====================================================

Popis projektu
--------------
Tato aplikace slouží k paralelnímu zpracování CSV souborů uložených ve složce
`data/input`. Program využívá více vláken (worker pool), ve kterých jsou CSV
soubory zpracovávány souběžně. Pro každý soubor je určen počet jeho řádků
a thread-safe agregátor ukládá výsledné statistiky.

Po dokončení zpracování je vygenerován výstupní report ve formátu HTML,
který shrnuje:
- celkový počet zpracovaných CSV souborů,
- celkový součet řádků,
- případné chyby vzniklé během zpracování.

Logování probíhá do souboru `logs/app.log`.

Struktura projektu
------------------
paralelni-reporty/
  src/
    main.py
    config.py
    loader/
    parser/
    aggregation/
    core/
    export/
  data/
    input/    - vstupní CSV soubory
    output/   - generované reporty
  logs/
  test/
  doc/

Instalace a spuštění
--------------------
1. Nainstalujte Python 3.10 nebo novější.
2. Ujistěte se, že složka `data/input` obsahuje alespoň jeden CSV soubor.
3. Spusťte aplikaci příkazem:

   python src/main.py

Konfigurace
-----------
V souboru `src/config.py` lze upravit:
- INPUT_DIR: cesta ke vstupní složce se CSV soubory
- OUTPUT_DIR: cesta k výstupní složce pro generované reporty
- LOG_DIR: umístění logů
- NUM_WORKERS: počet paralelních vláken (workerů)

Výstupy aplikace
----------------
- data/output/report.html  
  Obsahuje shrnutí zpracovaných souborů.
- logs/app.log  
  Obsahuje informace o průběhu běhu aplikace.

Testování
---------
Testy se nacházejí ve složce `test/` a používají knihovnu `unittest`. Obsahují:
- test parseru CSV
- test agregátoru
- test worker poolu

Licence
-------
Tento projekt je určen jako školní práce a slouží pro výukové účely.
