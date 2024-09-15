import pandas as pd

df = pd.read_csv('Datasets/Dataset2.csv')
# Convert date columns for rows 1 to 191 to '5-Apr/2020' format
df.loc[191:, ['Start date', 'end date']] = df.loc[191:, ['Start date', 'end date']] + '/2020'
df.loc[191:, ['Start date', 'end date']] = df.loc[191:, ['Start date', 'end date']].apply(pd.to_datetime, format='%d-%b/%Y', errors='coerce')

# Convert date columns for the rest of the DataFrame
df.loc[:190, 'Start date'] = pd.to_datetime(df.loc[:190, 'Start date'], errors='coerce')
df.loc[:190, 'end date'] = pd.to_datetime(df.loc[:190, 'end date'], errors='coerce')


# Check for missing values
print(df.isnull().sum())

# Convert columns to appropriate data types
df[['case count', 'test count', 'positive tests']] = df[['case count', 'test count', 'positive tests']].apply(pd.to_numeric, errors='coerce')

# Display the cleaned and processed DataFrame
print(df)
df.to_csv('dataset2.csv', index=False)