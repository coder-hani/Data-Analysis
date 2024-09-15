import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_excel('Dateset/Exo1.xlsx')

def equal_width_binning(data, column_name, num_bins):
    # Calculate bin width
    bin_width = (data[column_name].max() - data[column_name].min()) / num_bins
    
    # Define bin edges
    bin_edges = [data[column_name].min() + i * bin_width for i in range(num_bins + 1)]
    
    # Create labels for the bins
    bin_labels = [f'Bin {i+1}' for i in range(num_bins)]
    
    # Perform binning
    data['Binned'] = pd.cut(data[column_name], bins=bin_edges, labels=bin_labels)
    print('binned')
    print(data)
    return data

# Function to replace values with bin means
def replace_with_bin_means(data, column_name):
    data['Binned_Mean'] = data.groupby('Binned')[column_name].transform('mean')
    print('Binned_Mean')
    print(data)
    return data

k = int(1 + 10/3 + math.log(len(df['sepal length'])))
df = equal_width_binning(df, 'sepal length', k )
df = replace_with_bin_means(df, 'sepal length')


def min_max_normalization(data, column_name):
    data[column_name] = (data[column_name] - data[column_name].min()) / (data[column_name].max() - data[column_name].min())
    print(data)
    return data

df = min_max_normalization(df, 'sepal length')
print('------------------')

def standardization(data, column_name):
    data[column_name] = (data[column_name] - data[column_name].mean()) / data[column_name].std()
    print(data)
    return data


df = standardization(df, 'sepal length')




