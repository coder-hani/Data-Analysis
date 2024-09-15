import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Datasets/Cleaned_Dataset2.csv')

# Filter the dataset for the specific zone "95127"
df_filtered = df[df['zcta'] == 95127]

# Convert 'Start date' to datetime format
df_filtered['Start date'] = pd.to_datetime(df_filtered['Start date'])

# Create a new column for week, month, and year
df_filtered['Week_Year'] = df_filtered['Start date'].dt.strftime('%Y-%U')  # Combine Year and Week
df_filtered['Month_Year'] = df_filtered['Start date'].dt.strftime('%Y-%m')
df_filtered['Year'] = df_filtered['Start date'].dt.year

# Set seaborn style
sns.set(style="whitegrid")

# Plot 1: Over the Year
plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='case count', data=df_filtered, marker='o', label='Confirmed Cases')
sns.lineplot(x='Year', y='test count', data=df_filtered, marker='o', label='COVID-19 Tests')
sns.lineplot(x='Year', y='positive tests', data=df_filtered, marker='o', label='Positive Tests')
plt.title('Annual Summary: Evolution of COVID-19 Tests, Positive Tests, and Confirmed Case Statistics - Zone 95127')
plt.ylabel('Total number')
plt.show()

# Plot 2: By Month/Year
plt.figure(figsize=(10, 5))
# Sort the DataFrame by 'Month_Year' before plotting
df_sorted_month = df_filtered.sort_values('Month_Year')
sns.lineplot(x='Month_Year', y='case count', data=df_sorted_month, marker='o', label='Confirmed Cases')
sns.lineplot(x='Month_Year', y='test count', data=df_sorted_month, marker='o', label='COVID-19 Tests')
sns.lineplot(x='Month_Year', y='positive tests', data=df_sorted_month, marker='o', label='Positive Tests')
plt.title('Monthly View: Evolution of COVID-19 Tests, Positive Tests, and Confirmed Case Statistics - Zone 95127')
plt.ylabel('Total number')
plt.xticks(rotation=45)
plt.show()

# Plot 3: By Week/Year
plt.figure(figsize=(10, 5))
# Sort the DataFrame by 'Week_Year' before plotting
df_sorted_week = df_filtered.sort_values('Week_Year')
sns.lineplot(x='Week_Year', y='case count', data=df_sorted_week, marker='o', label='Confirmed Cases')
sns.lineplot(x='Week_Year', y='test count', data=df_sorted_week, marker='o', label='COVID-19 Tests')
sns.lineplot(x='Week_Year', y='positive tests', data=df_sorted_week, marker='o', label='Positive Tests')
plt.title('Weekly Perspective: Evolution of COVID-19 Tests, Positive Tests, and Confirmed Case Statistics - Zone 95127')
plt.ylabel('Total number')
plt.xticks(rotation=45)
plt.show()
