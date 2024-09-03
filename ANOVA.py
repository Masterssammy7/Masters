import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
data = {
    'Area_of_Interest': ['Electrical'] * 5 + ['Programming'] * 5 + ['Physics'] * 5 + ['Chemistry'] * 5 + ['Math'] * 5,
    'Software': ['Solidworks', 'Autocad', 'Matlab', 'Simulink', 'Ansys'] * 5,
    'Yes': [17, 10, 8, 3, 12, 9, 6, 7, 2, 11, 14, 12, 10, 5, 9, 7, 6, 1, 8, 11, 7, 8, 5, 3, 7],
    'No': [0, 10, 12, 14, 5, 8, 14, 13, 16, 6, 3, 8, 10, 13, 8, 10, 14, 17, 15, 9, 13, 12, 16, 15, 10]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total counts for each area of interest and software
total_counts = df.groupby(['Area_of_Interest', 'Software'])[['Yes', 'No']].sum()

# Calculate probabilities
total_counts['Probability_Yes'] = total_counts['Yes'] / (total_counts['Yes'] + total_counts['No'])
total_counts['Probability_No'] = 1 - total_counts['Probability_Yes']

# Reshape the DataFrame for plotting
probabilities = total_counts.reset_index().pivot(index='Area_of_Interest', columns='Software', values=['Probability_Yes'])

# Plotting
plt.figure(figsize=(10, 6))
sns.heatmap(probabilities['Probability_Yes'], cmap='YlGnBu', annot=True, fmt=".2f", linewidths=.5)
plt.title('Probability Distribution of Area of Interest vs Software')
plt.xlabel('Software')
plt.ylabel('Area of Interest')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
