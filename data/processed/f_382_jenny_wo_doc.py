import math
import numpy as np
from datetime import datetime
import pandas as pd


def f_783(
    start_time,
    end_time,
    step,
    columns=["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"],
    sensor_statuses=["OK", "MAINTENANCE_REQUIRED", "ERROR"],
    random_seed=42,
):
    """
    Generate a DataFrame with detailed artificial sensor readings for specified timestamps
    and sensor statuses from a predefined list.

    The function generates sensor readings for Sensor1, Sensor2, and Sensor3 (or their
    corresponding named columns in the supplied column list) using sine, cosine, and tan
    functions, respectively, of the timestamp (converted to seconds), with a small random
    noise added to simulate real sensor data variability.
    SensorStatus is randomly chosen from the provided statuses for each timestamp.

    Parameters:
    - start_time (int): Start time in milliseconds since epoch.
    - end_time (int): End time in milliseconds since epoch. Must not be before start_time.
    - step (int): The interval in milliseconds between each generated data point. Must be positive.
                  This step defines the frequency at which data points are generated. If the step
                  does not neatly divide the interval between start_time and end_time into
                  equal-sized portions, the last timestamp may be excluded.
    - columns (list of str, optional): Names of the DataFrame columns to be included in the output.
                                       Defaults to: ['Timestamp', 'Sensor1', 'Sensor2', 'Sensor3', 'SensorStatus'].
                                       Regardless of naming, the function will populate the first column with
                                       timestamp, the middle columns with sensor data, and the final with status.
    - sensor_statuses (list of str, optional): Possible statuses for the sensors to randomly assign in the dataset.
                                               Defaults to: ['OK', 'MAINTENANCE_REQUIRED', 'ERROR'].
    - random_seed (int, optional): Seed for the random number generator to ensure reproducible results.
                                   Defaults to 42.

    Returns:
    - pd.DataFrame: Generated sensor readings for the given timestamps.

    Requirements:
    - math
    - datetime
    - numpy
    - pandas

    Example:
    >>> df = f_783(0, 5000, 1000)
    >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    >>> df.head(1)
                        Timestamp   Sensor1   Sensor2   Sensor3 SensorStatus
    0  1970-01-01 00:00:00.000000  0.049671  0.986174  0.064769        ERROR
    """
    np.random.seed(random_seed)
    if start_time > end_time:
        raise ValueError("start_time cannot be after end_time")
    if step < 0:
        raise ValueError("step must be positive")
    timestamps = list(range(start_time, end_time, step))
    data = []
    for ts in timestamps:
        dt = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        sensor1 = math.sin(ts / 1000) + np.random.normal(0, 0.1)
        sensor2 = math.cos(ts / 1000) + np.random.normal(0, 0.1)
        sensor3 = math.tan(ts / 1000) + np.random.normal(0, 0.1)
        status = np.random.choice(sensor_statuses)
        row = [dt, sensor1, sensor2, sensor3, status]
        data.append(row)
    return pd.DataFrame(data, columns=columns)

import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        df = f_783(0, 10000, 100, random_seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(
            list(df.columns),
            ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"],
        )
        self.assertTrue(
            (df["SensorStatus"].isin(["OK", "MAINTENANCE_REQUIRED", "ERROR"])).all()
        )
    def test_case_2(self):
        # Test custom columns
        columns = ["Time", "Sensor_A", "Sensor_B", "Sensor_C", "Status"]
        statuses = ["WORKING", "NEEDS_CHECK", "FAILED"]
        df = f_783(
            1500, 3000, 50, columns=columns, sensor_statuses=statuses, random_seed=42
        )
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), columns)
        self.assertTrue((df["Status"].isin(statuses)).all())
    def test_case_3(self):
        # Test generated data integrity by comparing with expected results
        np.random.seed(42)
        ts = 0  # Using the starting timestamp for simplicity
        expected_sensor1 = math.sin(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        expected_sensor2 = math.cos(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        expected_sensor3 = math.tan(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        df = f_783(0, 100, 100, random_seed=42)
        self.assertAlmostEqual(df.iloc[0]["Sensor1"], expected_sensor1, places=5)
        self.assertAlmostEqual(df.iloc[0]["Sensor2"], expected_sensor2, places=5)
        self.assertAlmostEqual(df.iloc[0]["Sensor3"], expected_sensor3, places=5)
    def test_case_4(self):
        # Test handling invalid start times
        with self.assertRaises(ValueError):
            f_783(10000, 0, 100)
    def test_case_5(self):
        # Test handling incorrect end times
        with self.assertRaises(ValueError):
            f_783(1000, 900, 100)
    def test_case_6(self):
        # Test column handling
        columns = ["Time", "Value1", "Value2", "Value3", "MachineStatus"]
        df = f_783(0, 500, 100, columns=columns)
        self.assertEqual(list(df.columns), columns)
        # Too few/too many columns
        with self.assertRaises(ValueError):
            f_783(0, 500, 100, columns[:-1])
        with self.assertRaises(ValueError):
            f_783(0, 500, 100, columns + ["foo", "bar"])
    def test_case_7(self):
        # Test sensor status handling
        with self.assertRaises(ValueError):
            f_783(0, 500, 100, [])
        statuses = ["RUNNING", "SHUTDOWN", "ERROR"]
        df = f_783(0, 500, 100, sensor_statuses=statuses)
        self.assertTrue((df["SensorStatus"].isin(statuses)).all())
    def test_case_8(self):
        # Test random seed
        df1 = f_783(0, 500, 100, random_seed=42)
        df2 = f_783(0, 500, 100, random_seed=42)
        pd.testing.assert_frame_equal(df1, df2)
    def test_case_9(self):
        # Test invalid steps handling
        with self.assertRaises(ValueError):
            f_783(0, 1000, -100)  # Step is negative
        with self.assertRaises(ValueError):
            f_783(0, 1000, 0)  # Step is zero
