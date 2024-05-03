import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def f_1776(df):
    """
    Perform Principal Component Analysis (PCA) on the dataframe and visualize the two main components.

    Parameters:
        df (DataFrame): The input dataframe containing numerical data.

    Returns:
        DataFrame: A pandas DataFrame with the principal components named 'Principal Component 1' and 'Principal Component 2'.
        Axes: A Matplotlib Axes object representing the scatter plot of the two principal components. The plot includes:
              - Title: '2 Component PCA'
              - X-axis label: 'Principal Component 1'
              - Y-axis label: 'Principal Component 2'

    Raises:
        ValueError: If the input is not a DataFrame, or if the DataFrame is empty.

    Requirements:
        - numpy
        - pandas
        - sklearn.decomposition
        - matplotlib.pyplot

    Example:
        >>> df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        >>> pca_df, ax = f_1776(df)
        >>> plt.show()
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)

    pca_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])

    fig, ax = plt.subplots()
    ax.scatter(pca_df['Principal Component 1'], pca_df['Principal Component 2'])
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('2 Component PCA')

    return pca_df, ax


import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        
    def test_return_types(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        pca_df, ax = f_1776(df)
        self.assertIsInstance(pca_df, pd.DataFrame)
        self.assertIsInstance(ax, plt.Axes)
        df_list = pca_df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()

        expect = ['-13.610180281686779,36.44721199193204', '54.40050504687483,-22.08830947385322', '53.290672923391526,19.898200550170877', '-5.838062157770876,-41.496605164774465', '-53.21056178179435,-6.7930062349134515', '-44.061886187661926,-30.26929206755502', '-33.38668139161531,0.2552130859489897', '42.255766328331084,13.739000535024472', '6.029899810881003,15.126238793255917', '-18.384663806486895,-23.117183027938218', '17.000034894438222,5.940521054610546', '-60.98474060274173,-21.94655052613455', '-30.00040461300892,18.450912244913084', '-27.820112695627206,44.198551124848585', '21.640482233430532,42.827012832167476', '21.27682410219371,28.918723887000585', '-6.426505623035057,-30.06591045527269', '-11.820945264130339,12.934284948939736', '-37.93307224338836,-64.21332912709326', '-29.83733474784538,24.643368440288672', '31.177462497011778,27.951751630043795', '4.163378868131486,47.948877633664104', '39.466441761424804,-31.84126770945458', '33.46694547443355,34.986280788336444', '-13.419491344759962,39.536680403381986', '-27.449385998856247,2.326064334907882', '10.153378864987577,-37.42419694285016', '20.506332029367186,51.13871157458237', '15.479166813559896,-74.77051810727116', '-57.57615058127615,1.9487900993388594', '-26.28549929067824,-9.65224302392506', '28.87232875337196,-51.516178606375064', '-21.369932342462864,-34.1236876316218', '-10.606417996694866,-24.82414729954915', '68.74958300244347,18.816565469782933', '5.579297552982031,-17.677003191776734', '-21.341966358559443,4.735975870591118', '-5.860887616205186,12.519691151114444', '37.21768187909752,-14.039591194450889', '49.55165019654304,13.908325957765262', '-4.109823681478022,41.18095690997478', '-18.300419558723313,-40.56436386765031', '12.97814603859903,-29.84604839728002', '-6.506242870125811,33.44213945007128', '7.505109890855539,-14.249083056889246', '-26.99501720264034,-40.656443040125', '45.453529299057095,6.609269644757153', '43.79745816650168,48.66782572175226', '7.676376328527824,-55.529326002382895', '-36.585551589106444,-29.46960291192543', '2.6859086882920256,-20.946872012051397', '11.579319461434466,2.5153864773509023', '55.65592970891825,-20.57057269653286', '1.3120328752605257,4.833318905811497', '-66.85919589343598,-21.075315868673822', '-37.314605233768106,20.103748957710636', '-11.022351981248699,-12.253094718104157', '-35.890162916537804,75.92254310123329', '0.53667516622158,-33.56379772599969', '-10.956580788988687,2.694011504501463', '-26.643240831906112,16.27972355916017', '43.96533676049477,-32.97055341038151', '-42.552908807033326,47.31748220762675', '32.03341655049094,43.71683520153914', '-40.72528773476276,61.217583717153836', '23.734199718309124,4.642277267288987', '38.089253264176364,-0.5061650349672543', '-4.583397633889209,20.013141375057923', '-63.74373365434338,25.377057283508336', '33.902236715160406,21.630704685022035', '6.155388132598106,-45.93243697925512', '52.008505649077165,16.555012713476824', '-0.18435306886596514,-9.693856193910898', '-42.94165871339571,-13.297676348950137', '-51.35787421418141,8.196312826088189', '0.5434319974521136,0.24151904201080152', '14.133309129080612,-2.0678582975907136', '33.78108321347497,8.564486971124488', '13.07575726872196,44.0566337280887', '56.11471908089624,-0.06620431371651866', '27.017702255899717,-17.13919197733164', '-16.676726628569483,27.557565811529475', '-9.174097986026135,-27.752306755006675', '-6.124717633062933,-37.10319119462639', '6.841151020609539,-36.03494866860251', '-33.71096275749417,35.839301962584926', '-33.490515349711494,-10.213343702797827', '-3.270829570273045,-46.33176027759562', '-25.77282461526263,19.258518945937205', '19.15474665121042,41.0229034285221', '4.328634342877976,-48.53841855483938', '37.26577616545747,-21.838309778324763', '-56.74309813743457,12.457783909615435', '46.88891827433472,32.764991917828794', '49.153097685617915,-16.86188317717609', '17.674964710773796,30.321628721965062', '-17.175251345113725,12.970994233380647', '14.486399874990791,-53.79024894129019', '-21.72778895012001,16.325058069552753', '-11.442244844483053,-26.771778965048394']
        
        self.assertEqual(len(df_list), len(expect), "DataFrame size contents should match the expected output")
        for a, b in zip(df_list, expect):
            a1, a2 = str(a).split(',')
            b1, b2 = str(b).split(',')
            self.assertAlmostEqual(float(a1), float(b1), places=7)
            self.assertAlmostEqual(float(a2), float(b2), places=7)
        # self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")

    def test_invalid_input_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1776(pd.DataFrame())

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            f_1776("not a dataframe")

    def test_pca_columns(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        pca_df, _ = f_1776(df)
        self.assertTrue(all(col in pca_df.columns for col in ['Principal Component 1', 'Principal Component 2']))

    def test_plot_labels(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        _, ax = f_1776(df)
        self.assertEqual(ax.get_title(), '2 Component PCA')
        self.assertEqual(ax.get_xlabel(), 'Principal Component 1')
        self.assertEqual(ax.get_ylabel(), 'Principal Component 2')

    def test_pca_dataframe_structure(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        pca_df, _ = f_1776(df)
        self.assertEqual(pca_df.shape[1], 2)  # Should have 2 principal components

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