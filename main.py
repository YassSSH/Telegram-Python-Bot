from telegram.ext import *
from io import BytesIO
import cv2
import numpy as np
import tensorflow as tf

with open('token', 'r') as f:
    TOKEN = f.read()


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255, x_test / 255


class_names = ['Avion', 'Voiture', 'Oiseau', 'Chat', 'Cheval', 'Chien', 'Grenouille', 'Biche', 'Chevre', 'Camion']

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.Dense(10, activation='softmax'))


def start(update, context):
    update.message.reply_text("Bienvenue !")


def help(update, context):
    update.message.reply_text("""
    /start - Allumer le Bot
    /help - Afficher ce message
    /train - Se co au réseau
    """)


def train(update, context):
    update.message.reply_text("")
    pass


def handle_message(update, context):
    update.message.reply_text("Train le model et send la photo")


def handle_photo(update, context):
    pass


updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler("train", train))
dp.add_handler(MessageHandler(Filters.photo, handle_photo))

updater.start_polling()
updater.idle()
