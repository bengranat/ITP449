"""
Benjamin Granat
ITP 449
Assginment 11
Performs a KNN Classification on the diabetes.csv based on three
most statistically correlated numeric attributes.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import make_pipeline as mp
from sklearn.metrics import ConfusionMatrixDisplay as cms

#Function: remove_outliers
#Parameters: dataframe, columns
#Creates lower and upper quartile bounds for columns in dataframe.
#Drops values outside of the lower and upper bounds in the dataframe
#Returns updated dataframe
def remove_outliers(data, columns):
    for column in columns:
        Q3 = data[column].quantile(0.75)
        Q1 = data[column].quantile(0.25)
        IQR = Q3 - Q1
        lower = Q1 - 1.5*IQR
        upper = Q3 + 1.5*IQR
        df_filter = (data[column] >= lower)&(data[column] <= upper)
        data = data[df_filter]
    return data

def main():
    #Reading file into dataframe
    df = pd.read_csv('diabetes.csv')
    #Sorting columns most correlated with 'Outcome' column in descending order
    corr = df.corr()['Outcome'].sort_values(ascending=False)
    columns = corr[1:6].index.tolist()
    X = df[columns]
    y = df['Outcome']
    #Removing outliers
    X = remove_outliers(X, columns)
    y = y[X.index]
    #Scaling data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    #Splitting data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    #Initializing k values
    n_neighbors = list(range(1, 34, 2))
    #Initializing empty list to store accuracy scores
    accuracy_scores = []
    for k in n_neighbors:
        knn = KNeighborsClassifier(n_neighbors=k)
        #Cross-validation
        scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
        #Appending mean accuracy score for k to the list
        accuracy_scores.append(scores.mean())
    fig, axs = plt.subplots(1, 2)
    #Plotting accuracy scores against k values
    axs[0].plot(n_neighbors, accuracy_scores)
    #Sets labels
    axs[0].set(xlabel='Number of Neighbors', ylabel='Accuracy')
    #Iniializes best k
    best_k = n_neighbors[accuracy_scores.index(max(accuracy_scores))]
    # Sets title
    axs[0].set_title("Average score vs. K\nBest k = " + str(best_k))
    # Creates optimized model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    # Runs k neighbors classifier
    knn = KNeighborsClassifier(n_neighbors=best_k)
    # Creates pipelines and predictor variables
    pipeline = mp(StandardScaler(), knn)
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    # Creates confusion matrix with y_test and predicted y
    conf_matrix = confusion_matrix(y_test, y_pred)
    # Displays confusion matrix
    cm_disp = cms(confusion_matrix = conf_matrix)
    cm_disp.plot(ax = axs[1])
    plt.savefig("Diabetes Classification")



if __name__ == '__main__':
    main()