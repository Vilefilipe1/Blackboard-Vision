import numpy as np
import os
import tensorflow as tf
import PIL
import PIL.Image
from keras import layers
from tensorflow import keras
import keras
import tensorflow_datasets as tfds
from tensorflow.python.keras.layers import Input, Dense



import pathlib
# data_dir = tf.keras.utils.get_file(,
#                                    fname='quadro-phone',
#                                    untar=True)
# data_dir = tf.keras.utils.image_dataset_from_directory(, class_names=None,
# batch_size=32)
# print(data_dir)
# roses = list(data_dir.glob('*'))
# PIL.Image.open(str(roses[0]))

# batch_size = 32
# img_height = 180
# img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(
  "C:/Users/Vile/Documents/Programas/Programas de Python/Whiteboard-Vision/training-data/whiteboard",
  validation_split=0.2,
  subset="training",
  seed=123,
  batch_size=32)

val_ds = tf.keras.utils.image_dataset_from_directory(
  "C:/Users/Vile/Documents/Programas/Programas de Python/Whiteboard-Vision/training-data/whiteboard",
  validation_split=0.2,
  subset="training",
  seed=123,
  batch_size=32)


class_names = train_ds.class_names
print(class_names)
normalization_layer = layers.Rescaling(1./255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))

img_height = 1250
img_width = 1250

num_classes = len(class_names)

model = keras.Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

epochs=10
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)




