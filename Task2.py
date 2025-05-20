#Task 2: Basic Data Analysis
# Compute basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(iris_df.describe())

# Group by species and compute mean of numerical columns
print("\nMean measurements by species:")
print(iris_df.groupby('species').mean())

# Interesting findings observation
print("\nInteresting findings:")
print("Setosa has significantly smaller petal length and width compared to other species.")
print("Virginica has the largest sepal length on average.")