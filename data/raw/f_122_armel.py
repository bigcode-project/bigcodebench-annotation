import pandas as pd

def f_122(df: pd.DataFrame, population: int, gdp: int):
    """
    Filters the input DataFrame based on given population and GDP thresholds and returns the selected rows and their correlation matrix.

    Parameters:
    - df (pd.DataFrame): A DataFrame containing columns 'Country', 'Population', and 'GDP'.
    - population (int): The threshold for the 'Population' column.
    - gdp (int): The threshold for the 'GDP' column.

    Returns:
    - selected_df (pd.DataFrame): A DataFrame containing rows where both 'Population' > population and 'GDP' > gdp.
    - corr_matrix (pd.DataFrame): A correlation matrix of the 'Population' and 'GDP' columns of the selected_df.

    Requirements:
    - pandas

    Example:
    >>> df = pd.DataFrame({
        'Country': ['A', 'B', 'C', 'D'],
        'Population': [45, 55, 70, 85],
        'GDP': [65, 75, 55, 90]
    })
    >>> f_122(df, 50, 70)
    (   Country  Population  GDP
    3       D          85   90,             Population       GDP
    Population    1.000000  1.000000
    GDP          1.000000  1.000000)
    """
    selected_df = df[(df['Population'] > population) & (df['GDP'] > gdp)]
    corr_matrix = selected_df.corr()
    return selected_df, corr_matrix

import unittest
import random

