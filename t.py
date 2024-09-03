import matplotlib.pyplot as plt

# ANOVA Results
results = {
    'Electrical': {'F-statistic': 88.62, 'p-value': 6.85e-07},
    'Programming': {'F-statistic': 1.16, 'p-value': 0.3033},
    'Physics': {'F-statistic': 4.15, 'p-value': 0.0642},
    'Chemistry': {'F-statistic': 21.92, 'p-value': 0.00053},
    'Math': {'F-statistic': 11.31, 'p-value': 0.00565}
}

# Extract F-statistic and p-value for plotting
area_of_interest = list(results.keys())
f_statistic = [result['F-statistic'] for result in results.values()]
p_value = [result['p-value'] for result in results.values()]

# Plotting
plt.figure(figsize=(10, 6))

# Plot F-statistic
plt.bar(area_of_interest, f_statistic, color='blue', alpha=0.7, label='F-statistic')

# Plot p-value on secondary y-axis
plt.twinx()
plt.plot(area_of_interest, p_value, color='red', marker='o', label='p-value')

# Add labels and title
plt.xlabel('Area of Interest')
plt.ylabel('F-statistic')
plt.title('ANOVA Results: F-statistic and p-value by Area of Interest')
plt.legend(loc='upper left')

plt.show()

