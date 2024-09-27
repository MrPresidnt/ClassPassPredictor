import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib as mpl
import pandas as pd
from sklearn.model_selection import train_test_split

data  = pd.read_csv("editedData.csv")

x = data.drop(columns='Passed the class')
y = data["Passed the class"]

#print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# print("Training data shape:", x_train.shape)
# print("Training labels shape:", y_train.shape)
# print("Test data shape:", x_test.shape)
# print("Test labels shape:", y_test.shape)

model = keras.Sequential()
model.add(keras.layers.Dense(64, activation='relu', input_shape=(9,)))
model.add(keras.layers.Dense(32, activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

optimizer = keras.optimizers.Adam(learning_rate = 0.0006)

model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

fitmodel = model.fit(x_train, y_train, epochs = 40, verbose = 1, validation_data=(x_test, y_test), batch_size=128)

test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f'Test loss: {test_loss}')
print(f'Test accuracy: {test_accuracy}')

print(model.summary())

model.save('passPredictor.keras')