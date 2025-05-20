# Set the style for plots
sns.set_style("whitegrid")
plt.figure(figsize=(15, 10))

# 1. Line chart (simulating trends over time - though not perfect for Iris data)
plt.subplot(2, 2, 1)
iris_df_sample = iris_df.sample(10).sort_index()  # Take a sample to simulate time series
plt.plot(iris_df_sample.index, iris_df_sample['sepal length (cm)'], marker='o', label='Sepal Length')
plt.plot(iris_df_sample.index, iris_df_sample['petal length (cm)'], marker='s', label='Petal Length')
plt.title('Simulated Trend of Sepal and Petal Lengths')
plt.xlabel('Sample Index')
plt.ylabel('Length (cm)')
plt.legend()

# 2. Bar chart - average sepal length by species
plt.subplot(2, 2, 2)
sns.barplot(x='species', y='sepal length (cm)', data=iris_df, ci=None)
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')

# 3. Histogram - distribution of petal width
plt.subplot(2, 2, 3)
sns.histplot(iris_df['petal width (cm)'], bins=15, kde=True)
plt.title('Distribution of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')

# 4. Scatter plot - sepal length vs petal length
plt.subplot(2, 2, 4)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.tight_layout()
plt.show()