import pandas as pd
from scipy.stats import f_oneway

# Data
data = {
    'Electrical': {
        'Researching': [6, 6, 9, 7, 6, 6, 8],  # Yes counts for each software tool
        'Not Researching': [15, 14, 11, 13, 15, 15, 13]  # No counts for each software tool
    },
    'Programming': {
        'Researching': [11, 11, 8, 7, 11, 11, 7], 
        'Not Researching': [9, 9, 12, 13, 9, 9, 13]
    },
    'Physics': {
        'Researching': [14, 14, 10, 6, 14, 14, 10], 
        'Not Researching': [6, 6, 10, 14, 6, 6, 10]
    },
    'Chemistry': {
        'Researching': [10, 10, 5, 8, 10, 10, 5], 
        'Not Researching': [0, 1, 6, 3, 0, 0, 5]
    },
    'Math': {
        'Researching': [14, 14, 9, 8, 14, 14, 7], 
        'Not Researching': [3, 3, 8, 9, 3, 3, 10]
    }
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Perform ANOVA test
anova_results = {}
for area_of_interest, software_data in df.items():
    research_yes = software_data['Researching']
    research_no = software_data['Not Researching']
    f_statistic, p_value = f_oneway(research_yes, research_no)
    anova_results[area_of_interest] = {'F-statistic': f_statistic, 'p-value': p_value}

# Print ANOVA results
print("ANOVA Results:")
for area_of_interest, result in anova_results.items():
    print(f"{area_of_interest}: F-statistic = {result['F-statistic']}, p-value = {result['p-value']}")
