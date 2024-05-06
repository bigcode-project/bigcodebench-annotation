import pandas as pd
import numpy as np
import folium

def f_2245(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    """
    Create a map with markers for a list of cities, where the coordinates are randomly generated within given ranges.

    Parameters:
    dic (dict): Dictionary with 'Lon' and 'Lat' keys, each a tuple (min, max) for coordinate range. 
                Default: {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities (list): List of city names. Default: ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']

    Returns:
    tuple: A tuple containing (folium.Map, pandas.DataFrame).
           The DataFrame contains 'City', 'Longitude', and 'Latitude' columns.

    Raises:
    ValueError: If 'Lon' or 'Lat' keys are missing in the dictionary, or if their values are not tuples.

    Requirements:
    - pandas
    - numpy
    - folium

    Example:
    >>> dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    >>> map_obj, city_data = f_2245(dic)
    """
    if 'Lon' not in dic or 'Lat' not in dic or not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Dictionary must contain 'Lon' and 'Lat' keys with tuple values.")

    lon_min, lon_max = dic['Lon']
    lat_min, lat_max = dic['Lat']

    data = {'City': [], 'Longitude': [], 'Latitude': []}
    for city in cities:
        data['City'].append(city)
        data['Longitude'].append(np.random.uniform(lon_min, lon_max))
        data['Latitude'].append(np.random.uniform(lat_min, lat_max))

    df = pd.DataFrame(data)

    m = folium.Map(location=[0, 0], zoom_start=2)
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['City']).add_to(m)

    return m, df

import unittest
import numpy as np
import pandas as pd
import folium

class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        np.random.seed(42)
        map_obj, city_data = f_2245()
        self.assertEqual(len(city_data), 5)  # Default 5 cities
        self.assertIsInstance(city_data, pd.DataFrame)
        self.assertIn('New York', city_data['City'].values)
        
        df_list = city_data.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))
            
        expect = ['New York,-45.1655572149495,81.12857515378491', 'London,83.51781905210584,17.758527155466595', 'Beijing,-123.83328944072285,-61.92098633948352', 'Tokyo,-159.0898996194482,65.91170623948832', 'Sydney,36.40140422755516,37.45306400328819']
        
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")

    def test_custom_cities(self):
        custom_cities = ['Paris', 'Berlin']
        _, city_data = f_2245(cities=custom_cities)
        self.assertEqual(len(city_data), 2)
        self.assertTrue(all(city in city_data['City'].values for city in custom_cities))

    def test_invalid_dic(self):
        with self.assertRaises(ValueError):
            f_2245(dic={'Lon': 'invalid', 'Lat': (-90, 90)})

    def test_coordinate_ranges(self):
        _, city_data = f_2245(dic={'Lon': (0, 10), 'Lat': (0, 10)})
        self.assertTrue(all(0 <= lon <= 10 for lon in city_data['Longitude']))
        self.assertTrue(all(0 <= lat <= 10 for lat in city_data['Latitude']))

    def test_return_types(self):
        map_obj, city_data = f_2245()
        self.assertIsInstance(map_obj, folium.Map)
        self.assertIsInstance(city_data, pd.DataFrame)

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()