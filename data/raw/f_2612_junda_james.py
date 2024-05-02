import os
import pandas as pd
import folium
import tempfile
import shutil

def f_2612(dirname, outfile, columns=['Latitude', 'Longitude', 'Value']):
    """
    Iterate over a directory of CSV files, each containing geographical data (latitude, longitude, and a value),
    and plot the locations on a map with circle markers, where the size of the circle represents the value.

    Parameters:
    dirname (str): The directory containing the CSV files.
    outfile (str): The output HTML file name.
    columns (list): The column names for the DataFrame. Default: ['Latitude', 'Longitude', 'Value'].

    Returns:
    folium.Map: A folium map object.

    Raises:
    FileNotFoundError: If the directory does not exist.
    ValueError: If outfile is not a valid string.

    Requirements:
    - os
    - pandas
    - folium
    - tempfile
    - shutil

    Example:
    >>> tmp_dir = create_dummy_csv_files()
    >>> map_obj = f_2612(tmp_dir, 'map.html')
    >>> shutil.rmtree(tmp_dir)
    """
    if not os.path.exists(dirname):
        raise FileNotFoundError(f"Directory '{dirname}' does not exist")
    if not isinstance(outfile, str):
        raise ValueError("outfile must be a string")

    files = [file for file in os.listdir(dirname) if file.endswith('.csv')]
    df_list = []

    for file in files:
        filepath = os.path.join(dirname, file)
        df = pd.read_csv(filepath, names=columns)
        df_list.append(df)

    if not df_list:
        return folium.Map(location=[0, 0], zoom_start=2)  # Return an empty map

    df_all = pd.concat(df_list)

    m = folium.Map(location=[df_all[columns[0]].mean(), df_all[columns[1]].mean()], zoom_start=3)

    for _, row in df_all.iterrows():
        folium.Circle(
            location=[row[columns[0]], row[columns[1]]],
            radius=row[columns[2]],
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(m)

    return m

import unittest
import tempfile
import shutil

def create_dummy_csv_files():
    temp_dir = tempfile.mkdtemp()
    for i in range(3):
        data = {'Latitude': [i, i+1], 'Longitude': [i+2, i+3], 'Value': [i*10, (i+1)*10]}
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(temp_dir, f'dummy{i}.csv'), index=False, header=False)
    return temp_dir

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a temporary directory with dummy CSV files
        cls.temp_dir = tempfile.mkdtemp()
        for i in range(3):
            data = {'Latitude': [i, i+1], 'Longitude': [i+2, i+3], 'Value': [i*10, (i+1)*10]}
            df = pd.DataFrame(data)
            df.to_csv(os.path.join(cls.temp_dir, f'dummy{i}.csv'), index=False, header=False)
            
        cls.temp_dir1 = tempfile.mkdtemp()
        cls.custom_columns = ['Lat', 'Lon', 'Val']
        data_custom = {'Lat': [2, 3], 'Lon': [4, 5], 'Val': [20, 30]}
        df_custom = pd.DataFrame(data_custom)
        df_custom.to_csv(os.path.join(cls.temp_dir1, 'custom.csv'), index=False, header=False)

    @classmethod
    def tearDownClass(cls):
        # Remove temporary directory
        shutil.rmtree(cls.temp_dir)
        shutil.rmtree(cls.temp_dir1)

    def test_valid_input(self):
        def extract_circle_markers_info(map_obj):
            circle_markers_info = []
            for feature in map_obj._children.values():
                if isinstance(feature, folium.Circle):
                    location = feature.location
                    # Attempt to access the radius from the options attribute
                    radius = feature.options.get('radius', 'Radius not set')
                    circle_markers_info.append({'location': location, 'radius': radius})
            return circle_markers_info

            
        map_obj = f_2612(self.temp_dir, 'test_map.html')
        circle_markers_info = extract_circle_markers_info(map_obj)
        expect = [{'location': [2.0, 4.0], 'radius': 20}, {'location': [3.0, 5.0], 'radius': 30}, {'location': [1.0, 3.0], 'radius': 10}, {'location': [2.0, 4.0], 'radius': 20}, {'location': [0.0, 2.0], 'radius': 'Radius not set'}, {'location': [1.0, 3.0], 'radius': 10}]
        self.assertIsInstance(map_obj, folium.Map)
        self.assertEqual(expect, circle_markers_info)

    def test_invalid_directory(self):
        with self.assertRaises(FileNotFoundError):
            f_2612('./nonexistent_dir/', 'test_map.html')

    def test_invalid_outfile_type(self):
        with self.assertRaises(ValueError):
            f_2612(self.temp_dir, 123)

    def test_no_csv_files_in_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            map_obj = f_2612(temp_dir, 'test_map.html')
            self.assertIsInstance(map_obj, folium.Map)

    def test_custom_columns(self):
        custom_columns = ['Lat', 'Lon', 'Val']
        map_obj = f_2612(self.temp_dir1, 'test_map.html', columns=custom_columns)
        self.assertIsInstance(map_obj, folium.Map)

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