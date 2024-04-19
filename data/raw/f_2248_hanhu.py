import pandas as pd
import folium
from geopy.geocoders import Photon

def f_2250(dic):
    """
    Generates a Folium map with markers for specified locations. It preprocesses the input to handle
    both direct geographical coordinates and address strings. For address strings, it dynamically resolves
    their latitude and longitude using the Photon geolocation service. This flexible input handling
    allows for easy mapping of various location types.

    Parameters:
        dic (dict): A dictionary with location names as keys. Each key can either map to a dictionary
                    {'Lat': latitude, 'Lon': longitude} for direct coordinates, or to a string indicating
                    the location's address for geolocation lookup using Photon.

    Returns:
        folium.Map: A Folium map object with markers for each specified location.

    Requirements:
    - pandas
    - folium
    - geopy.geocoders.Photon

    Notes:
    - The geolocator, instantiated as Photon(user_agent="geoapiExercises"), plays a crucial role in enabling
    the function to handle string addresses by converting them into latitude and longitude, thus broadening
    the scope of input data that can be mapped.

    Examples:
    >>> locations = {'Place1': {'Lat': 0, 'Lon': 0}, 'Place2': 'New York, USA'}
    >>> result = f_2250(locations)
    >>> isinstance(result, folium.Map)
    True
    >>> [0.0, 0.0] == result.location
    True
    """
    geolocator = Photon(user_agent="geoapiExercises")

    # Preprocess to handle both coordinates and string addresses
    preprocessed_locations = []
    for location, value in dic.items():
        if isinstance(value, dict) and 'Lat' in value and 'Lon' in value:
            preprocessed_locations.append({'Location': location, 'Lat': value['Lat'], 'Lon': value['Lon']})
        elif isinstance(value, str):
            geocoded_location = geolocator.geocode(value)
            preprocessed_locations.append({'Location': location, 'Lat': geocoded_location.latitude, 'Lon': geocoded_location.longitude})
        else:
            raise ValueError("Location value must be either a dict with 'Lat' and 'Lon' keys or a string.")

    locations_df = pd.DataFrame(preprocessed_locations)

    # Assuming the first row has valid coordinates
    first_row = locations_df.iloc[0]
    folium_map = folium.Map(location=[first_row['Lat'], first_row['Lon']], zoom_start=4)

    # Add markers for all locations
    for _, row in locations_df.iterrows():
        folium.Marker([row['Lat'], row['Lon']], popup=row['Location']).add_to(folium_map)

    return folium_map


import unittest
from unittest.mock import patch, MagicMock

class TestCases(unittest.TestCase):
    def setUp(self):
        # Mocking the geocode return to control output of Photon geocode calls
        self.geocode_patch = patch('geopy.geocoders.Photon.geocode', return_value=MagicMock(latitude=0, longitude=0))
        self.mock_geocode = self.geocode_patch.start()
        # Ensure to stop the patcher to avoid side-effects
        self.addCleanup(self.geocode_patch.stop)

    def test_return_type(self):
        """Test that the function returns a folium.Map object."""
        locations = {'Loc1': {'Lat': 0, 'Lon': 0}}
        result = f_2250(locations)
        self.assertIsInstance(result, folium.Map)

    @patch('folium.Map')
    @patch('folium.Marker')
    def test_marker_creation(self, mock_marker, mock_map):
        """Test that markers are added to the map for each location."""
        locations = {'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 1, 'Lon': 1}}
        f_2250(locations)
        self.assertEqual(mock_marker.call_count, len(locations))

    @patch('geopy.geocoders.Photon.geocode')
    def test_different_locations(self, mock_geocode):
        mock_geocode.return_value = MagicMock(latitude=40.7128, longitude=-74.0060)
        locations = {'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': 'New York, USA'}
        result = f_2250(locations)
        # Verifying that geocode was called for the string location
        mock_geocode.assert_called_once_with('New York, USA')

    def test_initial_centering(self):
        """Test that the map is initially centered on the first location."""
        locations = {'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 3, 'Lon': 3}}
        result = f_2250(locations)
        self.assertEqual(result.location, [0, 0])

    @patch('folium.Map')
    def test_map_initialization(self, mock_map):
        """Test that the map is initialized with correct latitude and longitude."""
        locations = {'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 4, 'Lon': 4}}
        f_2250(locations)
        # Assuming that the map is initialized at the location of the first entry in the dictionary
        mock_map.assert_called_with(location=[0, 0], zoom_start=4)



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
