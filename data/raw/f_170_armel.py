import bs4
import pandas as pd
import matplotlib.pyplot as plt

def f_170(html_content):
    """
    Process the content of an html string to extract rows of data from table rows (<tr>) and columns (<td>), and organizes the extracted data into a pandas DataFrame.
    - Make sure to only consider the rows with at least 2 columns.
    - Make a bar plot of the number of occurrences of each unique elemnt of the second column of the dataframe.
    - If the dataframe is empty, the plot should be empty as well.
        - The plot title should be 'Frequency Distribution', the xlabel 'Values' and the ylabel 'Frequency'.

    Parameters:
    - html_content (str): String which represnts the HTML content of a webpage

    Requirements:
    - bs4
    - pandas
    
    Returns:
    - pandas.DataFrame: A pandas DataFrame containing the extracted data.
    - matplotlib.axes._axes.Axes: Barplot of the number of occurrences of the second column of the dataframe.
    
    Example:
    >>> ax = f_170(html_content)
    >>> print(type(ax))
    
    Note: 
    """
    soup = bs4.BeautifulSoup(html_content, 'html.parser')

    data = []
    rows = soup.find_all('tr')
    for row in rows[1:]:  # Ignoring the header row
        cols = row.find_all('td')
        # Ensuring the row has at least two columns before processing
        if cols and len(cols) > 1:
            data.append([element.text.strip() for element in cols])
    
    if rows:
        headers = [element.text.strip() for element in rows[0].find_all('th')]
        df = pd.DataFrame(data, columns=headers)
    else :
        df = pd.DataFrame(data)
    # If DataFrame is empty or doesn't have a second column, return an empty plot
    if df.empty or len(df.columns) < 2:
        fig, ax = plt.subplots()
    else :
        ax = df.iloc[:, 1].value_counts().plot(kind='bar')
    ax.set_title("Frequency Distribution")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    
    return df, ax

import unittest

class TestCases(unittest.TestCase):
    """Test cases for f_170."""
    @staticmethod
    def is_barplot(ax, expected_values, expected_categories):
        extracted_values = [bar.get_height() for bar in ax.patches] # extract bar height
        extracted_categories = [tick.get_text() for tick in ax.get_xticklabels()] # extract category label

        for actual_value, expected_value in zip(extracted_values, expected_values):
            assert actual_value == expected_value, f"Expected value '{expected_value}', but got '{actual_value}'"

        for actual_category, expected_category in zip(extracted_categories, expected_categories):
            assert actual_category == expected_category, f"Expected category '{expected_category}', but got '{actual_category}'"
    
    def test_case_1(self):
        html_1 = """
            <html>
            <body>
                <table id="table0">
                    <tr><th>Name</th><th>Age</th></tr>
                    <tr><td>Alice</td><td>25</td></tr>
                    <tr><td>Bob</td><td>30</td></tr>
                    <tr><td>Robert</td><td>30</td></tr>
                    <tr><td>Tania</td><td>30</td></tr>
                    <tr><td>Terry</td><td>10</td></tr>
                </table>
            </body>
            </html>
        """
        df, ax = f_170(html_1)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass
        # Assertions
        self.assertEqual(len(ax.patches), 3)
        self.assertEqual(ax.get_title(), 'Frequency Distribution')
        self.assertEqual(ax.get_xlabel(), 'Values')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
    
    def test_case_2(self):
        html_2 = """
            <html>
            <body>
                <table id="table0">
                    <tr><th>Name</th><th>Age</th></tr>
                    <tr><td>Alice</td><td>25</td></tr>
                    <tr><td>Bob</td><td>30</td></tr>
                </table>
            </body>
            </html>
        """
        df, ax = f_170(html_2)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass   
        # Assertions
        self.assertListEqual(df.columns.tolist(), ["Name", "Age"])
        df["Age"] = df["Age"].astype("int64")
        pd.testing.assert_frame_equal(
            df,
            pd.DataFrame(
                {
                    "Name" : ["Alice", "Bob"],
                    "Age": [25, 30]
                }
            )
        )
        self.assertEqual(len(ax.patches), 2)
        self.assertEqual(ax.get_title(), 'Frequency Distribution')
        self.assertEqual(ax.get_xlabel(), 'Values')
        self.assertEqual(ax.get_ylabel(), 'Frequency')

    def test_case_3(self):
        html_3 = '''
        <html>
            <body>
                <p>No table data here.</p>
            </body>
        </html>
        '''
        df, ax = f_170(html_3)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass
        # Assertions
        self.assertEqual(len(ax.patches), 0)  # No bars should be plotted

    def test_case_4(self):
        html_4 = """
            <html>
            <body>
                <table id="table0">
                    <tr><th>Name</th><th>Age</th></tr>
                    <tr><td>Alice</td><td>25</td></tr>
                    <tr><td>Bob</td><td>30</td></tr>
                    <tr><td>Bobby</td><td>39</td></tr>
                </table>
            </body>
            </html>
        """
        df, ax = f_170(html_4)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass  
        # Assertions
        self.assertEqual(len(ax.patches), 3)
        self.assertEqual(ax.get_title(), 'Frequency Distribution')
        self.assertEqual(ax.get_xlabel(), 'Values')
        self.assertEqual(ax.get_ylabel(), 'Frequency')

    def test_case_5(self):
        html_5 = """
            <html>
            <body>
                <table id="table0">
                    <tr><th>Name</th><th>Age</th><th>Height</th></tr>
                    <tr><td>Alice</td><td>25</td><td>180</td></tr>
                    <tr><td>Bob</td><td>30</td><td>173</td></tr>
                    <tr><td>Arthur</td><td>33</td><td>173</td></tr>
                    <tr><td>Albert</td><td>13</td><td>153</td></tr>
                </table>
            </body>
            </html>
        """
        df, ax = f_170(html_5)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass
        # Assertions
        self.assertEqual(len(ax.patches), 4)
        self.assertEqual(ax.get_title(), 'Frequency Distribution')
        self.assertEqual(ax.get_xlabel(), 'Values')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
        self.is_barplot(ax, [1, 1, 1, 1], ["25", "30", "33", "13"])

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()