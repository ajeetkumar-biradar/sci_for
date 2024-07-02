import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Downloading the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
iris_df = pd.read_csv(url, names=column_names)

# Step 2: Data Analysis with Pandas
# Check the first few rows of the dataset
print(iris_df.head())

# Check summary statistics
print(iris_df.describe())

# Check basic information about the dataset
print(iris_df.info())

# Step 3: Data Visualization with Matplotlib
# Histograms for each feature
iris_df.hist()
plt.tight_layout()
plt.show()

# Box plot for each feature by species
iris_df.boxplot(by="species", figsize=(10, 6))
plt.tight_layout()
plt.show()

# Scatter plot for sepal length vs sepal width
plt.scatter(iris_df["sepal_length"], iris_df["sepal_width"], c=iris_df["species"].astype("category").cat.codes)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter Plot of Sepal Length vs Sepal Width")
plt.show()
