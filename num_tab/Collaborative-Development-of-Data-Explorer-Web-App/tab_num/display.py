import streamlit as st

from tab_num.logics import NumericColumn

def display_tab_num_content(file_path=None, df=None):
    numeric_col = NumericColumn(df=df)
    numeric_col.find_num_cols()
    selected_numcol = st.selectbox('Which numeric column do you want to explore', numeric_col.cols_list)
    numeric_col.set_data(selected_numcol)
    with st.expander("Numeric Column"):
        num_summary = numeric_col.get_summary()
        st.table(num_summary)
        numeric_col.set_histogram()
        num_histogram = numeric_col.histogram
        st.altair_chart(num_histogram, use_container_width=True)
        numeric_col.set_frequent()
        num_frequent = numeric_col.frequent
        st.write("Most Frequent Values")
        st.dataframe(num_frequent)
    """
    --------------------
    Description
    --------------------
    -> display_tab_num_content (function): Function that will instantiate tab_num.logics.NumericColumn class, save it into Streamlit session state and call its tab_num.logics.NumericColumn.find_num_cols() method in order to find all numeric columns.
    Then it will display a Streamlit select box with the list of numeric columns found.
    Once the user select a numeric column from the select box, it will call the tab_num.logics.NumericColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_num.logics.NumericColumn.get_summary() as a Streamlit Table
    - the graph from tab_num.logics.NumericColumn.histogram using Streamlit.altair_chart()
    - the results of tab_num.logics.NumericColumn.frequent using Streamlit.write
 
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """
    
