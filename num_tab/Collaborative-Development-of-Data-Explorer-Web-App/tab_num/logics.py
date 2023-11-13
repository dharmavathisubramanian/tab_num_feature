import pandas as pd
import altair as alt


class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column of numeric data type

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (optional)
    -> df (pd.Dataframe): Pandas dataframe (optional)
    -> cols_list (list): List of columns names of dataset that are numeric type (default set to empty list)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (default set to None)
    -> n_unique (int): Number of unique value of a serie (default set to None)
    -> n_missing (int): Number of missing values of a serie (default set to None)
    -> col_mean (int): Average value of a serie (default set to None)
    -> col_std (int): Standard deviation value of a serie (default set to None)
    -> col_min (int): Minimum value of a serie (default set to None)
    -> col_max (int): Maximum value of a serie (default set to None)
    -> col_median (int): Median value of a serie (default set to None)
    -> n_zeros (int): Number of times a serie has values equal to 0 (default set to None)
    -> n_negatives (int): Number of times a serie has negative values (default set to None)
    -> histogram (alt.Chart): Altair histogram displaying the count for each bin value of a serie (default set to empty)
    -> frequent (pd.DataFrame): Datframe containing the most frequest value of a serie (default set to empty)

    """
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = df
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.col_mean = None
        self.col_std = None
        self.col_min = None
        self.col_max = None
        self.col_median = None
        self.n_zeros = None
        self.n_negatives = None
        self.histogram = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])

    def find_num_cols(self):
        try:
            numeric_cols = self.df.select_dtypes(include='number')

            if not numeric_cols.empty:
                self.cols_list = numeric_cols.columns
            else:
                self.df = pd.DataFrame()

        except pd.errors.EmptyDataError:
            self.df = pd.DataFrame()
        """
        --------------------
        Description
        --------------------
        -> find_num_cols (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.
        Then it will find all columns of numeric data type and store the results in the relevant attribute (self.cols_list).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_data(self, col_name):
        if col_name is not None:
            self.serie = self.df[col_name]
            self.set_unique()
            self.set_missing()
            self.set_zeros()
            self.set_negatives()
            self.set_mean()
            self.set_std()
            self.set_min()
            self.set_max()
            self.set_median()
        else:
            self.serie = pd.Series(dtype='object')
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that sets the self.serie attribute with the relevant column from the dataframe and then computes all requested information from self.serie to be displayed in the Numeric section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> col_name (str): Name of the numeric column to be analysed

        --------------------
        Returns
        --------------------
        -> None

        """

    def convert_serie_to_num(self):
        
        """
        --------------------
        Description
        --------------------
        -> convert_serie_to_num (method): Class method that convert a Pandas Series to numeric data type and store the results in the relevant attribute (self.serie).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.serie = pd.to_numeric(self.serie)

    def is_serie_none(self):
        
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none and store the results in the relevant attribute (self.cols_list) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if the serie is empty or not

        """
        if self.serie is not None and not self.serie.empty:
            self.cols_list = self.serie.tolist()

    def set_unique(self):
        
        
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a column and store the results in the relevant attribute (self.n_unique) if self.serie is not empty nor None

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
            self.n_unique = self.serie.nunique()

    def set_missing(self):
                
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie and store the results in the relevant attribute (self.n_missing) if self.serie is not empty nor None

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
            self.n_missing = self.serie.isna().sum()

    def set_zeros(self):
               
        
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that computes the number of times a serie has values equal to 0 and store the results in the relevant attribute (self.n_zeros) if self.serie is not empty nor None

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
            self.n_zeros = (self.serie == 0).sum() 

    def set_negatives(self):
        
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that computes the number of times a serie has negative values and store the results in the relevant attribute (self.n_negatives) if self.serie is not empty nor None

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
            self.n_negatives = (self.serie < 0).sum()

    def set_mean(self):
        
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that computes the average value of a serie and store the results in the relevant attribute (self.col_mean) if self.serie is not empty nor None

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
            self.col_mean = self.serie.mean()

    def set_std(self):
         if self.serie is not None and not self.serie.empty:
            self.col_std = self.serie.std()       
    """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that computes the standard deviation value of a serie and store the results in the relevant attribute (self.col_std) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        
    
    def set_min(self):
         if self.serie is not None and not self.serie.empty:
            self.col_min = self.serie.min()

    """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie and store the results in the relevant attribute (self.col_min) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_max(self):
         if self.serie is not None and not self.serie.empty:
            self.col_max = self.serie.max()
    """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie and store the results in the relevant attribute (self.col_max) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_median(self):
         if self.serie is not None and not self.serie.empty:
            self.col_median = self.serie.median()
    """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that computes the median value of a serie and store the results in the relevant attribute (self.col_median) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_histogram(self):
        if self.serie is not None and not self.serie.empty:
            chart = alt.Chart(self.df).mark_bar().encode(
                alt.X('{}'.format(self.serie.name), bin=alt.Bin(maxbins=20)),
                alt.Y('count()')
            ).properties(
                title="Histogram"
            )
            self.histogram = chart
    
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that computes the Altair histogram displaying the count for each bin value of a serie and store the results in the relevant attribute (self.histogram) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_frequent(self, end=20):
        if self.serie is not None and not self.serie.empty:
            frequent_values = self.serie.value_counts().reset_index()
            frequent_values.columns = ['value', 'frequency']
            frequent_values['percentage'] = (frequent_values['frequency'] / len(self.serie)) * 100
            if end is not None:
                frequent_values = frequent_values.head(end)
            frequent_values.rename(columns={'frequency': 'occurrence'}, inplace=True)

            self.frequent = frequent_values
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie and store the results in the relevant attribute (self.frequent) if self.serie is not empty nor None

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
        
    def get_summary(self):
        return [
                {"Description": "Number of Unique Values", "Value": str(self.n_unique)},
                {"Description": "Number of Rows with Missing Values", "Value": str(self.n_missing)},
                {"Description": "Number of Rows with 0", "Value": str(self.n_zeros)},
                {"Description": "Number of Rows with Negative Values", "Value": str(self.n_negatives)},                        
                {"Description": "Average Value", "Value": self.col_mean},
                {"Description": "Standard Deviation Value", "Value": self.col_std},
                {"Description": "Minimum Value", "Value": self.col_min},
                {"Description": "Maximum Value", "Value": self.col_max},
                {"Description": "Median Value", "Value": self.col_median}
 
        ]
 
        
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
        