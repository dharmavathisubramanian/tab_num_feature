# display.py

import streamlit as st
from logics import load_csv, get_numeric_columns, numeric_column_stats, generate_histogram_chart, top_values_percentage

def main():
    st.title("CSV Explorer")

    # Menu for uploading a CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file:
        # Read the CSV file
        df = load_csv(uploaded_file)

        # Display overall information of the dataset
        st.write("Overall Information:")
        st.write(df.head())

        # Display numeric column selection box
        numeric_columns = get_numeric_columns(df)
        selected_numeric_column = st.selectbox("Select a numeric column", numeric_columns)

        # Display numeric column statistics
        st.write("Numeric Column Statistics:")
        stats = numeric_column_stats(df, selected_numeric_column)
        st.table(stats)

        # Display interactive Altair histogram chart
        st.write("Histogram Chart:")
        chart = generate_histogram_chart(df, selected_numeric_column)
        st.altair_chart(chart)

        # Display top values and percentages
        st.write("Top Values and Percentages:")
        top_values_df = top_values_percentage(df, selected_numeric_column)
        st.table(top_values_df)

if __name__ == "__main__":
    main()
