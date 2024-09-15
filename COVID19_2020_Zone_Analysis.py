import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('Datasets/clean_dataset2.csv')

# Convert 'Start date' to datetime format
df['Start date'] = pd.to_datetime(df['Start date'])

# Filter data for the year 2020
df_2020 = df[df['Start date'].dt.year == 2020]

# Assuming your dataset has columns 'zcta', 'case count', 'test count', 'positive tests'
# Convert 'Start date' to datetime format
df_2020['Start date'] = pd.to_datetime(df_2020['Start date'])

# Set 'Start date' as the index
df_2020.set_index('Start date', inplace=True)

# Group data by 'zcta' and sum the values for each group
df_grouped = df_2020.groupby('zcta')[['case count', 'test count', 'positive tests']].sum()

# Plot bar charts for each zone
plt.figure(figsize=(12, 6))

bar_width = 0.2
bar_positions = range(len(df_grouped))

# Bar chart for case count
plt.bar(bar_positions, df_grouped['case count'], width=bar_width, label='Confirmed Cases', align='center')
# Bar chart for test count
plt.bar([pos + bar_width for pos in bar_positions], df_grouped['test count'], width=bar_width, label='Tests Conducted', align='center')
# Bar chart for positive tests
plt.bar([pos + 2 * bar_width for pos in bar_positions], df_grouped['positive tests'], width=bar_width, label='Positive Tests', align='center')

# Set x-axis labels and ticks
plt.xticks([pos + bar_width for pos in bar_positions], df_grouped.index)

# Set labels and title
plt.xlabel('Zone')
plt.ylabel('Total Number')
plt.title('2020 Analysis: Evolution of Tests, Confirmed Cases, and Positive Tests by Zone')

# Show legend
plt.legend()

# Show the plot
plt.show()
