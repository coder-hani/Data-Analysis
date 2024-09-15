import pandas as pd

# Load the dataset
df = pd.read_excel('Dateset/Dataset1.xlsx')

# Print the first 5 rows of the dataframe
print('First 5 rows of the dataset:')
print(df.head())

# Median for each column
print('--------------------------------------')
print('Median in each column:')
print('Petal Length:', df['petal length'].median())
print('Petal Width:', df['petal width'].median())
print('Sepal Length:', df['sepal length'].median())
print('Sepal Width:', df['sepal width'].median())

# Average for each column
print('--------------------------------------')
print('Average (Mean) in each column:')
print('Petal Length:', df['petal length'].mean())
print('Petal Width:', df['petal width'].mean())
print('Sepal Length:', df['sepal length'].mean())
print('Sepal Width:', df['sepal width'].mean())

# Mode for each column
print('--------------------------------------')
print('Mode in each column:')
print('Petal Length:', df['petal length'].mode()[0])  # Mode returns a series, using [0] to get the first mode
print('Petal Width:', df['petal width'].mode()[0])
print('Sepal Length:', df['sepal length'].mode()[0])
print('Sepal Width:', df['sepal width'].mode()[0])

# Q0 (Minimum) for each column
print('--------------------------------------')
print('Q0 (Minimum) in each column:')
print('Petal Length:', df['petal length'].min())
print('Petal Width:', df['petal width'].min())
print('Sepal Length:', df['sepal length'].min())
print('Sepal Width:', df['sepal width'].min())

# Q1 (25th percentile) for each column
print('--------------------------------------')
print('Q1 (25%) in each column:')
print('Petal Length:', df['petal length'].quantile(0.25))
print('Petal Width:', df['petal width'].quantile(0.25))
print('Sepal Length:', df['sepal length'].quantile(0.25))
print('Sepal Width:', df['sepal width'].quantile(0.25))

# Q2 (Median) for each column
print('--------------------------------------')
print('Q2 (Median) in each column:')
print('Petal Length:', df['petal length'].median())
print('Petal Width:', df['petal width'].median())
print('Sepal Length:', df['sepal length'].median())
print('Sepal Width:', df['sepal width'].median())

# Q3 (75th percentile) for each column
print('--------------------------------------')
print('Q3 (75%) in each column:')
print('Petal Length:', df['petal length'].quantile(0.75))
print('Petal Width:', df['petal width'].quantile(0.75))
print('Sepal Length:', df['sepal length'].quantile(0.75))
print('Sepal Width:', df['sepal width'].quantile(0.75))

# Q4 (Maximum) for each column
print('--------------------------------------')
print('Q4 (Maximum) in each column:')
print('Petal Length:', df['petal length'].max())
print('Petal Width:', df['petal width'].max())
print('Sepal Length:', df['sepal length'].max())
print('Sepal Width:', df['sepal width'].max())

# Null values in each column
print('--------------------------------------')
print('Null values in each column:')
print('Petal Length:', df['petal length'].isnull().sum())
print('Petal Width:', df['petal width'].isnull().sum())
print('Sepal Length:', df['sepal length'].isnull().sum())
print('Sepal Width:', df['sepal width'].isnull().sum())

# Percentage of null values in each column
print('--------------------------------------')
print('Percentage of null values in each column:')
print('Petal Length:', df['petal length'].isnull().sum() / len(df) * 100, '%')
print('Petal Width:', df['petal width'].isnull().sum() / len(df) * 100, '%')
print('Sepal Length:', df['sepal length'].isnull().sum() / len(df) * 100, '%')
print('Sepal Width:', df['sepal width'].isnull().sum() / len(df) * 100, '%')
