import numpy as np
import matplotlib.pyplot as plt

# Define the data
areas_of_interest = ['Electrical', 'Programming', 'Physics', 'Chemistry', 'Math']
software = ['Solidworks', 'Autocad', 'Matlab', 'Simulink', 'Ansys', 'Python', 'COMSOL']
probabilities_yes = np.array([
    [17, 10, 8, 3, 12, 8, 6],
    [9, 6, 7, 2, 11, 9, 4],
    [14, 12, 10, 5, 9, 5, 9],
    [7, 6, 1, 8, 11, 3, 2],
    [7, 8, 5, 3, 7, 7, 5]
])
total_students = np.array([21, 20, 20, 6, 17])

# Calculate probabilities
probabilities = probabilities_yes / total_students[:, np.newaxis]

# Create the Venn diagram
plt.figure(figsize=(8, 6))
plt.title('Area of Interest and NULL Test of COMSOL Software')
plt.xlabel('Software')
plt.ylabel('Area of Interest')

# Plot each set
for i, area in enumerate(areas_of_interest):
    for j, software_tool in enumerate(software):
        prob = probabilities[i, j]
        plt.scatter(j, i, s=prob * 20000, alpha=0.7, label=f'{software_tool}: {prob:.2f}')

# Add legend
#plt.legend(title='Probability', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust tick labels
plt.xticks(range(len(software)), software, rotation=45)
plt.yticks(range(len(areas_of_interest)), areas_of_interest)

plt.grid(True)
plt.tight_layout()
plt.show()
