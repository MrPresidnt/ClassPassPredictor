import pandas as pd

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
new = input("Enter name for modified data file> ")


