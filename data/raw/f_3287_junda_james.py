import os
import glob
import pandas as pd
from typing import List

def f_3287(excel_directory: str, file_pattern: str) -> List[pd.DataFrame]:
    """
    Reads all Excel files in a specified directory that match a given pattern, 
    converts each one into a Pandas DataFrame, and returns a list of DataFrames.

    Parameters:
    excel_directory (str): The directory containing Excel files.
    file_pattern (str): The pattern for matching Excel file names (e.g., 'data_*.xls').

    Returns:
    List[pd.DataFrame]: A list of pandas DataFrames.

    Raises:
    FileNotFoundError: If the specified directory does not exist.
    ValueError: If no files match the given pattern.

    Requirements:
    - os
    - glob
    - pandas
    - typing

    Example:
    >>> data_dir = 'excel_files'
    >>> create_dummy_excel_files(data_dir)
    >>> df_list = f_3287(data_dir, 'file*.xls')
    >>> for df in df_list:
    ...     print(df.head())
       Unnamed: 0         0         1         2
    0           0  0.318569  0.667410  0.131798
    1           1  0.716327  0.289406  0.183191
    2           2  0.586513  0.020108  0.828940
    3           3  0.004695  0.677817  0.270008
    4           4  0.735194  0.962189  0.248753
       Unnamed: 0         0         1         2
    0           0  0.158970  0.110375  0.656330
    1           1  0.138183  0.196582  0.368725
    2           2  0.820993  0.097101  0.837945
    3           3  0.096098  0.976459  0.468651
    4           4  0.976761  0.604846  0.739264
       Unnamed: 0         0         1         2
    0           0  0.548814  0.715189  0.602763
    1           1  0.544883  0.423655  0.645894
    2           2  0.437587  0.891773  0.963663
    3           3  0.383442  0.791725  0.528895
    4           4  0.568045  0.925597  0.071036
       Unnamed: 0         0         1         2
    0           0  0.264556  0.774234  0.456150
    1           1  0.568434  0.018790  0.617635
    2           2  0.612096  0.616934  0.943748
    3           3  0.681820  0.359508  0.437032
    4           4  0.697631  0.060225  0.666767
       Unnamed: 0         0         1         2
    0           0  0.725254  0.501324  0.956084
    1           1  0.643990  0.423855  0.606393
    2           2  0.019193  0.301575  0.660174
    3           3  0.290078  0.618015  0.428769
    4           4  0.135474  0.298282  0.569965
    >>> tear_down_excel_files(data_dir)
    """
    if not os.path.exists(excel_directory):
        raise FileNotFoundError(f"The directory {excel_directory} does not exist.")

    file_path = os.path.join(excel_directory, file_pattern)
    excel_files = glob.glob(file_path)

    if not excel_files:
        raise ValueError(f"No files found matching the pattern {file_pattern} in {excel_directory}")

    df_list = []
    for file in excel_files:
        df = pd.read_excel(file)
        df_list.append(df)
    
    return df_list

import unittest
import numpy as np
import pandas as pd
import os

def create_dummy_excel_files(data_dir):
    os.makedirs(data_dir, exist_ok=True)
    np.random.seed(0)
    for i in range(5):
        pd.DataFrame(np.random.rand(10, 3)).to_excel(os.path.join(data_dir, f'file_{i}.xls'))

