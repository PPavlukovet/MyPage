
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
    df = pd. read_csv (file_name, header = 0, sep = ';')    
    cnt_columns = df. shape[1]
    cnt_rows = df. shape[0]
    Label_03 [ 'text'] = cnt_rows
    Label_05 [ 'text'] = cnt_columns
    return df
#Выборка столбца в список
def get_column(df, column_ix):
     cnt_rows = df.shape[0]
     lst = [ ]
     for i in range (cnt_rows):
           lst. append ( df. iat [ i, column_ix] )
     return lst  

# Поиск функции- есть ли имя в столбце
def meet_name (field):
     checkfor=[ 'Вера','Анатолий','Мария', 'Артем', 'Алексей', 'Валерия', 'Наталья','Оксана','Галина','Марина','Вероника','Виталий','Борис','Диана','Ева']
     for s in checkfor:
         if s in str (field):  # Нашлось!
               return True
#Ничего не совпало
     return False          
# Усли в этом списке многие элементы содержат имя, пусть вернет True
def list_meet_name(fields_list):
    counter_total=0
    counter_meet=0
    for list_item in fields_list:
        counter_total+=1
  
        if meet_name (list_item):
             counter_meet +=1
    #Конец подсчета
    ratio= counter_meet / counter_total 
    if ratio >  0.1:
          return True, ratio
    # Не набралось нужного количества совпадений
    return False, ratio
    
 # Пройти все столбы              
def check_all_colamns(df):
    colamns_cnt=df.shape[1]
    for i in range( colamns_cnt): #От 0 до colamns_cnt-1
         lst=get_column(df,i)
         result = list_meet_name (lst)
         if result [ 0 ]:             
              output_text. insert ( tk. END, "В столбце"+ str(i+1)+"предположительно содержится имя."+os. linesep)
              output_text. insert ( tk. END, "Процент совпадений"+"{:.2f}".format(result[1]*100)+" %."+os. linesep)
         else:
               output_text. insert ( tk. END, "Предложений для столбца"+ str(i+1)+"не найдено."+os. linesep)   
# Обработчик нажатия кнопки 
def process_button ( ) :
    file_name = do_dialog( )
    Label_01 [ 'text' ] = file_name
    df = pandas_read_csv ( file_name)
    check_all_colamns(df) 
    mb. showinfo (title=None, message="Готово")

# Сoздание кнопки
button= tk. Button ( window, text = "Прочитать файл", command= process_button)
button . grid (column=1, row=4)

#Запуск цикла mainloop
window. mainloop ( )

