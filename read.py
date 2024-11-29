import numpy as np
import os
import tensorflow as tf
# from tensorflow import keras
import glob
import shutil
from datetime import datetime
import configparser
import json

img_height = 180
img_width = 180
class_names = ['etc', 'whiteboard']
array_files_scanned = []
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


config = configparser.ConfigParser()
try:
    os.mkdir("./user-settings")
    print("Not found user settings, creating a new one...")
    os.system('cls')
    print("Example: D:/Arquivos e Programas/Celular/Gallery/Camera")
    directory_user_camera = input("What directory of images to use? (Folder to filter out): ")
    os.system('cls')
    print("Example: D:/Arquivos e Programas/Celular/Pictures/Gallery/owner/Quadro")
    directory_user_whiteboard = input("What directory to place images filtered? (Folder organized): ")
    is_cloud = input("Want cloud backup?? : (y, [N]) ")
    if ((is_cloud == "y") or (is_cloud == "yes") or (is_cloud == "Yes") or (is_cloud == "YES")):
        directory_user_whiteboardCloud = input("What directory to place copyed backup?: ")
        config['User'] = {'directory_user_camera': directory_user_camera, 'directory_user_whiteboard': directory_user_whiteboard, 'directory_user_whiteboardCloud': directory_user_whiteboardCloud}
    else:
        is_cloud == False
        config['User'] = {'directory_user_camera': directory_user_camera, 'directory_user_whiteboard': directory_user_whiteboard}
    config["Files"] = {"files_scaned": []}
    with open('./user-settings/config.ini', 'w') as configfile:
         config.write(configfile)

except FileExistsError:
    print("Loading user settings")
    config.read('./user-settings/config.ini')
    directory_user_camera = config["User"]["directory_user_camera"]
    directory_user_whiteboard = config["User"]["directory_user_whiteboard"]
    try:
        directory_user_whiteboardCloud = config["User"]["directory_user_whiteboardCloud"]
    except KeyError:
        is_cloud = False
        directory_user_whiteboardCloud = False

    array_files_scanned = json.loads(config.get("Files","files_scaned"))


def classSchedule(a):
    a = a.removeprefix(directory_user_camera + "\\IMG_")
    horario = a[(a.find("_") + 1):(a.find(".jpg") - 2)]
    a = a.replace(a[a.find("_"):(a.find(".jpg") + 4)], "")
    given_date = datetime(int(a[0:4]), int(a[4:6]), int(a[6:8]))
    day_of_week = given_date.isoweekday() % 7 
    print(day_of_week)
    hour = int(horario[0:2])
    min = int(horario[2:4])
    if (day_of_week == 1) or (day_of_week == 3):
        # Segunda ou Quarta
        if (hour < 15) or ((hour == 15) and (min <= 10)):
            return "PI"  
        if (hour <= 17):
            return "LP"           
        else:
            return "C-B"
    if (day_of_week == 2) or (day_of_week == 4):
        # Terça ou Quinta
        if (hour < 15) or (hour == 15) and (min <= 10):
            return "F-1"            
        else:
            return "AL-1"

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
    list = glob.glob(directory_user_camera + "\*.jpg")
    for n in list:
        try:
            if (array_files_scanned.index(n) != 0):
                continue
        except ValueError:
            array_files_scanned.append(n)
            image_type = load_img(n)
            if image_type == 'whiteboard':
                classType = classSchedule(n)
                print(classType)
                name = n.replace(directory_user_camera, "")
                # if (is_cloud != False):
                #     shutil.copy(n, "C:/Users/Vile/OneDrive/Documentos/Faculdade" + "/" + classType + "/Quadro" + name)
                print(n)
                print(directory_user_whiteboard + "\\" + classType + name)
                try:
                    shutil.move(n, directory_user_whiteboard + "\\" + classType + name)
                except FileNotFoundError:
                    os.mkdir(directory_user_whiteboard + "\\" + classType)
                    shutil.move(n, directory_user_whiteboard + "\\" + classType + name)
    config["Files"] = {"files_scaned": array_files_scanned}
    config["Files"] = {"files_scaned": config["Files"]["files_scaned"].replace("'", '"')}
    with open('./user-settings/config.ini', 'w') as configfile:
        config.write(configfile)

# Recreate the exact same model, including its weights and the optimizer
model = tf.keras.models.load_model("./training/my_model_11-47_29-11.keras") 

load_directory()








