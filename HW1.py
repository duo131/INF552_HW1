import csv

import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.svm import SVC


def ReplaceFunction(v):
    if 'L' == v:
        v = 1
    if 'R' == v:
        v = 2
    if 'B' == v:
        v = 3
    return v

def RelistData(k):
    csvfile = open(k, newline='')
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='\n')
    data = list(csvreader)
    m = data[0]
    data.remove(m)
    return data

def RunPredict(k):

    listA = []
    listB = []
    line = 0

    for i in range (1,7):
        if i!=k:
            dataString = 'playerD'+str(i)+'.csv'
            data_train = RelistData(dataString)
            for line in range(len(data_train)):
                height = int(data_train[line][9])
                weight = int(data_train[line][8])

                bmi = 100*(weight)/(height*height)

                listA.append([bmi,weight,height,ReplaceFunction(data_train[line][10]),ReplaceFunction(data_train[line][11]),data_train[line][14]])
                listB.append(data_train[line][20])
                line += 1


    #print (len(listA))
    X = np.array(listA)
    Y = np.array(listB)
# fit a SVM model to the data

    model = SVC()
    model.fit(X, Y)
    print(model)
    # make predictions
    expected = Y
    dataString = 'playerD' + str(k) + '.csv'
    data_test = RelistData(dataString)
    list_test = []
    list_ans = []
    line_test = 0
    for line_test in range(len(data_test)):
        height = int(data_test[line_test][9])
        weight = int(data_test[line_test][8])
        bmi =  100*(weight)/(height*height)

        list_test.append([bmi,weight, height, ReplaceFunction(data_test[line_test][10]),ReplaceFunction(data_test[line_test][11]), data_test[line_test][14]])
        list_ans.append(data_test[line_test][20])
        line_test += 1

    predicted = model.predict(list_test)
    """""
      print(len(list_ans))
      print(len(predicted))
      print(predicted)
    """""
    corectAns = 0
    check_no = 0
    for check_no in range(len(list_ans)):
        if list_ans[check_no] == predicted[check_no]:
            corectAns+=1
    #print(corectAns)
    print(100*corectAns/len(list_ans))


for k in range (1,7) :
    print(k)
    RunPredict(k)
