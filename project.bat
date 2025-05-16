@echo off

REM компилируем програму на сишке и создаем exe файл
gcc k_means_plus_plus.c -o k_means_plus_plus.exe

REM запускаем программу на сишке
k_means_plus_plus.exe

REM python интерпритируемый язык поэтому не создаем .exe, a просто запускаем
python viz.py

REM на всякий перестраховываемся от дабл клика по батнику
pause