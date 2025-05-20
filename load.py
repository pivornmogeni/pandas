#Task 1: Load and Explore the Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], 
                      columns=iris['feature_names'] + ['target'])

# Map target values to species names
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows
print("First 5 rows of the dataset:")
print(iris_df.head())

# Explore the structure
print("\nDataset structure:")
print(iris_df.info())

# Check for missing values
print("\nMissing values:")
print(iris_df.isnull().sum())

# Since there are no missing values, no cleaning is needed
print("\nNo missing values found, so no cleaning required.")
