import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def dataReformater(baseDataFile, newDataFile):
    data = pd.read_csv(baseDataFile)

    for index, row in data.iterrows():
        if row["Passed the class"] == "Yes":
            data.loc[index, "Passed the class"] = 1
        else:
            data.loc[index, "Passed the class"] = 0

    for col in data.columns[:8]:
        data[col] = data[col].astype(float) / 100

    #print(data.loc[:,"Passed the class"])
    data['Study_attendence_interaction'] = data['hours_studied_per_week'] * data['attendance_percent']

    columns = data.columns.tolist()

    columns.insert(8, columns.pop(columns.index('Study_attendence_interaction')))
    data = data[columns]

    data.to_csv(newDataFile, index=False)

original = input("Enter the name of the original data file> ")
newFile = input("Enter name for modified data file> ")

dataReformater(original, newFile)

data = pd.read_csv(newFile)

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

model = keras.models.load_model('passPredictor.keras')
#print(model.summary())

def predictPass():
    print('Please enter the values for the following 8 questions: ')

    userInput = []

    for i in range(8):
        val = float(input(f"{features[i]}"))
        userInput.append(val/100)

    
    study_attendence_interaction = userInput[4]*userInput[5]
    userInput.append(study_attendence_interaction)
    
    userInput = np.array(userInput).reshape(1, 9)

    prediction = model.predict(userInput)

    passOrFail = 'Pass' if prediction[0][0] >= 0.5 else 'Fail'
    print(f'Prediction: You will {passOrFail} with a {prediction[0][0]*100:.2f}% certainty')


while True:
    features = ['Test 1 Score: ', 'Test 2 Score: ', 'Test 3 Score: ', 'Test 4 Score: ', 'Hours Studied Per Week: ', 'Attendence Percent: ', 'Classes Missed: ', 'Hours of Office Hours Attended: ']

    predictPass()