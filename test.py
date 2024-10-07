from datetime import datetime


a = "D:/Arquivos e Programas/Celular/Gallery/Camera\IMG_20240812_141112.jpg"
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
        print("C-A")  
    elif (hora == 15) and (minutos <= 10):
        print("C-A")           
    else:
        print("PF")
elif (day_of_week == 2) or (day_of_week == 4):
    # Terça ou Quinta
    if (hora < 15):
        print("FEM")  
    elif (hora == 15) and (minutos <= 10):
        print("FEM")           
    else:
        print("GA")
else:
    print("Seminários")