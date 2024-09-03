import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb

areas_of_interest = ['Electrical', 'Programming', 'Physics', 'Chemistry', 'Math']
total_students = [21, 20, 20, 6, 17]
researching_students = [6, 11, 14, 10, 14]
total_students_tested = 37

# Calculate combinations and probabilities
combinations = [comb(total_students[i], researching_students[i]) for i in range(len(areas_of_interest))]
probabilities = [researching_students[i] / total_students[i] for i in range(len(areas_of_interest))]

# Scale bubble sizes based on the total number of students tested
max_bubble_size = 1000
scaled_sizes = [max_bubble_size * (total_students[i] / total_students_tested) for i in range(len(areas_of_interest))]

# Bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(combinations, probabilities, s=scaled_sizes, alpha=0.7)
plt.title('OSU CEAT Students')
plt.xlabel("Students at OSU")
plt.ylabel('Ratio of Students Involved in Research')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Add labels for each bubble
for i in range(len(areas_of_interest)):
    plt.text(combinations[i], probabilities[i], areas_of_interest[i], ha='center', va='bottom')

plt.show()