class TestCases(unittest.TestCase):
    """Test cases for the f_122 function."""
    def test_case_1(self):
        random.seed(42)
        df = pd.DataFrame({'Country': ['New Zealand', 'French Polynesia', 'Ethiopia', 'Singapore', 'Guinea-Bissau', 'Iran', 'Romania', 'Honduras', 'French Polynesia', 'Pakistan', 'Senegal', 'Saudi Arabia', 'Netherlands Antilles', 'Greenland', 'Turks and Caicos Islands', 'Tanzania', 'Faroe Islands', 'Montenegro', 'Libyan Arab Jamahiriya', "Cote d'Ivoire", 'Luxembourg', 'Dominica', 'Heard Island and McDonald Islands', 'Korea', 'Macedonia', 'Canada', 'Bolivia', 'Cocos (Keeling) Islands', 'Bouvet Island (Bouvetoya)', 'United States Virgin Islands', 'Guinea', 'Eritrea', 'Falkland Islands (Malvinas)', 'Singapore', 'Nigeria', 'Latvia', 'Aruba', 'Madagascar', 'Kuwait', 'Benin', 'Bouvet Island (Bouvetoya)', 'Somalia', 'Mexico', 'Latvia', 'Chad', 'El Salvador', 'Saint Helena', 'Sao Tome and Principe', 'Saint Kitts and Nevis', 'Maldives'], 'Population': [41, 132, 61, 91, 146, 32, 106, 18, 71, 90, 140, 118, 40, 57, 18, 34, 81, 23, 142, 139, 68, 115, 82, 125, 52, 93, 128, 104, 53, 39, 27, 61, 120, 81, 70, 116, 120, 32, 51, 58, 63, 77, 52, 74, 56, 71, 115, 68, 118, 127], 'GDP': [130, 132, 125, 104, 31, 115, 23, 58, 39, 143, 86, 88, 81, 68, 120, 54, 15, 130, 97, 127, 31, 90, 138, 130, 103, 96, 123, 99, 85, 138, 120, 69, 87, 62, 92, 80, 87, 29, 26, 64, 25, 148, 140, 80, 50, 137, 134, 19, 92, 140]})
        population_threshold = random.randint(10, 150)
        gdp_threshold = random.randint(10, 150)
        selected_df, corr_matrix = f_122(df, population_threshold, gdp_threshold)
        
        # Assert that the selected_df has correct rows based on the thresholds
        self.assertTrue(all(selected_df['Population'] > population_threshold))
        self.assertTrue(all(selected_df['GDP'] > gdp_threshold))
        
        # Assert corr_matrix is correctly computed
        self.assertEqual(corr_matrix.shape, (2, 2))
        self.assertIn('Population', corr_matrix.columns)
        self.assertIn('GDP', corr_matrix.columns)

    def test_case_2(self):
        random.seed(42)
        df = pd.DataFrame({'Country': ['Latvia', 'China', 'Somalia', 'Ukraine', 'Norfolk Island', 'Guinea', 'Turkmenistan', 'Mali', 'Nicaragua', 'Poland', 'Mongolia', 'Grenada', 'Northern Mariana Islands', 'Cook Islands', 'Dominican Republic', 'Slovenia', 'India', 'Dominican Republic', 'Guatemala', 'Gibraltar', 'French Southern Territories', 'Kuwait', 'Denmark', 'Saint Lucia', 'India', 'Sao Tome and Principe', 'Venezuela', 'Haiti', 'Iceland', 'Martinique', 'Andorra', 'Saint Kitts and Nevis', 'El Salvador', 'Isle of Man', 'British Indian Ocean Territory (Chagos Archipelago)', 'Chile', 'Oman', 'Poland', 'Solomon Islands', 'Togo', 'Uganda', 'Malta', 'Oman', 'Zambia', 'Argentina', 'Svalbard & Jan Mayen Islands', 'Myanmar', 'Guernsey', 'Brunei Darussalam', 'Palau', 'Aruba', 'Poland', 'French Guiana', 'Bolivia', 'Afghanistan', 'Mongolia', 'Samoa', 'Iceland', 'Georgia', 'Qatar', 'Belize', 'Moldova', 'Trinidad and Tobago', 'Thailand', 'Trinidad and Tobago', 'American Samoa', 'Denmark', 'United Kingdom', 'Korea', 'Macao', 'Gambia', 'Guadeloupe', 'Bangladesh', 'Israel', 'Iran', 'France', 'Haiti', 'Turkey', 'Reunion', 'Suriname', 'Bahrain', 'Timor-Leste', 'Tajikistan', 'Japan', 'Greece', 'Niue', 'Macao', 'United States of America', 'Belgium', 'Mongolia', 'Equatorial Guinea', 'Vietnam', 'Nigeria', 'Saint Vincent and the Grenadines', 'Guinea-Bissau', 'Seychelles', 'United Arab Emirates', 'Georgia', 'Tunisia', 'Tonga'], 'Population': [95, 52, 57, 61, 107, 103, 19, 99, 103, 119, 101, 30, 117, 91, 144, 44, 55, 121, 133, 60, 145, 78, 144, 43, 138, 132, 148, 113, 14, 67, 140, 127, 60, 23, 135, 112, 84, 91, 29, 89, 25, 140, 116, 65, 12, 115, 94, 12, 130, 131, 34, 55, 60, 146, 149, 92, 81, 127, 43, 50, 79, 144, 20, 147, 91, 64, 94, 32, 41, 52, 104, 98, 50, 32, 110, 55, 147, 47, 109, 145, 142, 30, 30, 29, 140, 57, 86, 97, 15, 54, 78, 37, 81, 75, 89, 137, 133, 29, 76, 59], 'GDP': [37, 86, 21, 51, 94, 72, 128, 74, 128, 100, 11, 42, 125, 129, 34, 105, 95, 47, 88, 115, 64, 118, 39, 47, 141, 53, 144, 21, 108, 143, 39, 16, 48, 90, 92, 61, 11, 95, 143, 37, 97, 135, 21, 118, 10, 123, 88, 42, 127, 107, 139, 64, 52, 149, 15, 26, 116, 49, 87, 96, 30, 94, 49, 58, 53, 68, 111, 80, 47, 17, 108, 45, 49, 33, 86, 107, 88, 48, 46, 150, 67, 129, 63, 16, 114, 37, 118, 112, 89, 110, 34, 50, 104, 89, 119, 62, 126, 128, 18, 93]})
        population_threshold = random.randint(10, 150)
        gdp_threshold = random.randint(10, 150)
        selected_df, corr_matrix = f_122(df, population_threshold, gdp_threshold)
        
        # Assert that the selected_df has correct rows based on the thresholds
        self.assertTrue(all(selected_df['Population'] > population_threshold))
        self.assertTrue(all(selected_df['GDP'] > gdp_threshold))
        
        # Assert corr_matrix is correctly computed
        self.assertEqual(corr_matrix.shape, (2, 2))
        self.assertIn('Population', corr_matrix.columns)
        self.assertIn('GDP', corr_matrix.columns)

    def test_case_3(self):
        random.seed(42)
        df = pd.DataFrame({'Country': ['Kuwait', 'Maldives', 'Switzerland', 'Namibia', 'Austria', 'Bolivia', 'Turkey', 'Jersey', 'Bermuda', 'Saint Barthelemy', 'Venezuela', 'Angola', 'Heard Island and McDonald Islands', 'Kazakhstan', 'Belize', 'Haiti', 'Antarctica (the territory South of 60 deg S)', 'Comoros', 'Montenegro', 'Mongolia', 'United Kingdom', 'Kiribati', 'Jamaica', 'Mayotte', 'Saint Vincent and the Grenadines', 'Tokelau', 'Fiji', 'Liechtenstein', 'China', 'Namibia', 'Tuvalu', 'Djibouti', 'Mauritius', 'Burundi', 'Namibia', 'Mozambique', 'Kenya', 'Czech Republic', 'Jersey', 'Afghanistan', 'United Arab Emirates', 'Costa Rica', 'Croatia', 'Samoa', 'Guyana', 'Costa Rica', 'Tonga', 'Gabon', 'Gibraltar', 'Mauritius', 'Niue', 'United States Virgin Islands', 'Micronesia', 'Spain', 'Niger', 'Burkina Faso', 'Thailand', 'Suriname', 'Norfolk Island', 'Belarus', 'French Polynesia', 'Tonga', 'Haiti', 'Macedonia', 'Swaziland', 'Saint Martin', 'Ghana', 'Tuvalu', 'Paraguay', 'Singapore', 'Indonesia', 'Malta', 'Congo', 'Grenada', 'Japan', 'Libyan Arab Jamahiriya', 'Mozambique', 'France', 'Mozambique', 'Nepal', 'Colombia', 'Senegal', 'Morocco', 'Swaziland', 'Chile', 'Swaziland', 'Lebanon', 'Serbia', 'Dominica', 'Pitcairn Islands', 'Libyan Arab Jamahiriya', 'Benin', 'Niue', 'Nicaragua', 'Kyrgyz Republic', 'Liberia', 'Iran', 'United Arab Emirates', 'Dominican Republic', 'Rwanda', 'Palau', 'Bouvet Island (Bouvetoya)', 'Svalbard & Jan Mayen Islands', 'Hungary', 'Brazil', 'Turkmenistan', 'Guernsey', 'Qatar', 'Falkland Islands (Malvinas)', 'Turkmenistan', 'Chile', 'Nauru', 'Slovakia (Slovak Republic)', 'Aruba', 'Reunion', 'Kuwait', 'Congo', 'French Guiana', 'Eritrea', 'Ethiopia', 'Christmas Island', 'Oman', 'Trinidad and Tobago', 'Cameroon', 'United Arab Emirates', 'Guadeloupe', 'Slovenia', 'Vietnam', 'Greenland', 'France', 'Djibouti', 'Bulgaria', 'Puerto Rico', 'Equatorial Guinea', 'Timor-Leste', 'South Africa', 'United States Minor Outlying Islands', 'Lebanon', 'Micronesia', 'Isle of Man', 'Macao', 'Afghanistan', 'Czech Republic', 'Djibouti', 'Bouvet Island (Bouvetoya)', 'Norway', 'Macao', 'Antigua and Barbuda', 'Senegal', 'Chad'], 'Population': [136, 141, 138, 66, 34, 21, 148, 50, 92, 41, 19, 21, 55, 137, 84, 113, 96, 113, 48, 93, 70, 94, 95, 75, 130, 47, 120, 65, 45, 85, 71, 65, 81, 71, 64, 87, 78, 107, 73, 109, 18, 109, 97, 67, 23, 141, 126, 94, 126, 84, 120, 131, 114, 14, 90, 103, 54, 41, 51, 139, 35, 66, 138, 102, 76, 149, 106, 97, 51, 120, 131, 133, 93, 50, 42, 16, 78, 24, 99, 20, 145, 86, 36, 69, 36, 78, 52, 143, 139, 47, 139, 62, 149, 82, 67, 115, 54, 130, 85, 117, 73, 54, 129, 42, 54, 85, 102, 116, 99, 13, 145, 97, 83, 39, 78, 72, 61, 89, 23, 44, 148, 45, 115, 77, 28, 37, 93, 88, 147, 26, 40, 123, 24, 58, 26, 123, 40, 98, 38, 138, 51, 17, 80, 27, 74, 76, 34, 132, 117, 87], 'GDP': [31, 32, 15, 67, 96, 73, 31, 29, 107, 45, 142, 101, 83, 117, 114, 87, 99, 15, 45, 56, 132, 89, 109, 115, 75, 33, 150, 113, 41, 16, 87, 73, 138, 91, 116, 146, 71, 97, 144, 46, 44, 61, 143, 57, 95, 114, 49, 76, 118, 10, 137, 129, 114, 140, 61, 25, 49, 70, 22, 107, 57, 130, 132, 50, 13, 150, 113, 131, 95, 99, 78, 94, 32, 113, 69, 118, 46, 24, 68, 81, 149, 107, 43, 27, 13, 50, 145, 46, 44, 99, 25, 43, 97, 58, 61, 132, 70, 44, 49, 143, 149, 107, 131, 116, 89, 102, 147, 88, 42, 79, 111, 33, 22, 62, 99, 147, 38, 126, 74, 102, 120, 92, 108, 66, 34, 78, 74, 93, 90, 53, 67, 36, 115, 21, 24, 98, 39, 143, 100, 28, 20, 119, 64, 123, 36, 69, 117, 95, 116, 15]})
        population_threshold = random.randint(10, 150)
        gdp_threshold = random.randint(10, 150)
        selected_df, corr_matrix = f_122(df, population_threshold, gdp_threshold)
        
        # Assert that the selected_df has correct rows based on the thresholds
        self.assertTrue(all(selected_df['Population'] > population_threshold))
        self.assertTrue(all(selected_df['GDP'] > gdp_threshold))
        
        # Assert corr_matrix is correctly computed
        self.assertEqual(corr_matrix.shape, (2, 2))
        self.assertIn('Population', corr_matrix.columns)
        self.assertIn('GDP', corr_matrix.columns)

    def test_case_4(self):
        random.seed(42)
        df = pd.DataFrame({'Country': ['Cape Verde', 'Guatemala', 'Australia', 'United Kingdom', 'Faroe Islands', 'Cocos (Keeling) Islands', 'Mali', 'Colombia', 'Turkey', 'Lithuania', 'Saint Kitts and Nevis', 'Sudan', 'Cuba', 'Bosnia and Herzegovina', 'Qatar', 'Moldova', 'Indonesia', 'Luxembourg', 'Christmas Island', 'Uruguay', 'Saint Lucia', 'Hungary', 'Angola', 'Bangladesh', 'Saint Kitts and Nevis', 'Saint Helena', 'Marshall Islands', 'Papua New Guinea', 'Belgium', 'Venezuela', 'Austria', 'Taiwan', 'Saint Vincent and the Grenadines', 'Czech Republic', 'Portugal', 'Tanzania', 'Kuwait', 'South Georgia and the South Sandwich Islands', 'Saint Martin', 'Ghana', 'France', 'Samoa', 'Singapore', 'Kenya', 'Suriname', "Cote d'Ivoire", 'Niue', 'Argentina', 'Hungary', 'Lesotho', 'Spain', 'Marshall Islands', 'Nicaragua', 'San Marino', 'Saint Kitts and Nevis', 'Armenia', 'Pakistan', 'Madagascar', 'Gabon', 'Finland', 'Swaziland', 'Burkina Faso', 'United States Minor Outlying Islands', 'Gabon', 'Micronesia', 'Sao Tome and Principe', 'Tonga', 'Malawi', 'Svalbard & Jan Mayen Islands', 'Jersey', 'Tuvalu', 'Turks and Caicos Islands', 'Oman', 'Iraq', 'Falkland Islands (Malvinas)', 'Saudi Arabia', 'Italy', 'Mayotte', 'Madagascar', 'Montenegro', 'Mexico', 'Bulgaria', 'Saint Martin', 'Costa Rica', 'Lesotho', 'Thailand', 'Cambodia', 'Papua New Guinea', 'Costa Rica', 'Cape Verde', 'Denmark', 'Denmark', 'Greece', 'Aruba', 'Uganda', 'Kazakhstan', 'Faroe Islands', 'Thailand', 'Antarctica (the territory South of 60 deg S)', 'United States Virgin Islands', 'Central African Republic', 'Guatemala', 'British Virgin Islands', 'Tanzania', 'Finland', 'Nepal', 'Singapore', 'Kyrgyz Republic', 'Micronesia', 'Maldives', 'Sri Lanka', 'Armenia', 'Pitcairn Islands', 'Faroe Islands', 'Antigua and Barbuda', 'Niue', 'Afghanistan', 'Mozambique', 'Netherlands', 'Germany', 'Micronesia', 'Saint Barthelemy', 'Heard Island and McDonald Islands', 'Heard Island and McDonald Islands', 'France', 'Turkmenistan', 'Afghanistan', 'Somalia', 'Belize', 'Greenland', 'Saint Barthelemy', 'Korea', 'Cuba', 'Isle of Man', 'Christmas Island', 'Antarctica (the territory South of 60 deg S)', 'Nepal', 'Somalia', 'Tunisia', 'Bahrain', 'Andorra', 'India', 'French Polynesia', 'Bahamas', 'Zambia', 'Brunei Darussalam', 'Anguilla', 'Cape Verde', 'British Virgin Islands', 'Liechtenstein', 'Western Sahara', 'Poland', 'Guyana', 'Angola', 'Cocos (Keeling) Islands', 'Bosnia and Herzegovina', 'Benin', 'Turkey', 'Pakistan', 'Heard Island and McDonald Islands', 'Timor-Leste', 'Serbia', 'French Southern Territories', 'Brunei Darussalam', 'Montenegro', 'Russian Federation', 'Gabon', 'Haiti', 'Paraguay', 'Greenland', 'Suriname', 'United Kingdom', 'Nepal', 'United States Virgin Islands', 'Ukraine', 'Anguilla', 'Tuvalu', 'Cape Verde', 'Netherlands Antilles', 'Senegal', 'Finland', 'Cyprus', 'Ecuador', 'Falkland Islands (Malvinas)', 'Nicaragua', 'Ethiopia', 'Kyrgyz Republic', 'Sri Lanka', 'Venezuela', 'Chile', 'Spain', 'Malta', 'New Caledonia', 'Paraguay', 'Finland', 'Namibia', 'Andorra', 'Congo', 'Wallis and Futuna', 'French Guiana'], 'Population': [93, 126, 138, 38, 10, 131, 113, 25, 98, 112, 56, 134, 52, 120, 76, 41, 20, 115, 23, 138, 138, 109, 136, 45, 71, 63, 110, 90, 77, 37, 24, 148, 29, 110, 104, 41, 85, 101, 105, 134, 14, 117, 147, 54, 35, 127, 51, 127, 103, 104, 49, 64, 110, 130, 43, 86, 105, 54, 89, 69, 134, 141, 64, 147, 21, 14, 35, 101, 56, 50, 113, 68, 108, 107, 13, 74, 65, 134, 117, 23, 105, 115, 51, 65, 86, 69, 135, 57, 107, 69, 135, 97, 97, 15, 27, 33, 120, 78, 47, 42, 105, 69, 45, 14, 134, 20, 82, 95, 60, 79, 79, 15, 125, 28, 34, 88, 138, 84, 62, 75, 148, 21, 45, 95, 97, 148, 115, 123, 107, 31, 122, 99, 132, 62, 43, 52, 30, 94, 140, 85, 124, 118, 126, 68, 45, 10, 31, 58, 68, 112, 50, 47, 128, 62, 70, 103, 84, 61, 84, 31, 83, 150, 124, 38, 48, 79, 37, 38, 88, 116, 117, 89, 124, 69, 12, 91, 69, 122, 117, 102, 83, 136, 30, 86, 125, 33, 142, 34, 52, 84, 72, 88, 102, 52, 79, 135, 46, 74, 91, 34], 'GDP': [36, 14, 83, 147, 96, 144, 135, 72, 100, 99, 102, 46, 71, 150, 124, 129, 106, 21, 42, 15, 121, 127, 143, 56, 143, 84, 121, 126, 57, 128, 146, 27, 105, 111, 38, 60, 110, 89, 138, 77, 55, 53, 41, 49, 125, 21, 69, 130, 135, 147, 40, 19, 129, 10, 50, 137, 29, 141, 111, 100, 31, 80, 11, 64, 119, 58, 46, 78, 80, 79, 85, 88, 89, 103, 125, 96, 80, 59, 117, 52, 145, 25, 32, 148, 133, 56, 44, 94, 20, 121, 39, 27, 96, 46, 49, 114, 111, 116, 66, 60, 38, 112, 14, 64, 70, 143, 110, 95, 97, 88, 149, 150, 51, 147, 18, 44, 95, 62, 57, 136, 89, 17, 106, 60, 55, 19, 76, 125, 30, 81, 120, 34, 128, 109, 52, 57, 111, 129, 112, 125, 89, 35, 118, 125, 72, 131, 105, 148, 97, 69, 100, 86, 24, 74, 39, 145, 23, 50, 126, 11, 128, 19, 70, 65, 96, 106, 147, 122, 18, 97, 95, 97, 128, 35, 72, 118, 35, 87, 39, 140, 22, 10, 19, 35, 17, 58, 77, 118, 67, 29, 61, 46, 72, 91, 97, 65, 111, 102, 17, 62]})
        population_threshold = random.randint(10, 150)
        gdp_threshold = random.randint(10, 150)
        selected_df, corr_matrix = f_122(df, population_threshold, gdp_threshold)
        
        # Assert that the selected_df has correct rows based on the thresholds
        self.assertTrue(all(selected_df['Population'] > population_threshold))
        self.assertTrue(all(selected_df['GDP'] > gdp_threshold))
        
        # Assert corr_matrix is correctly computed
        self.assertEqual(corr_matrix.shape, (2, 2))
        self.assertIn('Population', corr_matrix.columns)
        self.assertIn('GDP', corr_matrix.columns)

    def test_case_5(self):
        random.seed(42)
        df = pd.DataFrame({'Country': ['Bouvet Island (Bouvetoya)', 'Zambia', 'Turks and Caicos Islands', 'Burkina Faso', 'Myanmar', 'Montserrat', 'Sierra Leone', 'Gabon', 'Antarctica (the territory South of 60 deg S)', 'Papua New Guinea', 'Thailand', 'Denmark', 'Zambia', 'Finland', 'Bulgaria', 'Greece', 'Liberia', 'Syrian Arab Republic', 'Eritrea', 'Cuba', 'United States of America', 'Portugal', 'Russian Federation', 'British Virgin Islands', 'Turkey', 'American Samoa', 'Slovakia (Slovak Republic)', 'Brazil', 'Guernsey', 'Serbia', 'Tunisia', 'India', 'Senegal', 'Paraguay', 'United Kingdom', 'Zimbabwe', 'Palau', 'Mongolia', 'Peru', 'Greenland', 'Saint Helena', 'Netherlands', 'Trinidad and Tobago', 'Kuwait', 'French Southern Territories', 'Samoa', 'Belgium', 'Canada', 'Turkey', 'Netherlands', 'Taiwan', 'Georgia', 'Greece', 'Nigeria', 'El Salvador', 'Djibouti', 'Thailand', 'Northern Mariana Islands', 'Hungary', 'Algeria', 'Taiwan', 'French Southern Territories', 'Comoros', 'South Georgia and the South Sandwich Islands', 'Guernsey', 'Zambia', 'Cameroon', 'Iceland', 'Czech Republic', 'Yemen', 'India', 'Tokelau', 'Brunei Darussalam', 'Zimbabwe', 'Mayotte', 'Pakistan', 'Tonga', 'Tunisia', 'Faroe Islands', 'Brunei Darussalam', 'Colombia', 'Colombia', 'Chad', 'Dominica', 'Montserrat', 'Afghanistan', 'Romania', 'Greenland', 'Philippines', 'Hong Kong', 'Saint Barthelemy', 'Latvia', 'Congo', 'Iran', 'Luxembourg', 'Puerto Rico', 'British Indian Ocean Territory (Chagos Archipelago)', 'Moldova', 'Romania', 'French Southern Territories', 'Nigeria', 'Haiti', 'Philippines', 'Bolivia', 'Hong Kong', 'Saint Helena', 'Papua New Guinea', 'Syrian Arab Republic', 'Thailand', 'Cuba', 'Egypt', 'Swaziland', 'Pitcairn Islands', 'Heard Island and McDonald Islands', 'Faroe Islands', 'Saint Vincent and the Grenadines', 'British Indian Ocean Territory (Chagos Archipelago)', 'Panama', 'Madagascar', 'Nicaragua', 'British Virgin Islands', 'Jersey', 'France', 'Ecuador', 'Lithuania', 'Spain', 'Iran', 'Chile', 'British Indian Ocean Territory (Chagos Archipelago)', 'Marshall Islands', 'Turks and Caicos Islands', 'Ireland', 'Honduras', 'Falkland Islands (Malvinas)', 'Reunion', 'Aruba', 'India', 'Martinique', 'Faroe Islands', 'Egypt', 'Jordan', 'Uganda', 'South Georgia and the South Sandwich Islands', 'Bahrain', 'Tanzania', 'Ghana', 'Faroe Islands', 'Grenada', 'El Salvador', 'Madagascar', 'Marshall Islands', 'Uruguay', 'Barbados', 'Palau', 'Turkey', 'Ethiopia', 'Indonesia', 'Palau', 'Puerto Rico', 'Nepal', 'Nicaragua', 'Costa Rica', 'Maldives', 'Liberia', 'Vanuatu', 'China', 'British Virgin Islands', 'Central African Republic', 'Luxembourg', 'Mexico', 'Taiwan', 'Peru', 'Croatia', 'Montserrat', 'British Virgin Islands', 'Hong Kong', 'Zimbabwe', 'Niue', 'British Virgin Islands', 'Iceland', 'Mozambique', 'South Georgia and the South Sandwich Islands', 'Uzbekistan', 'South Georgia and the South Sandwich Islands', "Cote d'Ivoire", 'Montenegro', 'Niue', 'Zambia', 'Lithuania', 'Equatorial Guinea', 'Israel', 'Vanuatu', 'Martinique', 'South Africa', 'Afghanistan', 'Seychelles', 'Brunei Darussalam', 'Croatia', 'Syrian Arab Republic', 'Kenya', 'Kuwait', 'Anguilla', 'Puerto Rico', 'Pitcairn Islands', 'Mauritania', 'Belize', 'Norway', 'Falkland Islands (Malvinas)', 'Ukraine', 'Slovenia', 'Sri Lanka', 'Bulgaria', 'Northern Mariana Islands', 'Brunei Darussalam', 'United States of America', "Lao People's Democratic Republic", 'Nepal', 'Guam', 'Aruba', 'Indonesia', 'Mauritania', 'Solomon Islands', 'Cook Islands', 'Chile', 'Greece', 'Chad', 'United Arab Emirates', 'Jersey', 'Tajikistan', 'Falkland Islands (Malvinas)', 'Netherlands', 'Montenegro', 'Turks and Caicos Islands', 'Cuba', 'Morocco', 'Netherlands', 'Paraguay', 'Costa Rica', 'Marshall Islands', 'Martinique', 'Lithuania', 'Madagascar', 'Peru', 'Turks and Caicos Islands', 'Italy', 'Rwanda', 'Taiwan', 'Venezuela', 'Denmark', 'Tunisia'], 'Population': [125, 134, 38, 122, 43, 133, 28, 73, 67, 11, 124, 33, 23, 129, 143, 58, 140, 100, 73, 78, 16, 114, 140, 17, 108, 60, 32, 124, 41, 137, 117, 119, 16, 71, 84, 78, 129, 91, 57, 51, 128, 121, 103, 96, 24, 11, 13, 21, 37, 101, 73, 129, 60, 97, 56, 64, 127, 103, 60, 110, 128, 61, 65, 16, 120, 61, 33, 66, 60, 18, 27, 78, 38, 91, 15, 118, 110, 38, 139, 136, 116, 37, 137, 85, 111, 94, 55, 96, 140, 145, 60, 36, 81, 119, 120, 27, 34, 25, 95, 74, 97, 39, 85, 55, 149, 10, 96, 88, 44, 93, 125, 137, 75, 131, 129, 26, 42, 50, 76, 74, 24, 12, 135, 34, 118, 87, 122, 99, 149, 40, 12, 51, 19, 125, 103, 17, 145, 104, 111, 33, 116, 49, 73, 61, 60, 49, 94, 59, 133, 141, 146, 115, 47, 78, 57, 146, 42, 22, 127, 90, 124, 46, 129, 76, 85, 10, 104, 40, 54, 55, 143, 99, 14, 54, 65, 29, 62, 66, 82, 54, 100, 22, 109, 63, 25, 148, 41, 107, 124, 64, 95, 126, 12, 11, 135, 121, 67, 27, 18, 43, 135, 140, 69, 72, 114, 148, 108, 123, 60, 12, 49, 147, 53, 138, 68, 146, 73, 35, 96, 64, 121, 150, 127, 79, 81, 57, 43, 23, 86, 49, 137, 61, 44, 31, 36, 126, 66, 118, 86, 17, 97, 149, 27, 86, 81, 28, 34, 112, 78, 111], 'GDP': [82, 133, 110, 49, 89, 24, 85, 28, 34, 56, 57, 98, 42, 109, 31, 134, 84, 132, 126, 130, 97, 107, 36, 137, 145, 68, 60, 115, 118, 121, 16, 92, 90, 108, 119, 15, 44, 101, 81, 110, 109, 49, 118, 58, 138, 97, 55, 47, 93, 148, 118, 20, 59, 29, 77, 21, 43, 31, 96, 22, 54, 130, 128, 55, 46, 125, 116, 37, 97, 118, 104, 28, 117, 98, 82, 62, 66, 18, 112, 11, 93, 37, 123, 104, 44, 15, 11, 19, 76, 51, 103, 71, 46, 113, 97, 143, 78, 147, 118, 37, 38, 138, 100, 106, 50, 128, 15, 131, 22, 38, 77, 52, 106, 76, 29, 77, 39, 35, 38, 85, 107, 122, 108, 84, 86, 44, 18, 98, 71, 18, 145, 150, 51, 23, 23, 112, 23, 50, 60, 14, 20, 25, 79, 85, 95, 48, 40, 106, 72, 109, 116, 42, 77, 77, 11, 149, 77, 76, 16, 46, 19, 59, 57, 150, 104, 25, 102, 78, 18, 93, 126, 69, 116, 95, 148, 133, 54, 46, 54, 71, 129, 124, 29, 96, 29, 93, 35, 41, 78, 118, 118, 25, 150, 48, 17, 78, 117, 88, 107, 127, 42, 150, 103, 126, 93, 57, 36, 30, 83, 109, 38, 101, 122, 139, 32, 138, 148, 85, 84, 57, 10, 32, 83, 34, 75, 84, 88, 82, 116, 110, 85, 20, 102, 73, 16, 87, 121, 61, 34, 133, 78, 110, 18, 86, 91, 43, 124, 65, 44, 81]})
        population_threshold = random.randint(10, 150)
        gdp_threshold = random.randint(10, 150)
        selected_df, corr_matrix = f_122(df, population_threshold, gdp_threshold)
        
        # Assert that the selected_df has correct rows based on the thresholds
        self.assertTrue(all(selected_df['Population'] > population_threshold))
        self.assertTrue(all(selected_df['GDP'] > gdp_threshold))
        
        # Assert corr_matrix is correctly computed
        self.assertEqual(corr_matrix.shape, (2, 2))
        self.assertIn('Population', corr_matrix.columns)
        self.assertIn('GDP', corr_matrix.columns)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()