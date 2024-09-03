import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn3

# Define the data
areas_of_interest = ['Electrical', 'Programming', 'Physics', 'Chemistry', 'Math']
comsol_usage = [12, 2, 15, 5, 3]

# Create Venn diagram
plt.figure(figsize=(8, 6))
venn3(subsets=(comsol_usage[0], comsol_usage[1], comsol_usage[2], comsol_usage[3], comsol_usage[4], 0, 0),
      set_labels=('Electrical', 'Physics', 'Chemistry'))

# Set title and show plot
plt.title('Usage of COMSOL Multiphysics among Students')
plt.show()
