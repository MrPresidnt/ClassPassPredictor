import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib as mpl
import pandas as pd

model = keras.models.load_model('passPredictor.keras')
#print(model.summary())
features = ['Test 1 Score: ', 'Test 2 Score: ', 'Test 3 Score: ', 'Test 4 Score: ', 'Hours Studied Per Week: ', 'Attendence Percent: ', 'Classes Missed: ', 'Hours of Office Hours Attended: ']

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

predictPass()