def tear_down_excel_files(data_dir):
    for file in os.listdir(data_dir):
        os.remove(os.path.join(data_dir, file))
    os.rmdir(data_dir)

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create dummy Excel files for testing
        cls.test_dir = 'test_excel_files'
        os.makedirs(cls.test_dir, exist_ok=True)
        np.random.seed(0)
        for i in range(5):
            pd.DataFrame(np.random.rand(10, 3)).to_excel(os.path.join(cls.test_dir, f'test_file_{i}.xls'))

    @classmethod
    def tearDownClass(cls):
        # Cleanup test directory
        for file in os.listdir(cls.test_dir):
            os.remove(os.path.join(cls.test_dir, file))
        os.rmdir(cls.test_dir)

    def test_valid_input(self):
        df_lists = f_3287(self.test_dir, 'test_file_*.xls')
        # with open('df_contents.txt', 'w') as file:
        #     for df in df_lists:
        #         df_list = df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        #         file.write(str(df_list))
        #         file.write(', ')
        #     file.close()
                
        expect_df = [['0.0,0.7252542798196405,0.5013243819267023,0.9560836347232239', '1.0,0.6439901992296374,0.4238550485581797,0.6063932141279244', '2.0,0.019193198309333526,0.30157481667454933,0.660173537492685', '3.0,0.29007760721044407,0.6180154289988415,0.42876870094576613', '4.0,0.13547406422245023,0.29828232595603077,0.5699649107012649', '5.0,0.5908727612481732,0.5743252488495788,0.6532008198571336', '6.0,0.6521032700016889,0.43141843543397396,0.896546595851063', '7.0,0.36756187004789653,0.4358649252656268,0.8919233550156721', '8.0,0.8061939890460857,0.7038885835403663,0.10022688731230112', '9.0,0.9194826137446735,0.7142412995491114,0.9988470065678665'], ['0.0,0.31856895245132366,0.6674103799636817,0.13179786240439217', '1.0,0.7163272041185655,0.2894060929472011,0.18319136200711683', '2.0,0.5865129348100832,0.020107546187493552,0.8289400292173631', '3.0,0.004695476192547066,0.6778165367962301,0.27000797319216485', '4.0,0.7351940221225949,0.9621885451174382,0.24875314351995803', '5.0,0.5761573344178369,0.592041931271839,0.5722519057908734', '6.0,0.2230816326406183,0.952749011516985,0.44712537861762736', '7.0,0.8464086724711278,0.6994792753175043,0.29743695085513366', '8.0,0.8137978197024772,0.39650574084698464,0.8811031971111616', '9.0,0.5812728726358587,0.8817353618548528,0.6925315900777659'], ['0.0,0.15896958364551972,0.11037514116430513,0.6563295894652734', '1.0,0.1381829513486138,0.1965823616800535,0.3687251706609641', '2.0,0.8209932298479351,0.09710127579306127,0.8379449074988039', '3.0,0.09609840789396307,0.9764594650133958,0.4686512016477016', '4.0,0.9767610881903371,0.604845519745046,0.7392635793983017', '5.0,0.039187792254320675,0.2828069625764096,0.1201965612131689', '6.0,0.29614019752214493,0.11872771895424405,0.317983179393976', '7.0,0.41426299451466997,0.06414749634878436,0.6924721193700198', '8.0,0.5666014542065752,0.2653894909394454,0.5232480534666997', '9.0,0.09394051075844168,0.5759464955561793,0.9292961975762141'], ['0.0,0.5488135039273248,0.7151893663724195,0.6027633760716439', '1.0,0.5448831829968969,0.4236547993389047,0.6458941130666561', '2.0,0.4375872112626925,0.8917730007820798,0.9636627605010293', '3.0,0.3834415188257777,0.7917250380826646,0.5288949197529045', '4.0,0.5680445610939323,0.925596638292661,0.07103605819788694', '5.0,0.08712929970154071,0.02021839744032572,0.832619845547938', '6.0,0.7781567509498505,0.8700121482468192,0.978618342232764', '7.0,0.7991585642167236,0.46147936225293185,0.7805291762864555', '8.0,0.11827442586893322,0.6399210213275238,0.1433532874090464', '9.0,0.9446689170495839,0.5218483217500717,0.4146619399905236'], ['0.0,0.26455561210462697,0.7742336894342167,0.45615033221654855', '1.0,0.5684339488686485,0.018789800436355142,0.6176354970758771', '2.0,0.6120957227224214,0.6169339968747569,0.9437480785146242', '3.0,0.6818202991034834,0.359507900573786,0.43703195379934145', '4.0,0.6976311959272649,0.06022547162926983,0.6667667154456677', '5.0,0.6706378696181594,0.2103825610738409,0.1289262976548533', '6.0,0.31542835092418386,0.3637107709426226,0.5701967704178796', '7.0,0.43860151346232035,0.9883738380592262,0.10204481074802807', '8.0,0.2088767560948347,0.16130951788499626,0.6531083254653984', '9.0,0.2532916025397821,0.4663107728563063,0.24442559200160274'],]
        self.assertEqual(len(df_lists), 5)
        self.assertTrue(all(isinstance(df, pd.DataFrame) for df in df_lists))
        
        for i in range(len(df_lists)):
            df =  df_lists[i].apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
            self.assertEqual(df, expect_df[i], "DataFrame contents should match the expected output")

    def test_invalid_directory(self):
        with self.assertRaises(FileNotFoundError):
            f_3287('non_existent_directory', 'test_file_*.xls')

    def test_no_matching_files(self):
        with self.assertRaises(ValueError):
            f_3287(self.test_dir, 'non_matching_pattern_*.xls')

    def test_returned_dataframe_content(self):
        df_list = f_3287(self.test_dir, 'test_file_*.xls')
        for df in df_list:
            self.assertEqual(df.shape, (10, 4))  # Including index column
            self.assertTrue(np.issubdtype(df.dtypes[1], np.number))

    def test_empty_directory(self):
        empty_dir = 'empty_test_dir'
        os.makedirs(empty_dir, exist_ok=True)
        with self.assertRaises(ValueError):
            f_3287(empty_dir, 'test_file_*.xls')
        os.rmdir(empty_dir)

# Run the tests
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