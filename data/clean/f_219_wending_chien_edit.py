import re
import matplotlib.pyplot as plt


def f_219(df):
    """
    Analyzes a DataFrame to find videos with titles containing "how" or "what" and visualizes their like ratios.
    The like ratio for each video is calculated by dividing the number of likes by the number of views.
    This function generates a bar plot of the like ratios for these specific videos.
    If the DataFrame is empty, lacks the required columns, or contains no titles matching the criteria,
    an empty subplot is returned.

    Parameters:
    df (DataFrame): A DataFrame containing video data with columns 'Title', 'Views', and 'Likes'.

    Returns:
    Axes: A matplotlib.axes.Axes object of the bar plot. The plot will be empty if the DataFrame is insufficient
    or no video titles match the search criteria.

    Requirements:
    - re
    - matplotlib

    Note:
    The function checks for the presence of the necessary data columns ('Title', 'Views', 'Likes') and whether
    there are any entries matching the search criteria. If these conditions are not met, it returns an empty plot.

    Example:
    >>> import pandas as pd
    >>> data = {'Title': ['How to code', 'What is Python', 'Tutorial'], 'Views': [1500, 1200, 1000], 'Likes': [150, 300, 100]}
    >>> df = pd.DataFrame(data)
    >>> ax = f_219(df)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    if df.empty or 'Likes' not in df.columns or 'Views' not in df.columns or 'Title' not in df.columns:
        fig, ax = plt.subplots()
        return ax

    pattern = re.compile(r'(how|what)', re.IGNORECASE)
    interesting_videos = df[df['Title'].apply(lambda x: bool(pattern.search(x)))]

    if interesting_videos.empty:
        fig, ax = plt.subplots()
        return ax

    interesting_videos = interesting_videos.copy()  # Create a copy to avoid modifying the input df
    interesting_videos['Like Ratio'] = interesting_videos['Likes'] / interesting_videos['Views']

    ax = interesting_videos.plot(kind='bar', x='Title', y='Like Ratio', legend=False)
    ax.set_ylabel('Like Ratio')
    ax.set_xticklabels(interesting_videos['Title'], rotation='vertical')

    return ax


# Integrating the test_cases function into the TestCases class methods and running the tests

import pandas as pd
import unittest
import matplotlib

matplotlib.use('Agg')


def run_tests():
    """
    Execute the test cases for function f_218.
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        data_1 = pd.DataFrame({
            'Title': ['How to code?', 'What is Python?', 'The art of programming', 'How to cook?', 'What is life?'],
            'Views': [1000, 500, 200, 300, 800],
            'Likes': [500, 250, 100, 150, 600]
        })

        ax = f_219(data_1)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")
        y_data = [rect.get_height() for rect in ax.patches]
        expected_y_data = [0.5, 0.5, 0.5, 0.75]
        self.assertEqual(y_data, expected_y_data, f"Expected {expected_y_data}, but got {y_data}")

    def test_case_2(self):
        data_2 = pd.DataFrame({
            'Title': ['How to swim?', 'What is Java?', 'The beauty of nature', 'How to paint?', 'What is art?'],
            'Views': [1200, 400, 250, 350, 900],
            'Likes': [600, 200, 125, 175, 450]
        })

        ax = f_219(data_2)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")
        y_data = [rect.get_height() for rect in ax.patches]
        expected_y_data = [0.5, 0.5, 0.5, 0.5]
        self.assertEqual(y_data, expected_y_data, f"Expected {expected_y_data}, but got {y_data}")

    def test_case_3(self):
        data_3 = pd.DataFrame({
            'Title': [],
            'Views': [],
            'Likes': []
        })

        ax = f_219(data_3)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")

    def test_case_4(self):
        data_4 = pd.DataFrame({
            'Title': ['Learning to code', 'Python basics', 'Advanced programming', 'Cooking basics',
                      'Life and philosophy'],
            'Views': [1100, 450, 220, 320, 850],
            'Likes': [550, 225, 110, 160, 425]
        })

        ax = f_219(data_4)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")

    def test_case_5(self):
        data_5 = pd.DataFrame({
            'Title': ['How to sing?', 'What is C++?', 'The mysteries of the universe', 'How to dance?',
                      'What is time?'],
            'Views': [1300, 420, 270, 370, 950],
            'Likes': [650, 210, 135, 185, 475]
        })

        ax = f_219(data_5)
        self.assertIsInstance(ax, matplotlib.axes.Axes, "The returned object should be of type Axes.")
        y_data = [rect.get_height() for rect in ax.patches]
        expected_y_data = [0.5, 0.5, 0.5, 0.5]
        self.assertEqual(y_data, expected_y_data, f"Expected {expected_y_data}, but got {y_data}")


if __name__ == "__main__":
    run_tests()
