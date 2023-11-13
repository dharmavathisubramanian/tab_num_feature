import pandas as pd
import altair as alt
pd.set_option('display.max_colwidth', None)
class DateColumn:
    """
    --------------------
    Description
    --------------------
    -> DateColumn (class): Class that manages a column from a dataframe of datetime data type

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (optional)
    -> df (pd.Dataframe): Pandas dataframe (optional)
    -> cols_list (list): List of columns names of dataset that are text type (default set to empty list)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (default set to None)
    -> n_unique (int): Number of unique value of a serie (optional)
    -> n_missing (int): Number of missing values of a serie (optional)
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> n_weekend (int): Number of times a serie has dates falling during weekend (optional)
    -> n_weekday (int): Number of times a serie has dates not falling during weekend (optional)
    -> n_future (int): Number of times a serie has dates falling in the future (optional)
    -> n_empty_1900 (int): Number of times a serie has dates equal to '1900-01-01' (optional)
    -> n_empty_1970 (int): Number of times a serie has dates equal to '1970-01-01' (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Dataframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = df
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.col_min = None
        self.col_max = None
        self.n_weekend = None
        self.n_weekday = None
        self.n_future = None
        self.n_empty_1900 = None
        self.n_empty_1970 = None
        self.barchart = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])
    
    def find_date_cols(self):
        """
        --------------------
        Description
        --------------------
        -> find_date_cols (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.
        Then it will find all columns of datetime data type. If it can't find any datetime then it will look for all columns of text time. Then it will store the results in the relevant attribute (self.cols_list).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """ 
        if self.file_path is not None:
            if self.df is None:
                # Load the CSV file as a DataFrame if it hasn't been provided
                self.df = pd.read_csv(self.file_path)

            # Find columns with datetime data type
            date_cols = self.df.select_dtypes(include=['datetime64']).columns

            if not date_cols.empty:
                self.cols_list = date_cols.tolist()
            else:
                # If no datetime columns found, look for text columns that may contain date/time information
                text_date_cols = self.df.select_dtypes(include=['object']).columns
                self.cols_list = text_date_cols.tolist()
        else:
            # Handle the case where file_path is None
            raise ValueError("Please upload a CSV.")


    def set_data(self, col_name):
        """
        --------------------
        Description
        --------------------
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that sets the self.serie attribute with the relevant column from the dataframe and then computes all requested information from self.serie to be displayed in the Date section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> col_name (str): Name of the text column to be analysed

        --------------------
        Returns
        --------------------
        -> None
        
        """
        # Check if the column name exists in the DataFrame
        if col_name not in self.df.columns:
            raise ValueError(f"Column '{col_name}' not found in the DataFrame.")
        
        # Set self.serie to the specified column
        self.serie = self.df[col_name]
        

    def convert_serie_to_date(self):
        """
        --------------------
        Description
        --------------------
        -> convert_serie_to_date (method): Class method that convert a Pandas Series to datetime data type and store the results in the relevant attribute (self.serie).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None and not self.serie.empty:
            try:
                # Attempt to convert the Series to datetime
                self.serie = pd.to_datetime(self.serie, format='mixed', dayfirst=True)
            except (ValueError, pd.errors.OutOfBoundsDatetime) as e:
                # Raise a custom exception with a descriptive error message
                raise ValueError(f"Failed to convert the series to datetime: {e}")
        else:
            print("The series is None or empty. Nothing to convert.")
        
    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if the serie is empty or not

        """
        return self.serie is None or self.serie.empty
        

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie and store the results in the relevant attribute(self.n_unique).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        # Check if the series is not empty
        if not self.is_serie_none():
            # Calculate the number of unique values in the series
            number_unique = self.serie.nunique()
            self.n_unique = number_unique
            return self.n_unique
        

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie and store the results in the relevant attribute(self.n_missing).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            # Replace "NA" with NaN in the datetime column
            self.serie = self.serie.replace("NA", pd.NA)
            # Calculate the number of missing values in the series
            number_missing = self.serie.isna().sum()
            if number_missing == 0:
                self.n_missing = None
            else:
                self.n_missing = number_missing
            return self.n_missing
        

    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie and store the results in the relevant attribute(self.col_min).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            # Calculate the minimum value in the series
            min_value = self.serie.min()
            self.col_min = min_value
            return self.col_min
        

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the minimum value of a serie and store the results in the relevant attribute(self.col_max).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            # Calculate the minimum value in the series
            max_value = self.serie.max()
            self.col_max = max_value
            return self.col_max
        

    def set_weekend(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekend (method): Class method that computes the number of times a serie has dates falling during weekend and store the results in the relevant attribute(self.n_weekend).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            # Count the number of times dates fall during weekends
            number_weekend = self.serie.dt.dayofweek.isin([5, 6]).sum()
            if number_weekend == 0:
                self.n_weekend = None
            else:
                self.n_weekend = number_weekend
            return self.n_weekend
        

    def set_weekday(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekday (method): Class method that computes the number of times a serie has dates not falling during weekend and store the results in the relevant attribute(self.n_weekday).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            # Count the number of times dates do not fall during weekends
            number_weekday = (~self.serie.dt.dayofweek.isin([5, 6])).sum()
            if number_weekday == 0:
                self.n_weekday = None
            else:
                self.n_weekday = number_weekday
            return self.n_weekday
        

    def set_future(self):
        """
        --------------------
        Description
        --------------------
        -> set_future (method): Class method that computes the number of times a serie has dates falling in the future and store the results in the relevant attribute(self.n_future).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            # Get the current date
            current_date = pd.to_datetime('now').normalize()
            # Count the number of times dates fall in the future
            number_future = (self.serie > current_date).sum()
            if number_future == 0:
                self.n_future = None
            else:
                self.n_future = number_future
            return self.n_future
        
    
    def set_empty_1900(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1900 (method): Class method that computes the number of times a serie has dates equal to '1900-01-01' and store the results in the relevant attribute(self.n_empty_1900).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        # Count the number of times dates are equal to '1900-01-01'
        number_empty_1900 = (self.serie == pd.to_datetime('1900-01-01')).sum()
        if number_empty_1900 == 0:
            self.n_weekend = None
        else:
            self.n_empty_1900 = number_empty_1900
        return self.n_empty_1900
        

    def set_empty_1970(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1970 (method): Class method that computes the number of times a serie has only digit characters and store the results in the relevant attribute(self.n_empty_1970).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            # Count the number of times dates are equal to '1970-01-01'
            number_empty_1970 = (self.serie == pd.to_datetime('1970-01-01')).sum()
            if number_empty_1970 == 0:
                self.n_empty_1970 = None
            else:
                self.n_empty_1970 = number_empty_1970
            return self.n_empty_1970
        
        

    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie and store the results in the relevant attribute(self.barchart).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            # Extract the year from the datetime values
            years = self.serie.dt.year
            # Compute value counts for the series
            year_counts = years.value_counts().reset_index()
            year_counts.columns = ['year', 'count']
            
            # Create a barchart using Altair
            barchart = alt.Chart(year_counts)
            barchart = barchart.mark_bar()
            barchart = barchart.encode(
                x=alt.X('year:O', title='Date', axis=alt.Axis(labelAngle=0)),
                y=alt.Y('count:Q', title='Count of Records')
            )
            # Store the Altair chart in the self.barchart attribute
            self.barchart = barchart
            return self.barchart
        
      
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie and store the results in the relevant attribute(self.frequent).

        --------------------
        Parameters
        --------------------
        -> end (int):
            Parameter indicating the maximum number of values to be displayed

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            # Calculate the value counts of the series
            serie_counts = self.serie.value_counts()
            # Create a DataFrame to store the results
            self.frequent = pd.DataFrame({'value': serie_counts.index, 'occurrence': serie_counts.values})
        
            # Calculate the percentage frequency
            total_occurrences = self.frequent['occurrence'].sum()
            self.frequent['percentage'] = (self.frequent['occurrence'] / total_occurrences).round(4)
        
            # Sort the DataFrame by occurrence in descending order
            self.frequent = self.frequent.sort_values(by='occurrence', ascending=False)
        
            # Display the top 'end' most frequent values
            self.frequent = self.frequent.head(end)
            return self.frequent
        

    def get_summary(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
        if self.serie is not None:
            # Create a summary Dictionary
            summary_data = {
                "Number of Unique Values": [self.set_unique()],
                "Number of Rows with Missing Values": [self.set_missing()],
                "Number of Weekend Dates": [self.set_weekend()],
                "Number of Weekday Dates": [self.set_weekday()],
                "Number of Dates in Future": [self.set_future()],
                "Number of Rows with 1900-01-01": [self.set_empty_1900()],
                "Number of Rows with 1970-01-01": [self.set_empty_1970()],
                "Minimum Value": [str(self.set_min())],
                "Maximum Value": [str(self.set_max())],
            }

            summary_table = pd.DataFrame(summary_data).T.reset_index()
            summary_table.columns = ["Description", "Value"]
            summary_table["Value"] = summary_table["Value"].astype(str)
            return summary_table