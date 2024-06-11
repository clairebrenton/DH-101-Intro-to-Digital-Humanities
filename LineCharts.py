import pandas as pd
import matplotlib.pyplot as plt
"""
# Load the data from the provided CSV file
data_path = 'seda2023_state_poolsub_gys_updated_20240205.csv'

# Read the data and codebook
data = pd.read_csv(data_path)

# Filter data for math scores across all subgroups and the specified years
# Filter data for math scores across all subgroups and the specified years
math_data = data[(data['subject'] == 'mth') & (data['subgroup'] == 'all')]

# Select relevant columns for plotting
years = ['gys_mn_2016_ol', 'gys_mn_2017_ol', 'gys_mn_2018_ol', 'gys_mn_2019_ol', 'gys_mn_2022_ol', 'gys_mn_2023_ol']
math_scores = math_data[years].mean()

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot([2016, 2017, 2018, 2019, 2022, 2023], math_scores, marker='o', linestyle='-')
plt.title('Overall Change in Math Scores (2016-2023)')
plt.xlabel('Year')
plt.ylabel('Average Math Score')
plt.xticks([2016, 2017, 2018, 2019, 2022, 2023], rotation=45)
plt.grid(True)
plt.show()
"""
import matplotlib.pyplot as plt

data_path = 'seda2023_state_poolsub_gys_updated_20240205.csv'

# Read the data and codebook
data = pd.read_csv(data_path)

# Filter data for math scores across all subgroups and the specified years
math_data = data[(data['subject'] == 'rla') & (data['subgroup'] == 'all')]

# Select relevant columns for plotting
years = ['gys_mn_2016_ol', 'gys_mn_2017_ol', 'gys_mn_2018_ol', 'gys_mn_2019_ol', 'gys_mn_2022_ol', 'gys_mn_2023_ol']
math_scores = math_data[years].mean()

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot([2016, 2017, 2018, 2019, 2022, 2023], math_scores, marker='o', linestyle='-')
plt.title('Overall Change in RLA Scores (2016-2023)')
plt.xlabel('Year')
plt.ylabel('Average RLA Score (Standardized)')
plt.xticks([2016, 2017, 2018, 2019, 2022, 2023], rotation=45)
plt.grid(True)

# Adding explanatory annotations
plt.annotate('Note: Scores are standardized values indicating average RLA achievement.',
             xy=(0.5, -0.15), xycoords='axes fraction', ha='center', fontsize=10)

# Adding context to the y-axis
plt.text(2024, 0, 'Baseline/Average Performance', va='center', ha='right', color='black', fontsize=9)
plt.text(2024, -0.5, 'Below Average\nPerformance\n(-0.5 SD)', va='center', ha='right', color='red', fontsize=9)
plt.text(2024, 0.5, 'Above Average\nPerformance\n(+0.5 SD)', va='center', ha='right', color='green', fontsize=9)

plt.show()
