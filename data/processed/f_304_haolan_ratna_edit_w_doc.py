import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Constants
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'

def f_304(df):
    """
    Train a linear regression model on a given DataFrame.
    
    Parameters:
    df (DataFrame): The DataFrame with features and target.
    
    Returns:
    LinearRegression: The trained linear regression model.
    
    Requirements:
    - pandas
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression
    
    Raises:
    - The function will raise a ValueError is input df is not a DataFrame.

    Example:
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> df = pd.DataFrame({'feature ' + str(i): np.random.rand(100) for i in range(1, 11)})
    >>> df['target'] = df.apply(lambda row: sum(row), axis=1)
    >>> model = f_304(df)
    >>> print(len(model.coef_))
    10
    """

    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

import unittest
import pandas as pd
from io import StringIO
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with CSV data
        TESTDATA = StringIO("""feature 1,feature 2,feature 3,feature 4,feature 5,feature 6,feature 7,feature 8,feature 9,feature 10,target
                    0.42400509556218957,0.4556954476778564,0.5876033479070203,0.7372019791788254,0.631294770216076,0.4950266019166166,0.0638144062778504,0.7069802218693271,0.9005726909016923,0.6939292546038213,14.696123816111275
                    0.7424296388887492,0.37759478623365395,0.6150348990404139,0.5245385173014507,0.34372354676823247,0.26734555024798334,0.25816065500447305,0.7593949490266066,0.28726200622586806,0.1389614032632609,11.314445952000693
                    0.5542329648360879,0.8921257562394426,0.8642884839827235,0.15535175081891284,0.04765544199312799,0.6959587174128501,0.8750991336831166,0.9405740432480505,0.6080858349786378,0.20758024604975633,11.840952373242706
                    0.3128080182238582,0.4306484443433306,0.13158163455824945,0.6124936004910966,0.3658172041589832,0.8865358950435007,0.6896354766071041,0.49374167962283977,0.09496096416410882,0.8635022149845224,9.881725132197595
                    0.9918117132641856,0.34155948441867745,0.13825937535425548,0.2075606744217059,0.5024270600409457,0.4499385613253092,0.927332889017184,0.9226317268159956,0.7109355740305163,0.48498273400417413,7.67743979269295
                    0.8487974650141276,0.5419882208385368,0.6219327392404139,0.607186072248796,0.5817917868937075,0.16757506758203844,0.513478962441245,0.5813924083375205,0.2999370992352748,0.8095241847125411,9.573604006544201
                    0.8531765660138543,0.6230807384621613,0.121193482114335,0.40339655427645227,0.8252000772363516,0.7089362855980166,0.4399130776125867,0.5547381179483073,0.5271579371209105,0.4887721459504082,8.545564982333383
                    0.7379434286935841,0.35388533243065834,0.28270164727057234,0.10937131252334209,0.7554490444282028,0.11627353503671667,0.29878795437943706,0.5272147239980629,0.6682257849027331,0.4506451053217232,5.300497868985032
                    0.51734842472885,0.7300897961646883,0.8822236158906909,0.8223865310105216,0.14248094409880296,0.49409856103306826,0.9337165561571048,0.8043124404561036,0.912213630647814,0.41502961287020834,13.653900113057855
                    0.4338281641525509,0.6559602318884544,0.62746801792774,0.5038739464689795,0.08921870715449975,0.7274382944105564,0.6152014156275979,0.2093703770326366,0.9052167270350973,0.4696339914768609,8.237209873174972
                    """)
        df = pd.read_csv(TESTDATA)
        model = f_304(df)
        self.assertIsInstance(model, LinearRegression, "Return type should be LinearRegression")
        self.assertEqual(len(model.coef_), 10, "Model should have coefficients for all 10 features")
        
    def test_case_2(self):
        # Testing with JSON data
        TESTDATA = StringIO("""[{"feature 1":0.4240050956,"feature 2":0.4556954477,"feature 3":0.5876033479,
                            "feature 4":0.7372019792,"feature 5":0.6312947702,"feature 6":0.4950266019,
                            "feature 7":0.0638144063,"feature 8":0.7069802219,"feature 9":0.9005726909,
                            "feature 10":0.6939292546,"target":14.6961238161},{"feature 1":0.7424296389,
                            "feature 2":0.3775947862,"feature 3":0.615034899,"feature 4":0.5245385173,
                            "feature 5":0.3437235468,"feature 6":0.2673455502,"feature 7":0.258160655,
                            "feature 8":0.759394949,"feature 9":0.2872620062,"feature 10":0.1389614033,
                            "target":11.314445952},{"feature 1":0.5542329648,"feature 2":0.8921257562,
                            "feature 3":0.864288484,"feature 4":0.1553517508,"feature 5":0.047655442,
                            "feature 6":0.6959587174,"feature 7":0.8750991337,"feature 8":0.9405740432,
                            "feature 9":0.608085835,"feature 10":0.207580246,"target":11.8409523732}
                            ] """)
        df = pd.read_json(TESTDATA)
        model = f_304(df)
        self.assertIsInstance(model, LinearRegression, "Return type should be LinearRegression")
        self.assertEqual(len(model.coef_), 10, "Model should have coefficients for all 10 features")
        
    def test_case_3(self):
        # Testing with random data
        np.random.seed(0)
        df = pd.DataFrame({
            'feature ' + str(i): np.random.rand(100) for i in range(1, 11)
        })
        df['target'] = df.apply(lambda row: sum(row), axis=1)
        model = f_304(df)
        self.assertIsInstance(model, LinearRegression, "Return type should be LinearRegression")
        self.assertEqual(len(model.coef_), 10, "Model should have coefficients for all 10 features")
    def test_case_4(self):
        # Testing with data where all features are zeros
        df = pd.DataFrame({
            'feature ' + str(i): [0]*100 for i in range(1, 11)
        })
        df['target'] = [0]*100
        model = f_304(df)
        self.assertIsInstance(model, LinearRegression, "Return type should be LinearRegression")
        self.assertTrue(all(coef == 0 for coef in model.coef_), "All coefficients should be zero")
    def test_case_5(self):
        # Testing with data where target is a linear combination of features
        np.random.seed(0)
        df = pd.DataFrame({
            'feature ' + str(i): np.random.rand(100) for i in range(1, 11)
        })
        df['target'] = df['feature 1'] + 2*df['feature 2'] + 3*df['feature 3']
        model = f_304(df)
        self.assertIsInstance(model, LinearRegression, "Return type should be LinearRegression")
        self.assertAlmostEqual(model.coef_[0], 1, places=1, msg="Coefficient for feature 1 should be close to 1")
        self.assertAlmostEqual(model.coef_[1], 2, places=1, msg="Coefficient for feature 2 should be close to 2")
        self.assertAlmostEqual(model.coef_[2], 3, places=1, msg="Coefficient for feature 3 should be close to 3")
