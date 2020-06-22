import os
import signal
import zipfile
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from model import keras_model

local_zip = './TradeLicenseAbuDhabi.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

base_dir = '/tmp/data'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# Directory with our training license images
train_dir = os.path.join(train_dir, 'license')

# categories of license
category_names = ['LicenseAbuDhabiNo', 'Ajman', 'Dibba', 'Dubai', 'Fujairah', 'RAK', 'Sharjah', 'Umm']

def pre_processor():

def train_generator():

# the three color channels: R, G, and B
# yet to decide input shape
# img_input = layers.Input(shape=(150, 150, 3))

model = keras_model()

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['acc'])

# All images will be rescaled by 1./255
train_datagen = ImageDataGenerator(rescale=1. / 255)
val_datagen = ImageDataGenerator(rescale=1. / 255)

# Flow training images in batches of 20 using train_datagen generator
train_generator = train_datagen.flow_from_directory(
    train_dir,  # This is the source directory for training images
    target_size=(150, 150),  # All images will be resized to 150x150
    batch_size=20,
    # Since we use binary_crossentropy loss, we need binary labels
    class_mode='binary')

# Flow validation images in batches of 20 using val_datagen generator
validation_generator = val_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')

history = model.fit_generator(
    train_generator,
    steps_per_epoch=100,  # 2000 images = batch_size * steps
    epochs=15,
    validation_data=validation_generator,
    validation_steps=50,  # 1000 images = batch_size * steps
    verbose=2)



        # Retrieve a list of accuracy results on training and validation data
        # sets for each training epoch
        acc = history.history['acc']
        val_acc = history.history['val_acc']

        # Retrieve a list of list results on training and validation data
        # sets for each training epoch
        loss = history.history['loss']
        val_loss = history.history['val_loss']

        # Get number of epochs
        epochs = range(len(acc))

        # Plot training and validation accuracy per epoch
        plt.plot(epochs, acc)
        plt.plot(epochs, val_acc)
        plt.title('Training and validation accuracy')

        plt.figure()

        # Plot training and validation loss per epoch
        plt.plot(epochs, loss)
        plt.plot(epochs, val_loss)
        plt.title('Training and validation loss')

        os.kill(os.getpid(), signal.SIGKILL)
