# Программа анализа .csv  фйлов
import tkinter as tk
from tkinter .scrolledtext import ScrolledText as st
from tkinter import  messagebox as mb
from tkinter import  filedialog as fd
import os
import pandas as pd

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

# Создание текстового вывода с прокруткой
output_text = st (height = 22 , width = 50)
output_text . grid (column=1, row=3, padx=5, pady=10, sticky=" w ")

#Диалог открытия файла
def do_dialog( ):
    my_dir = os. getcwd ( )
    name = fd. askopenfilename (initialdir = my_dir )
    return name
 
 #Обработка csv файла при помощи pandas
def pandas_read_csv ( file_name):
    df = pd. read_csv (file_name, header = None, sep = ';')    
    cnt_columns = df. shape[1]
    cnt_rows = df. shape[0]
    Label_03 [ 'text'] = cnt_rows
    Label_05 [ 'text'] = cnt_columns
    return df
    
# Обработчик нажатия кнопки 
def process_button ( ) :
       file_name = do_dialog( )
       Label_01 [ 'text' ] = file_name
       pandas_read_csv ( file_name) 
       mb. showinfo (title=None, message="Готово")

# Сoздание кнопки
button= tk. Button ( window, text = "Прочитать файл", command= process_button)
button . grid (column=1, row=4)

#Запуск цикла mainloop
window. mainloop ( )

