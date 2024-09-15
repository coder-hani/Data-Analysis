import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset/Dataset2.csv')

# Grouping by 'zcta' and calculating the sum of 'case count' and 'positive tests'
grouped_data = df.groupby('zcta')[['case count', 'positive tests']].sum()

# Plotting the bar chart with two bars for each zone
grouped_data.plot(kind='bar', width=0.8)
plt.xlabel('Zone')
plt.ylabel('Total number')
plt.title('Distribution of the total number of confirmed cases and positive tests by zones')
plt.legend(['Confirmed cases', 'Positive tests'])
plt.show()

# Convert the 'Start date' column to datetime objects by trying multiple formats
df['Start_date'] = pd.to_datetime(df['Start date'], errors='coerce')

# Convert the 'end date' column in the same way if necessary
df['end date'] = pd.to_datetime(df['end date'], errors='coerce')

# Extract the year from the 'Start date' column
df['Year'] = df['Start date'].dt.year
print(df['Start_date'])

# Assuming df is your DataFrame with the COVID-19 data

# Convert 'Start date' to datetime if not already done
