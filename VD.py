import matplotlib.pyplot as plt

# Define the data
areas_of_interest = ['Electrical', 'Programming', 'Physics', 'Chemistry', 'Math']
software = ['Solidworks', 'Autocad', 'Matlab', 'Simulink', 'Ansys']
probabilities_yes = [[17, 10, 8, 3, 12],
                     [9, 6, 7, 2, 11],
                     [14, 12, 10, 5, 9],
                     [7, 6, 1, 8, 11],
                     [7, 8, 5, 3, 7]]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the probabilities
for i, area in enumerate(areas_of_interest):
    for j, software_tool in enumerate(software):
        probability = probabilities_yes[i][j] / 37  # Total students tested = 37
        plt.scatter(j, i, s=probability * 200000, alpha=0.7, label=f'{software_tool}: {probability:.2f}')

# Add labels and legend
plt.xticks(range(len(software)), software, rotation=45)
plt.yticks(range(len(areas_of_interest)), areas_of_interest)
plt.xlabel('Software')
plt.ylabel('Area of Interest')
plt.title('Area of Interest Branching vs Software')
#plt.legend(title='Probability', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
