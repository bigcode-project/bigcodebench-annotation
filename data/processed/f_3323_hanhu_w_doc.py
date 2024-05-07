from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

def f_408(X, Y):
    """
    This function performs the following operations:
    - Splits the input data into training (70%) and test (30%) sets.
    - Constructs a Keras Sequential model with one hidden dense layer and sigmoid activation.
      The input dimension is determined based on the first feature set of X.
    - Compiles the model using binary cross-entropy loss and SGD optimizer.
    - Fits the model to the training data in a non-verbose mode.
    - Plots the Precision-Recall curve for the model based on the test set data.

    Parameters:
    X (np.ndarray): Input data for the model. Must have at least one feature.
    Y (np.ndarray): Target labels for the model.

    Returns:
    - keras.models.Sequential: The trained Keras model.
    - matplotlib.axes._axes.Axes: The matplotlib Axes object for the Precision-Recall curve plot.
    
    Notes:
    - The plot's x-axis is labeled 'Recall', and the y-axis is labeled 'Precision'.
    - The title of the axes is set to 'Precision-Recall curve'.
    - The axes object allows for further customization of the plot outside the function.

    Requirements:
    - tensorflow.keras
    - sklearn.model_selection.train_test_split
    - sklearn.metrics.precision_recall_curve
    - matplotlib.pyplot

    Examples:
    >>> X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    >>> Y = np.array([[0], [1], [1], [0]])
    >>> model, ax = f_408(X, Y)
    >>> isinstance(model, Sequential)
    True
    >>> isinstance(ax, plt.Axes)
    True
    """
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
    input_dim = X.shape[1]  # Dynamically set input dimension
    model = keras.models.Sequential([keras.layers.Dense(units=1, input_dim=input_dim, activation='sigmoid')])
    model.compile(loss='binary_crossentropy', optimizer=keras.optimizers.SGD(learning_rate=0.1))
    model.fit(X_train, Y_train, epochs=200, batch_size=1, verbose=0)
    Y_pred = model.predict(X_test, verbose=0).ravel()
    precision, recall, thresholds = precision_recall_curve(Y_test, Y_pred)
    fig, ax = plt.subplots()  # Modify here to return Axes object
    ax.plot(recall, precision, label='Precision-Recall curve')
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_title('Precision-Recall Curve')
    ax.legend(loc='best')
    return model, ax  # Return both the model and the axes object

import unittest
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    def setUp(self):
        # Initialize common test data used in multiple test cases.
        self.X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        self.Y = np.array([0, 1, 1, 0])
    def test_model_and_axes_types(self):
        # Verify if the returned objects include a Keras Sequential model and a matplotlib Axes.
        model, ax = f_408(self.X, self.Y)
        self.assertIsInstance(model, Sequential, "The function should return a Sequential model.")
        self.assertIsInstance(ax, Axes, "The function should return a matplotlib Axes object.")
    def test_model_output_shape(self):
        # Ensure the model's output shape is correct based on the input data.
        model, _ = f_408(self.X, self.Y)
        self.assertEqual(model.output_shape, (None, 1), "The model's output shape should have one dimension for binary classification.")
    def test_model_loss(self):
        # Confirm that the model uses binary cross-entropy as its loss function.
        model, _ = f_408(self.X, self.Y)
        self.assertEqual(model.loss, 'binary_crossentropy', "Binary cross-entropy should be the loss function for the model.")
    def test_model_optimizer(self):
        # Check if the model's optimizer is an instance of SGD.
        model, _ = f_408(self.X, self.Y)
        self.assertIsNotNone(model.optimizer)
        self.assertIsInstance(model.optimizer, SGD, "The optimizer for the model should be SGD.")
    def test_input_dimension_flexibility(self):
        # Test the model's ability to handle inputs with varying feature dimensions.
        X_varied = np.array([[0], [1], [2], [3]])
        Y_varied = np.array([0, 1, 0, 1])
        model, _ = f_408(X_varied, Y_varied)
        self.assertEqual(model.input_shape[1], X_varied.shape[1], "The model should dynamically adapt to the input feature size.")
    def test_axes_labels_and_title(self):
        # Test if the Axes object has the correct title and labels as specified.
        _, ax = f_408(self.X, self.Y)
        self.assertEqual(ax.get_title(), 'Precision-Recall Curve', "The plot's title should be 'Precision-Recall Curve'.")
        self.assertEqual(ax.get_xlabel(), 'Recall', "The plot's x-axis label should be 'Recall'.")
        self.assertEqual(ax.get_ylabel(), 'Precision', "The plot's y-axis label should be 'Precision'.")
