"""
Benjamin Granat
ITP 449
Assginment 9
Trains and tests a logistic regression based on diabetes classification data
Produces confusion matrix visualization
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix as cmatrix
from sklearn.metrics import accuracy_score as accscore
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import ConfusionMatrixDisplay as cms


# Function: remove_outliers
# Parameters: dataframe, columns
# Creates lower and upper quartile bounds for columns in dataframe.
# Drops values outside of the lower and upper bounds in the dataframe
# Returns updated dataframe
def remove_outliers(data, columns):
    for column in columns:
        Q3 = data[column].quantile(0.75)
        Q1 = data[column].quantile(0.25)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df_filter = (data[column] >= lower) & (data[column] <= upper)
        data = data[df_filter]
    return data


def main():
    # Reading file into dataframe
    df = pd.read_csv('diabetes.csv')
    # Sorting columns most correlated with 'Outcome' column in descending order
    corr = df.corr()['Outcome'].abs().sort_values(ascending=False)
    # Isolates most correlated attributes
    corr_attrs = corr[1:4].index
    # Outcome column
    outcome = corr[0:1].index
    # Drop duplicates and null values
    df.drop_duplicates()
    df.dropna()
    # Removes outliers from dataframe using correlated columns and outcome column
    remove_outliers(df, corr_attrs)
    remove_outliers(df, outcome)
    # Creates feature vector and target vector
    X = df[corr_attrs].values
    Y = df[outcome].values
    # Partitions data into training and testing subsets
    X_train, X_test, Y_train, Y_test = tts(X, Y, random_state=42)
    # Runs logistic regression
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    predict_Y = model.predict(X_test)
    # Creates confusion matrix based on predictions
    matrix = cmatrix(Y_test, predict_Y)
    # Calculates accuracy score and concatinates into a string
    accuracy = accscore(Y_test, predict_Y)
    accuracy_string = "Accuracy is " + str(accuracy)
    # Displaying the confusion matrix
    cm_disp = cms(confusion_matrix=matrix, display_labels=model.classes_)
    fig, axes = plt.subplots()
    cm_disp.plot(ax=axes)
    axes.set(title="Diabetes Logistic Regression Confusion Matrix" + "\n" + accuracy_string)
    plt.savefig('Diabetes Logistic Regression Confusion Matrix.png')


if __name__ == '__main__':
    main()