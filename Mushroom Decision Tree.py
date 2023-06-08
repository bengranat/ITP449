import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split

def main():
    #Reading mushrooms dataset
    #Dropping null and duplicate values
    df = pd.read_csv('mushrooms.csv')
    df = df.dropna()
    df = df.drop_duplicates()

    #Assigning feature vectors and output
    #Converts X into numerical features
    X = df.drop('class', axis=1)
    y = df['class']
    X = pd.get_dummies(X)

    #Train and testing split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Decision Tree
    #Hyperparameters
    #Uses randomized search cv to find best hyperparameters
    model_dt = DecisionTreeClassifier()
    hyperparam_dict = {
    'criterion': ['entropy', 'gini'],
    'max_depth': range(2, int(round(np.sqrt(X_train.shape[0]))) + 1),
    'min_samples_split': range(2, 11),
    'min_samples_leaf': range(2, 11)
    }
    rscv = RandomizedSearchCV(estimator=model_dt, param_distributions=hyperparam_dict)
    rscv.fit(X_train, y_train)
    best_params = rscv.best_params_

    #Model fit with best parameters
    model_dt = DecisionTreeClassifier(criterion=best_params['criterion'], max_depth=best_params['max_depth'],
        min_samples_split=best_params['min_samples_split'],
        min_samples_leaf=best_params['min_samples_leaf'])
    model_dt.fit(X_train, y_train)

    #Data requiring classification
    #Predicted output calculation for confusion matrix
    sample_data = pd.DataFrame({
    "cap-shape": ["x"],
    "cap-surface": ["s"],
    "cap-color": ["n"],
    "bruises": ["t"],
    "odor": ["y"],
    "gill-attachment": ["f"],
    "gill-spacing": ["c"],
    "gill-size": ["n"],
    "gill-color": ["k"],
    "stalk-shape": ["e"],
    "stalk-root": ["e"],
    "stalk-surface-above-ring": ["s"],
    "stalk-surface-below-ring": ["s"],
    "stalk-color-above-ring": ["w"],
    "stalk-color-below-ring": ["w"],
    "veil-type": ["p"],
    "veil-color": ["w"],
    "ring-number": ["o"],
    "ring-type": ["p"],
    "spore-print-color": ["r"],
    "population": ["s"],
    "habitat": ["u"]
    })
    new_data_dummies = pd.get_dummies(sample_data).reindex(columns=X.columns, fill_value=0)
    prediction = model_dt.predict(new_data_dummies)
    print("Prediction of sample mushroom:", prediction[0])
    y_pred = model_dt.predict(X_test)

    #Figure creation for plots
    fig, ax = plt.subplots(1, 2, figsize=(20, 9))

    #Confusion matrix plot
    conf_matrix = confusion_matrix(y_test, y_pred)
    cm_disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
    cm_disp.plot(ax=ax[0])
    ax[0].set(title='Confusion Matrix')

    #Decision tree plot
    plot_tree(model_dt, ax=ax[1], feature_names=X.columns, class_names=y.unique(), filled=True)
    ax[1].set(title='Decision Tree')
    fig.suptitle('Inedible Mushrooms Decision Tree Results')
    fig.tight_layout()
    plt.show()
    plt.savefig("FP_DT_Granat.png")

if __name__ == '__main__':
    main()