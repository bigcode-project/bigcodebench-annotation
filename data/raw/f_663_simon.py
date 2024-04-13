import pandas as pd
import pytz

def f_663(articles, timezone):
    """
    Analyze the publication times of a list of articles: 
    1) Convert 'published_time' to a specified timezone
    2) Group articles by 'category'
    3) For each category, calculate the count, mean, min, max publication times only considering the hour.

    Parameters:
    articles (list): A list of dictionaries where each dictionary represents 
    an article with keys 'title', 'title_url', 'id', 'category', and 'published_time' (in UTC).
    timezone (str): The string representation of the timezone to which the 'published_time' should be converted.

    Returns:
    DataFrame: A pandas DataFrame with the count, mean, min, max publication hour for each category.
               The category is the index of the DataFrame.

    Raises:
    ValueError: If dictionary keys do not match the requirements.
    TypeError: If articles is not a list of dictionaries. 
    ValueError: If an empty list is passed as articles.

    Requirements:
    - pandas
    - pytz

    Example:
    >>> articles = [{'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'Technology', 'published_time': datetime(2023, 6, 15, 12, 0, 0, tzinfo=pytz.UTC)},
    ...             {'title': 'New York Times', 'title_url': 'New_York_Times', 'id': 4, 'category': 'Sports', 'published_time': datetime(2023, 6, 16, 23, 0, 0, tzinfo=pytz.UTC)},
    ...             {'title': 'USA Today', 'title_url': 'USA_Today', 'id': 6, 'category': 'Health', 'published_time': datetime(2023, 6, 17, 7, 0, 0, tzinfo=pytz.UTC)}]
    >>> analysis_df = f_663(articles, 'America/New_York')
    >>> print(analysis_df)
                count  mean  min  max
    category                         
    Health          1   3.0    3    3
    Sports          1  19.0   19   19
    Technology      1   8.0    8    8

    >>> articles = [{'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'Technology', 'published_time': datetime(2023, 6, 15, 12, 0, 0, tzinfo=pytz.UTC)},
    ...             {'title': 'New York Times', 'title_url': 'New_York_Times', 'id': 4, 'category': 'Sports', 'published_time': datetime(2023, 6, 16, 23, 0, 0, tzinfo=pytz.UTC)},
    ...             {'title': 'USA Today', 'title_url': 'USA_Today', 'id': 6, 'category': 'Health', 'published_time': datetime(2023, 6, 17, 7, 0, 0, tzinfo=pytz.UTC)}]
    >>> analysis_df = f_663(articles, 'America/New_York')
    >>> print(analysis_df)
                count  mean  min  max
    category                         
    Health          1   3.0    3    3
    Sports          1  19.0   19   19
    Technology      1   8.0    8    8

    >>> articles = [
    ...    {'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'Technology', 'published_time': '09:01:04.403278+00:00'},
    ...    {'title': 'New York Times', 'title_url': 'New_York_Times', 'id': 4, 'category': 'Sports', 'published_time': '02:03:04.403278+00:00'},
    ...    {'title': 'USA Today', 'title_url': 'USA_Today', 'id': 6, 'category': 'Health', 'published_time': '21:11:01.403278+00:00'},
    ...    {'title': 'newsies', 'title_url': 'newsies.news', 'id': 21, 'category': 'Technology', 'published_time': '4:25:12.403278+00:00'},
    ...    {'title': 'ORF', 'title_url': 'orf.at', 'id': 44, 'category': 'Health', 'published_time': '03:04:03.403278+00:00'},
    ...    {'title': 'ARD', 'title_url': 'ard.com', 'id': 61, 'category': 'Health', 'published_time': '11:41:12.403278+00:00'}]
    >>> analysis_df = f_663(articles, 'America/New_York')
    >>> print(analysis_df)
                count       mean  min  max
    category                              
    Health          3  14.666667    6   22
    Sports          1  21.000000   21   21
    Technology      2  13.500000    4   23
    """

    if not isinstance(articles, list):
        raise TypeError("articles should be a list of dictionaries.")
    
    if not all(isinstance(item, dict) for item in articles):
        raise TypeError("articles should be a list of dictionaries.")

    
    if len(articles) == 0:
        raise ValueError("input articles list should contain at least one article.")

    if any(not sorted(dic.keys()) == ['category', 'id', 'published_time', 'title', 'title_url']  for dic in articles):
        raise ValueError("input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url', 'published_time'")


    tz = pytz.timezone(timezone)
    for article in articles:
        article['published_time'] = pd.to_datetime(article['published_time']).astimezone(tz)

    df = pd.DataFrame(articles)
    df['published_time'] = df['published_time'].dt.hour

    analysis_df = df.groupby('category')['published_time'].agg(['count', 'mean', 'min', 'max'])

    return analysis_df

import unittest
import pytz
import pandas as pd
from faker import Faker
import csv

fake = Faker()

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def generate_random_articles(self, n, seed):
        fake.seed_instance(seed=seed)
        categories = ['Sports', 'Technology', 'Health', 'Science', 'Business']
        articles = []
        for _ in range(n):
            article = {
                'title': fake.sentence(),
                'title_url': fake.url(),
                'id': fake.random_int(min=1, max=100),
                'category': fake.random_element(categories),
                'published_time': fake.date_time(tzinfo=pytz.UTC)
            }
            articles.append(article)
        return articles
    
    def test_wrong_input(self):
        self.assertRaises(Exception, f_663, [], 'UTC')
        self.assertRaises(Exception, f_663, [{}], 'UTC')
        self.assertRaises(Exception, f_663, [{'test': 2}], 'UTC')

    def test_case_1(self):
        'big dataset'
        with open('f_663_data_simon/test_data1.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            articles = list(reader)
        analysis_df = f_663(articles, 'America/New_York')

        excepted_df = pd.read_csv('f_663_data_simon/test_data1_result.csv', index_col='category')

        self.assertTrue(pd.testing.assert_frame_equal(analysis_df, excepted_df) is None)
        
    def test_case_2(self):
        'medium dataset'
        with open('f_663_data_simon/test_data2.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            articles = list(reader)
        analysis_df = f_663(articles, 'Europe/Vienna')

        excepted_df = pd.read_csv('f_663_data_simon/test_data2_result.csv', index_col='category')

        self.assertTrue(pd.testing.assert_frame_equal(analysis_df, excepted_df) is None)

    def test_case_3(self):
        'small dataset'
        with open('f_663_data_simon/test_data3.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            articles = list(reader)
        analysis_df = f_663(articles, 'Asia/Shanghai')

        excepted_df = pd.read_csv('f_663_data_simon/test_data3_result.csv', index_col='category')
        self.assertTrue(pd.testing.assert_frame_equal(analysis_df, excepted_df) is None)
        
    def test_case_5(self):
        'check general structure'
        articles = self.generate_random_articles(534, seed=11)
        analysis_df = f_663(articles, 'Africa/Cairo')
        self.assertTrue(set(analysis_df.index).issubset(['Sports', 'Technology', 'Health', 'Science', 'Business']))
        self.assertIn('count', analysis_df.columns)
        self.assertIn('mean', analysis_df.columns)
        self.assertIn('min', analysis_df.columns)
        self.assertIn('max', analysis_df.columns)
if __name__ == "__main__":
    run_tests()