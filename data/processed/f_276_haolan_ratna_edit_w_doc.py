import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['Date', 'Value']

def f_174(df, plot=False):
    '''
    Splits a list in the 'Value' column of a DataFrame into several columns, scales these columns using StandardScaler, 
    and optionally returned the scaled data using a bar chart. The 'Date' column is converted to datetime and used as 
    the index in the plot.

    Parameters:
    df (DataFrame): A pandas DataFrame with a 'Date' column and a 'Value' column where 'Value' contains lists of numbers.
    plot (bool): If True, a bar chart of the scaled values is displayed. Defaults to False.

    Returns:
    DataFrame: A pandas DataFrame with the 'Date' column and additional columns for each element in the original 'Value' list,
               where these columns contain the scaled values.
    Axes (optional): A matplotlib Axes object containing the bar chart, returned if 'plot' is True.

    Note:
    - This function use "Scaled Values Over Time" for the plot title.
    - This function use "Date" and "Scaled Value" as the xlabel and ylabel respectively.

    Raises:
    - This function will raise KeyError if the DataFrame does not have the 'Date' and 'Value' columns.

    Requirements:
    - pandas
    - sklearn.preprocessing.StandardScaler
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=COLUMNS)
    >>> scaled_df, ax = f_174(df, plot=True)
    >>> print(scaled_df.shape)
    (2, 4)
    >>> plt.close()
    '''
    df['Date'] = pd.to_datetime(df['Date'])
    df = pd.concat([df['Date'], df['Value'].apply(pd.Series)], axis=1)
    
    scaler = StandardScaler()
    df.iloc[:,1:] = scaler.fit_transform(df.iloc[:,1:])
    
    if plot:
        plt.figure()
        ax = df.set_index('Date').plot(kind='bar', stacked=True)
        plt.title('Scaled Values Over Time')
        plt.xlabel('Date')
        plt.ylabel('Scaled Value')
        return df, ax

    
    return df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_normal_case(self):
        # Normal case with valid DataFrame
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result= f_174(df)
        self.assertEqual(result.shape, (2, 4))  # Checking if the DataFrame has the correct shape
        plt.close()
    def test_varying_length_lists(self):
        # DataFrame where 'Value' contains lists of varying lengths
        df = pd.DataFrame([['2021-01-01', [8, 10]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result = f_174(df)
        self.assertEqual(result.shape, (2, 4))  # The function should handle varying lengths
        plt.close()
    def test_varying_length_list_2(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result = f_174(df)
        self.assertEqual(result.empty, False)  
        plt.close()
    def test_missing_columns(self):
        # DataFrame missing 'Value' column
        df = pd.DataFrame([['2021-01-01'], ['2021-01-02']], columns=['Date'])
        with self.assertRaises(KeyError):
            f_174(df)  # Expecting a KeyError due to missing 'Value' column
        plt.close()
    def test_empty(self):
        df = pd.DataFrame()
        with self.assertRaises(KeyError):
            f_174(df)  
        plt.close()
    def test_plot_attributes(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        _, ax = f_174(df, True)
        self.assertEqual(ax.get_title(), 'Scaled Values Over Time')
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Scaled Value')
        plt.close()
    def test_plot_point(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result, ax = f_174(df, True)
        list_result = []
        for column in result:
            if column != "Date":
                columnSeriesObj = result[column]
                list_result.extend(columnSeriesObj.values)
        bar_heights = [rect.get_height() for rect in ax.patches]
        self.assertListEqual(bar_heights, list_result)
        plt.close()
