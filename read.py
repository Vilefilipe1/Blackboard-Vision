import numpy as np
import os
import tensorflow as tf
# from tensorflow import keras
import glob
import shutil
from datetime import datetime


img_height = 180
img_width = 180
class_names = ['outros', 'quadros']
lista_lida = []
directory = "D:/Arquivos e Programas/Celular/Gallery/Camera"
directory_organiz = "D:/Arquivos e Programas/Celular/Pictures/Gallery/owner/Quadro"

try :
    with open("C:/Users/Vile/Documents/Programas/Programas de Python/Whiteboard-Vision/lista_lida.txt", "r") as f:
        for line in f:
            lista_lida.append(line.strip())
except FileNotFoundError:
    print()

print(lista_lida)
# p = 'D:/Arquivos e Programas/Celular/Gallery/Camera\20230914_073530.jpg'
# print(lista_lida.index(p))



# Recreate the exact same model, including its weights and the optimizer
model = tf.keras.models.load_model("C:/Users/Vile/Documents/Programas/Programas de Python/Whiteboard-Vision/training/my_model.keras") 

def materiaCronograma(a):
    # a = "D:/Arquivos e Programas/Celular/Gallery/Camera\IMG_20240812_141112.jpg"
    a = a.removeprefix("D:/Arquivos e Programas/Celular/Gallery/Camera\\")
    a = a.removeprefix("IMG_")
    horario = a[(a.find("_") + 1):(a.find(".jpg") - 2)]
    a = a.replace(a[a.find("_"):(a.find(".jpg") + 4)], "")
    given_date = datetime(int(a[0:4]), int(a[4:6]), int(a[6:8]))
    day_of_week = given_date.isoweekday() % 7 
    print(day_of_week)
    hora = int(horario[0:2])
    minutos = int(horario[2:4])
    if (day_of_week == 1) or (day_of_week == 3):
        # Segunda ou Quarta
        if (hora < 15):
            return "C-A"  
        if (hora == 15) and (minutos <= 10):
            return "C-A"           
        else:
            return "PF"
    if (day_of_week == 2) or (day_of_week == 4):
        # Terça ou Quinta
        if (hora < 15):
            return "FM"  
        if (hora == 15) and (minutos <= 10):
            return "FM"           
        else:
            return "GA"
    else:
        return "SM"





def load_img (img):
    img = tf.keras.utils.load_img(
    img, target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print(class_names[np.argmax(score)], 100 * np.max(score))
    return class_names[np.argmax(score)]

def load_directory ():
    lista = glob.glob(directory + "\*.jpg")
    for n in lista:
        try:
            if (lista_lida.index(n) != 0):
                continue
        except ValueError:
            lista_lida.append(n)
            with open("C:/Users/Vile/Documents/Programas/Programas de Python/Whiteboard-Vision/lista_lida.txt", "a") as f:
                f.write(n + "\n")
            print(n)
            tipo_imagem = load_img(n)
            if tipo_imagem == 'quadros':
                materia = materiaCronograma(n)
                print(materia)
                nome = n.replace("D:/Arquivos e Programas/Celular/Gallery/Camera", "")
                # print(n)
                # print(directory_organiz)
                # print(nome)
                shutil.copy(n, "C:/Users/Vile/OneDrive/Documentos/Faculdade" + "/" + materia + "/Quadro" + nome)
                shutil.move(n, directory_organiz + "/" + materia + nome)

            



    # for n in lista:
    #     try:
    #         # print(lista_lida.index(n))
    #         if (lista_lida.index(n) != ValueError):
    #             continue
    #     except ValueError:
    #         print(n)
    #         lista_lida.append(n)
    #         with open("lista_lida.txt", "a") as f:
    #             f.write(n + "\n")
    #         tipo_imagem = load_img(n)
    #         if tipo_imagem == 'quadros':
    #             nome = n.replace("D:/Arquivos e Programas/Celular/Gallery/Camera\\", "")
    #             shutil.move(n, directory_organiz + "/" + nome) 



load_directory()








