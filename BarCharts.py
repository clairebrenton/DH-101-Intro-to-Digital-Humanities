import pandas as pd
import matplotlib.pyplot as plt
"""
# Assuming 'data' is your DataFrame containing the relevant data
data_path = './seda2023_state_poolsub_gys_updated_20240205.csv'  # Replace with your actual file path
data = pd.read_csv(data_path)

# Filter data for the required subgroups and subjects for the years 2019 and 2022
subgroups = ['blk', 'hsp', 'wht']
subjects = ['mth', 'rla']
required_columns = ['subject', 'subgroup', 'gys_mn_2019_ol', 'gys_mn_2022_ol']

# Filter the data
filtered_data = data[(data['subgroup'].isin(subgroups)) & (data['subject'].isin(subjects))]
filtered_data = filtered_data[required_columns]

# Drop rows with any missing values in the required columns
filtered_data.dropna(subset=['gys_mn_2019_ol', 'gys_mn_2022_ol'], inplace=True)

# Calculate score change from 2019 to 2022
filtered_data['score_change'] = filtered_data['gys_mn_2022_ol'] - filtered_data['gys_mn_2019_ol']

# Pivot table for plotting
score_change_pivot = filtered_data.pivot_table(index='subgroup', columns='subject', values='score_change', aggfunc='mean')

# Plotting with specified colors
score_change_pivot.plot(kind='bar', figsize=(10, 6), color=['red', 'blue'])
plt.title('Average Score Changes from 2019 to 2022 by Subgroup and Subject')
plt.xlabel('Subgroup')
plt.ylabel('Average Score Change')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.legend(title='Subject', labels=['Math', 'Reading & Language Arts'])
plt.show()
"""
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data_path = './seda2023_state_poolsub_gys_updated_20240205.csv'  # Replace with your actual file path
data = pd.read_csv(data_path)

# Filter data for the required subgroups and subjects for the years 2019 and 2022
subgroups = ['blk', 'hsp', 'wht']
subjects = ['mth', 'rla']
required_columns = ['subject', 'subgroup', 'gys_mn_2019_ol', 'gys_mn_2022_ol']

# Filter the data
filtered_data = data[(data['subgroup'].isin(subgroups)) & (data['subject'].isin(subjects))]
filtered_data = filtered_data[required_columns]

# Drop rows with any missing values in the required columns
filtered_data.dropna(subset=['gys_mn_2019_ol', 'gys_mn_2022_ol'], inplace=True)

# Calculate score change and percent change from 2019 to 2022
filtered_data['score_change'] = filtered_data['gys_mn_2022_ol'] - filtered_data['gys_mn_2019_ol']
filtered_data['percent_change'] = (filtered_data['score_change'] / abs(filtered_data['gys_mn_2019_ol'])) * 100

# Pivot table for plotting percentage changes
percent_change_pivot = filtered_data.pivot_table(index='subgroup', columns='subject', values='percent_change', aggfunc='mean')

# Set less saturated colors for the plot
colors = ['#FF9999', '#9999FF']  # Light red for math, light blue for RLA

# Plotting percentage change for Math
plt.figure(figsize=(8, 6))
percent_change_pivot['mth'].plot(kind='bar', color=colors[0], title='Math: Percent Change from 2019 to 2022')
plt.ylabel('Percent Change (%)')
plt.xlabel('Subgroup')
plt.grid(axis='y', linestyle='--')
plt.show()

# Plotting percentage change for Reading and Language Arts
plt.figure(figsize=(8, 6))
percent_change_pivot['rla'].plot(kind='bar', color=colors[1], title='Reading & Language Arts: Percent Change from 2019 to 2022')
plt.xlabel('Subgroup')
plt.ylabel('Percent Change (%)')
plt.grid(axis='y', linestyle='--')
plt.show()
"""

# Load the data from the provided CSV file
data_path = './seda2023_state_poolsub_gys_updated_20240205.csv'  # Replace with your actual file path
data = pd.read_csv(data_path)

# Filter the data for relevant subjects, subgroups, and years
relevant_subgroups = ['blk', 'hsp', 'wht']
relevant_years = ['gys_mn_2019_ol', 'gys_mn_2023_ol']

filtered_data = data[(data['subgroup'].isin(relevant_subgroups)) & (data['subject'].isin(['mth', 'rla']))][['stateabb', 'subject', 'subgroup'] + relevant_years]

# Calculate the score change and percentage change
filtered_data['score_change'] = filtered_data['gys_mn_2023_ol'] - filtered_data['gys_mn_2019_ol']
filtered_data['2019_score'] = filtered_data['gys_mn_2019_ol']
filtered_data['percent_change'] = (filtered_data['score_change'] / abs(filtered_data['2019_score'])) * 100

# Group by subject and subgroup to get the average percentage changes
average_percent_changes = filtered_data.groupby(['subject', 'subgroup'])['percent_change'].mean().unstack()

# Separate the data by subject for individual charts
math_changes = average_percent_changes.loc['mth'].transpose()
rla_changes = average_percent_changes.loc['rla'].transpose()

# Plotting separate charts for Math and Reading Language Arts in different windows
# Math Scores Changes
plt.figure(figsize=(9, 6))
math_changes.plot(kind='bar', color='lightcoral')
plt.title('Math Score Changes from 2019 to 2023 by Race/Ethnicity')
plt.ylabel('Average Percentage Score Change (%)')
plt.xlabel('Race/Ethnicity')
plt.xticks(rotation=0)
plt.axhline(0, color='black', linewidth=0.8)
plt.show()

# Reading Language Arts Scores Changes
plt.figure(figsize=(9, 6))
rla_changes.plot(kind='bar', color='lightskyblue')
plt.title('Reading Language Arts Score Changes from 2019 to 2023 by Race/Ethnicity')
plt.xlabel('Race/Ethnicity')
plt.xticks(rotation=0)
plt.axhline(0, color='black', linewidth=0.8)
plt.show()

# Filter data for economically disadvantaged ('ecd') and not economically disadvantaged ('nec') subgroups
economic_groups = ['ecd', 'nec']
economic_data = data[(data['subgroup'].isin(economic_groups)) & (data['subject'].isin(['mth', 'rla']))]

# Calculate the score change for these groups
economic_data['score_change'] = economic_data['gys_mn_2023_ol'] - economic_data['gys_mn_2019_ol']

# Calculate percentage changes
economic_data['percent_change'] = (economic_data['score_change'] / economic_data['gys_mn_2019_ol'].abs()) * 100
average_percent_changes = economic_data.groupby(['subject', 'subgroup'])['percent_change'].mean().unstack()

# Plotting the original bar chart with updates
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['lightskyblue', 'lightcoral']
average_percent_changes.plot(kind='bar', ax=ax, color=colors)
ax.set_title('Average Percentage Score Changes by Economic Group (2019 to 2023)')
ax.set_ylabel('Average Percentage Score Change (%)')
ax.set_xlabel('Subject')
ax.set_xticklabels(['Math', 'Reading Language Arts'], rotation=0)
ax.legend(title='Economic Group', title_fontsize='13', fontsize='11', loc='upper left')

plt.show()
data = pd.read_csv('path_to_your_data.csv')