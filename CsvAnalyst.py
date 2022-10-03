# Программа анализа .csv  фйлов
import tkinter as tk

#Создание главного окна
window=tk . Tk ( )
window. geometry ( "550x550" )
window. title ( "Программа анализа .csv  фйлов" )

#создание меток ввода
Label_00 = tk.Label (text = "Файл:")
Label_00 . grid (column=0, row=0, padx=10, pady=10, sticky=" e ")

Label_01 = tk.Label (text = " ")
Label_01 . grid (column=1, row=0, sticky=" w ")

Label_02 = tk.Label (text = "Строк:")
Label_02. grid (column=0, row=1, padx=10, pady=10, sticky=" e ")

Label_03 = tk.Label (text = " ")
Label_03 . grid (column=1, row=1, sticky=" w ")

Label_04 = tk.Label (text = " Столбцов:")
Label_04 . grid (column=0, row=2, padx=10, pady=10, sticky=" e ")

Label_05 = tk.Label (text = " ")
Label_05 . grid (column=1, row=2, padx=10, sticky=" w ")

#Запуск цикла mainloop
window. mainloop ( )

