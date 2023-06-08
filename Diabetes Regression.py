""" Benjamin Granat
    ITP-449
    Assignment 8
    Creates a line of best fit of quantitative diabetes progression.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Function: calc_nonoutlier_range
#Parameters: dataframe
#Returns lower and upper quartile bounds for dataframe.
def calc_nonoutlier_range(data):
    Q3 = data.quantile(0.75)
    Q1 = data.quantile(0.25)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    return [lower, upper]

def main():
    # Makes sure all columns in df are printed:
    pd.set_option('display.width', None)
    # Import file into pandas df
    file_path = 'diabetes.csv'
    # Read csv file
    df_diabetes = pd.read_csv(file_path, skiprows=[0])
    # Drops null values
    df_diabetes.dropna()
    # Drops duplicate values
    df_diabetes.drop_duplicates()
    # Drops outliers
    df_target = df_diabetes['Y']
    bounds = calc_nonoutlier_range(df_target)
    filt_remove_outliers = (df_target >= bounds[0])&(df_target <= bounds[1])
    target = df_target[filt_remove_outliers]
    target = target.values.reshape(-1,1)

    # Target attribute is 'Y' - a quantitative measure
    # of disease progression one year after baseline

    # Correlation matrix to determine statistically correlated
    correlation_matrix = df_diabetes.corr()['Y']
    print(correlation_matrix)

    # Feature attribute is 'BMI' with a correlation value of 0.586450
    df_BMI = df_diabetes['BMI']
    filt_remove_outliers = (df_BMI >= bounds[0])&(df_BMI <= bounds[1])
    feature_vector = df_BMI[filt_remove_outliers]
    feature_vector = feature_vector.values.reshape(-1,1)

    # Run linear regression
    model_linreg = LinearRegression(fit_intercept=True)
    model_linreg.fit(feature_vector, target)

    # Line of best fit data sets
    feature_vector_BF = np.linspace(feature_vector.min(), feature_vector.max(), 100).reshape(-1, 1)
    target_BF = model_linreg.predict(feature_vector_BF)

    # Visualizations
    plt.scatter(feature_vector, target)
    plt.plot(feature_vector_BF, target_BF, color="orange")
    plt.xlabel("BMI")
    plt.ylabel("Progression")
    plt.title("Diabetes data: Progression vs. BMI")
    plt.legend(["Data Points", "Line of Best Fit"])
    plt.savefig("Diabetes Data")

if __name__ == '__main__':
    main()