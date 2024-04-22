import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler

def f_2726(X, y, n_splits, batch_size, epochs):
    """
    Trains a simple neural network on provided data using k-fold cross-validation.
    The network has one hidden layer with 50 neurons and ReLU activation, and
    an output layer with sigmoid activation for binary classification.

    Parameters:
        X (numpy.array): The input data.
        y (numpy.array): The target data.
        n_splits (int): The number of splits for k-fold cross-validation. Default is 5.
        batch_size (int): The size of the batch used during training. Default is 32.
        epochs (int): The number of epochs for training the model. Default is 10.

    Returns:
        list: A list containing the training history of the model for each fold. Each history
              object includes training loss and accuracy.

    Requirements:
    - tensorflow
    - sklearn.model_selection.KFold
    - sklearn.preprocessing.MinMaxScaler

    Examples:
    >>> import numpy as np
    >>> X = np.random.rand(100, 10)
    >>> y = np.random.randint(0, 2, 100)
    >>> history = f_2726(X, y, 5, 32, 1)
    >>> isinstance(history, list)
    True
    >>> len(history)
    5
    >>> all('loss' in hist.history.keys() for hist in history)
    True
    """
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    kf = KFold(n_splits=n_splits)
    history = []

    for train_index, test_index in kf.split(X_scaled):
        X_train, X_test = X_scaled[train_index], X_scaled[test_index]
        y_train, y_test = y[train_index], y[test_index]

        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(50, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        hist = model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=batch_size, epochs=epochs, verbose=0)
        history.append(hist)

    return history

import unittest
import numpy as np
import tensorflow as tf
class TestCases(unittest.TestCase):
    def setUp(self):
        # Common setup for all tests
        self.X = np.random.rand(100, 10)
        self.y = np.random.randint(0, 2, 100)
        self.n_splits = 5
        self.batch_size = 32
        self.epochs = 10
    def test_return_type(self):
        """Test that the function returns a list."""
        result = f_2726(self.X, self.y, self.n_splits, self.batch_size, self.epochs)
        self.assertIsInstance(result, list)
    def test_history_length_with_default_splits(self):
        """Test the length of the history list matches the number of splits."""
        result = f_2726(self.X, self.y, self.n_splits, self.batch_size, self.epochs)
        self.assertEqual(len(result), self.n_splits)
    def test_training_metrics_inclusion(self):
        """Test that key metrics are included in the training history."""
        result = f_2726(self.X, self.y, self.n_splits, self.batch_size, self.epochs)
        self.assertTrue(all('accuracy' in hist.history for hist in result))
    def test_effect_of_different_n_splits(self):
        """Test function behavior with different values of n_splits."""
        for n_splits in [3, 7]:
            result = f_2726(self.X, self.y, n_splits, self.batch_size, self.epochs)
            self.assertEqual(len(result), n_splits)
    def test_effect_of_different_batch_sizes(self):
        """Test function behavior with different batch sizes."""
        for batch_size in [16, 64]:
            result = f_2726(self.X, self.y, self.n_splits, batch_size, self.epochs)
            self.assertEqual(len(result), self.n_splits)  # Validating function execution
    def test_effect_of_different_epochs(self):
        """Test function behavior with different epochs."""
        for epochs in [5, 20]:
            result = f_2726(self.X, self.y, self.n_splits, self.batch_size, epochs)
            self.assertEqual(len(result), self.n_splits)  # Validating function execution
