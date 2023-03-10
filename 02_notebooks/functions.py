
import pandas as pd

def split_columns(data):
    '''function to break proteins into 20-characters-length sequences'''

    df1 = pd.DataFrame()
    for index in range(0,len(data['seq'])):
        df2 = pd.DataFrame()
        for n in range(2,len(data['seq'][index])-2):
            parts = [ data['seq'][index][n-2], data['seq'][index][n-1], data['seq'][index][n],
                     data['seq'][index][n+1], data['seq'][index][n+2], data['sst3'][index][n], data['sst8'][index][n]]
            df1 = pd.concat([df1, pd.DataFrame(parts).T], axis=0)
        df2 = pd.concat([df2, df1], axis=0)

    df1 = pd.concat([df1,df2], axis=0)

    df1.columns = ['AA-2','AA-1','AA','AA+1','AA+2','y3','y8']
                
    return df1

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from sklearn.metrics import cohen_kappa_score

def search_model(names, classifiers, x_train, y_train, x_test, y_test)

    # iterate over classifiers
for name, clf in zip(names, classifiers):
    clf.fit(x_train, y_train.values.ravel())
    score = clf.score(x_test, y_test)
    kappa = cohen_kappa_score(y_test, clf.predict(x_test))
    
    return name, score, kappa

import matplotlib.pyplot as plt

def plot_loss_accuracy(history):
    historydf = pd.DataFrame(history.history, index=history.epoch)
    plt.figure(figsize=(8, 6))
    historydf.plot(ylim=(0, max(1, historydf.values.max())))
    loss = history.history['loss'][-1]
    acc = history.history['accuracy'][-1] #'acc'
    plt.title('Loss: %.3f, Accuracy: %.3f' % (loss, acc))

from sklearn.metrics import cohen_kappa_score, classification_report 

def model_performance_class(y_train, y_pred_train, y_test, y_pred_test):

    print("Results obtained for the TRAIN SET")
    print("==================================")
    print("The Cohen's Kappa is: {:.2f}".format(cohen_kappa_score(y_train, y_pred_train)))
    print(classification_report(y_train, y_pred_train))
    print("==================================")
    print("Results obtained for the TEST SET")
    print("The Cohen's Kappa is: {:.2f}".format(cohen_kappa_score(y_test, y_pred_test)))
    print(classification_report(y_test, y_pred_test))
