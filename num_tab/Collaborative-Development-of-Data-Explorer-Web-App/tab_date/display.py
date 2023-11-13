import streamlit as st

from tab_date.logics import DateColumn

def display_tab_date_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_date_content (function): Function that will instantiate tab_date.logics.DateColumn class, save it into Streamlit session state and call its tab_date.logics.DateColumn.find_date_cols() method in order to find all datetime columns.
    Then it will display a Streamlit select box with the list of datetime columns found.
    Once the user select a datetime column from the select box, it will call the tab_date.logics.DateColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_date.logics.DateColumn.get_summary() as a Streamlit Table
    - the graph from tab_date.logics.DateColumn.histogram using Streamlit.altair_chart()
    - the results of tab_date.logics.DateColumn.frequent using Streamlit.write
 
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
    if file_path is not None:
        # Instantiate DateColumn class
        date_column = DateColumn(file_path, df)

        # Save the instance to Streamlit session state
        st.session_state.date_column = date_column

        # Find datetime columns
        st.session_state.date_column.find_date_cols()
    #else:
        #st.error("Please upload a CSV file.")
    
    # Create a select box to choose a datetime column
    selected_column = st.selectbox("Which datetime column do you want to explore?", st.session_state.date_column.cols_list)
    
    if selected_column:
        # Set data for the selected column
        st.session_state.date_column.set_data(selected_column)

        # Convert series to Date
        st.session_state.date_column.convert_serie_to_date()
        
        # Create an expander container to show information
        with st.expander(""):
            # Display a summary table
            st.write("Date Column")
            summary = st.session_state.date_column.get_summary()
            st.write(summary, use_container_width=True)

            # Display a Bar Chart using Altair chart
            st.write("Bar Chart")
            chart = st.session_state.date_column.set_barchart()
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)

            # Display the most frequent values
            st.write(" Most Frequent Values")
            frequent_values = st.session_state.date_column.set_frequent()
            st.write(frequent_values)