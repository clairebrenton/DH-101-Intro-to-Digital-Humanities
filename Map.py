import pandas as pd
import plotly.express as px

# Load the CSV file
csv_file_path = 'seda2023_state_poolsub_gys_updated_20240205.csv'
df_csv = pd.read_csv(csv_file_path)

# Filter the dataframe to only include rows where the subject is "mth" (math)
math_scores = df_csv[df_csv['subject'] == 'mth']

# Calculate the average math achievement score for each state in 2016 and 2023
average_math_scores_2016 = math_scores.groupby('stateabb')['gys_mn_2016_ol'].mean().reset_index()
average_math_scores_2023 = math_scores.groupby('stateabb')['gys_mn_2022_ol'].mean().reset_index()

# Merge the 2016 and 2023 dataframes on the state abbreviation
average_math_scores_change = pd.merge(average_math_scores_2016, average_math_scores_2023, on='stateabb', suffixes=('_2016', '_2022'))

# Calculate the change in average math scores from 2016 to 2023
average_math_scores_change['score_change'] = average_math_scores_change['gys_mn_2022_ol'] - average_math_scores_change['gys_mn_2016_ol']

# Create the choropleth map
fig = px.choropleth(
    average_math_scores_change,
    locations='stateabb',
    locationmode='USA-states',
    color='score_change',
    color_continuous_scale="RdBu",
    range_color=(-1, 1),
    scope="usa",
    labels={'score_change': 'Change in Average Math Score'},
    title="Change in Average Math Achievement Scores by State (2016 to 2023)"
)

# Annotate the color bar
fig.update_layout(
    coloraxis_colorbar=dict(
        title='Change in RLA Score',
        tickvals=[-1, -0.5, 0, 0.5, 1],
        ticktext=['-1.0 std dev', '-0.5 std dev', '0 (avg)', '0.5 std dev', '1.0 std dev']
    )
)

# Save the map as an interactive HTML file
html_file_path = 'change_in_math_scores_by_state.html'
fig.write_html(html_file_path)

# Show the map
fig.show()

change_in_scores_by_state = average_math_scores_change[['stateabb', 'score_change']]
change_in_scores_by_state_sorted = change_in_scores_by_state.sort_values(by='score_change', ascending=False)



print(change_in_scores_by_state_sorted)

"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('./seda2023_state_poolsub_gys_updated_20240205.csv')

# Filter for reading subject
reading_data = data[data['subject'] == 'rla']

# Calculate improvement in reading scores from 2016 to 2023
reading_data['improvement'] = reading_data['gys_mn_2023_ol'] - reading_data['gys_mn_2016_ol']

# Sort the data by improvement
reading_data_sorted = reading_data.sort_values(by='improvement', ascending=False)

# Plot the improvements as a bar chart
plt.figure(figsize=(15, 10))
plt.barh(reading_data_sorted['stateabb'], reading_data_sorted['improvement'], color='skyblue')
plt.xlabel('Improvement in RLA Scores (2016-2023)')
plt.ylabel('State')
plt.title('Improvement in RLA Scores by Points by State (2016-2023)')
plt.gca().invert_yaxis()
plt.show()
"""