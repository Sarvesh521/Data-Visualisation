import pandas as pd
import plotly.express as px
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'Cleaned_LA_Dataset.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

df["Binned_Age"] = pd.cut(df['Vict Age'], bins=[0, 18, 30, 50, 130], labels=['0-18', '18-30', '30-50', '50+'])
victim_descent_mapping = {
    'H': 'Hispanic/Latin/Mexican',
    'W': 'White',
    'X': 'Unknown',
    'B': 'Black',
    'O': 'Other',
    **{key: 'Miscellaneous' for key in 'ACDFGIKLPSUVZ'}
}
df["Vict Descent"] = df["Vict Descent"].map(victim_descent_mapping)
# Select and process the columns
columns = ['AREA NAME', 'Part 1-2', 'Binned_Age', 'Vict Sex','Vict Descent']
plot_data = df[columns].dropna()  # Drop rows with missing values

plot_data.to_csv('plot_data.csv', index=False) #writing data to csv for reference

fig = px.parallel_categories(
    plot_data,
    dimensions=columns,  # Ensure all columns have the correct type
    # color='Vict Age',  # Use a numeric column for coloring
    # color_continuous_scale=px.colors.sequential.Viridis,  # Color scale
)

# Update layout for better readability
fig.update_layout(
    title="Parallel Coordinates Plot for Crime Data",
    font=dict(size=12)
)

fig_json = fig.to_json()
with open('parallel_categories_plot.json', 'w') as f:
    f.write(fig_json)

fig.write_html('parallel_categories_plot.html')


# Show the plot
fig.show()