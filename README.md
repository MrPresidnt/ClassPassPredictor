Data Formate:
[Test 1 score][Test 2 score][Test 3 score][Test 4 score][hours_studied_per_week][attendence_percent][classes_missed][office_hours_attended][StudyHours_Attendence_interaction][Passed the class]

Trained on 20,000 data points
Wrote the inital neural network and accompanying scripts
-> dataReformater.py takes in the inital data set generated with chatGPT, and changes the "Passed the class" column from Yes/No to 1/0.
   It also divides all the other columns by 100 to normalize the data.
   Also added another metric called Study/Attendence interaction which is the value of hours_studied_per_week times attendence_percent to make the data set more corelated with itself

-> main.py is where the network is built and trained. 80% of the data set is training and 20% test right now. The trained network is saved to a file at the end of the program.
   Its currently 4 lays of 64,32,16, and 1 neuron respectivley. 1 neuron in the output layer because we just need a 0 or a 1. This is also why that layer's activation function is sigmoid, as it helps push the output towards 0 or 1.
   learning rate of 0.0006 up from standard 0.0001, 40 epochs, 128 sample size (mostly for speed)

-> userInteraction.py loads the saved network then a class called predictPass is called. predictPass takes the 8 data points from the user, calcualtes the study/attendence corelation and adds its to the array with the inputs,
   then all the numbers are divided by 100 and passed to the network to make a prediction. 
   Following, if the prediction is >= 0.5 the studnet will pass and vice versa.

Current Bugs:
-> Model is biased with the office hours value. An input of [20,20,20,20,10,90,3,20] with get a 0.96 while an input of [20,20,20,20,10,90,3,10] will get a 0.0266.
   I believe this may have something to do with the [StudyHours_Attendence_interaction] value. 

-> When the model is very sure it will spit out something like a 0.96 for example with is easy to translate to 96% certain. However, when its closer to 0, meaning 
   it believes a fail is in order, it will spit out something like 0.02 but then this gets printed out as 2% certain which is obviously not the case. Need to
   implement some way of handeling this to get a correct percent value on the fail predictions.

To-do:
-> Fix office hours bias
-> Print correct percent certainty on Fail evaluations
-> Tune model paramters
