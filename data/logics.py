# logics.py

import pandas as pd
import altair as alt

# Function to load CSV file and return DataFrame
def load_csv(file_path):
    # Load CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    return df

# Function to display numeric series information
def get_numeric_columns(df):
    # Get a list of numeric columns in the DataFrame
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    return numeric_columns

def numeric_column_stats(df, column_name):
    # Calculate statistics for the selected numeric column
    stats = {
        'Unique Values': df[column_name].nunique(),
        'Missing Values': df[column_name].isnull().sum(),
        'Occurrences of 0': (df[column_name] == 0).sum(),
        'Average value': df[column_name].mean(),
        'Standard deviation': df[column_name].std(),
        'Minimum value': df[column_name].min(),
        'Maximum value': df[column_name].max(),
        'Median value': df[column_name].median(),
    }
    return stats

def generate_histogram_chart(df, column_name):
    # Generate an Altair histogram chart for the selected numeric column
    chart = alt.Chart(df).mark_bar().encode(
        alt.X(column_name, bin=True),
        alt.Y('count()')
    ).properties(
        width=500,
        height=300
    )
    return chart

def top_values_percentage(df, column_name, top_n=20):
    # Get the top N most frequent values and their percentages
    top_values = df[column_name].value_counts().head(top_n)
    percentage = (top_values / len(df)) * 100
    result_df = pd.DataFrame({
        'Value': top_values.index,
        'Occurrences': top_values.values,
        'Percentage': percentage.values
    })
    return result_df



