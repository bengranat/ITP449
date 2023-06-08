""" Ben Granat
    ITP-449
    SVM Classification Model
    Performs SVM Classification using cross validation on winequality dataset
    Creates confusion matrix and lineplot of accuracy score visualizations
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler


def main():
    # Reads in dataset (skips first row)
    # Drops null and duplicate values
    df = pd.read_csv('winequality-white.csv', skiprows=1, sep=';')
    df = df.drop_duplicates()
    df = df.dropna()

    # RobustScaler transformation
    scaler = RobustScaler()
    df_scaled = scaler.fit_transform(df)
    df = pd.DataFrame(df_scaled, columns=df.columns)

    # Z score normalization
    z_scores = (df - df.mean()) / df.std()
    df = df[(z_scores.abs() < 3).all(axis=1)]

    # Correlation matrix
    # Finding four most correlated columns with "quality"
    corr_matrix = df.corr()
    corr_list = corr_matrix["quality"].sort_values(ascending=False).keys()
    four_corrs = corr_list[0:4]

    # Creating feature vector and output
    df_updated = df[four_corrs]
    y = df_updated['quality']
    X = df_updated.drop(columns='quality')

    # Standardizaton process using StandardScaler
    tfr_standard = StandardScaler()
    X_t = tfr_standard.fit_transform(X)
    X = pd.DataFrame(X_t, columns=X.columns)

    # Training and testing split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=42, stratify=y)
    # Dictionary of hyperparameters
    param_dict_svc = {
        'kernel': ['rbf', 'linear'],
        'C': [0.1, 1, 10, 100],
        'gamma': [0.1, 1, 10, 100]
    }
    # SVC declaration
    # GridSearchCV declaration
    model_svc = SVC()
    gscv_svc = GridSearchCV(model_svc,
                            param_grid=param_dict_svc, verbose=1, cv=3
                            )

    gscv_svc.fit(X_train, y_train)
    # Assigning mean test scores and best parameters
    mean_test_scores = gscv_svc.cv_results_['mean_test_score']
    best_params = gscv_svc.best_params_
    # Model is fitted with best parameters
    model_svc = SVC(C=best_params['C'],
                    gamma=gscv_svc.best_params_['gamma'],
                    kernel=best_params['kernel'])
    # And fitted to training set
    model_svc.fit(X_train, y_train)
    # Output prediction
    y_pred = model_svc.predict(X_test)

    # Visualization
    fig, ax = plt.subplots(1, 2, figsize=(20, 9))

    # X-Axis is generated
    x_values = range(len(mean_test_scores))
    # Line plot of accuracy score vs. hyperparameter setup index
    ax[0].plot(x_values, mean_test_scores)
    ax[0].set(title='Accuracy score vs. Hyperparameter Setup Index',
              ylabel='Accuracy Score',
              xlabel='Hyperparameters')

    # Confusion matrix plot
    conf_matrix = confusion_matrix(y_test, y_pred)
    cm_disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
    cm_disp.plot(ax=ax[1])
    ax[1].set(title='Confusion Matrix for SVC')

    plt.show()
    plt.savefig("FP_SVC_Granat.png")


if __name__ == '__main__':
    main()