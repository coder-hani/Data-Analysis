import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('Datasets/clean_dataset2.csv')

# Convert 'Start date' to datetime format
df['Start date'] = pd.to_datetime(df['Start date'])

# Set 'Start date' as the index
df.set_index('Start date', inplace=True)

# Group data by 'population' and sum the 'case count' for each group
df_grouped = df.groupby('population')['case count'].sum().reset_index()

# Plot bar chart
plt.figure(figsize=(12, 6))

# Bar chart for case count
sns.barplot(x='population', y='case count', data=df_grouped)

# Set labels and title
plt.xlabel('Population')
plt.ylabel('Tests Conducted')
plt.title('Analysis of the Correlation between Population and Number of Tests Conducted')

# Show the plot
plt.show()
