import inspect
import types

def f_4441(f):
    """
    Inspects a given function 'f' and returns its specifications, including the function's name,
    whether it is a lambda function, its arguments, defaults, and annotations. This method
    utilizes the inspect and types modules to introspect function properties.

    Parameters:
    f (function): The function to inspect.

    Returns:
    dict: A dictionary containing details about the function, such as its name, if it's a lambda function,
          arguments, default values, and annotations.

    Requirements:
    - inspect
    - types

    Examples:
    >>> def sample_function(x, y=5): return x + y
    >>> result = f_4441(sample_function)
    >>> 'sample_function' == result['function_name'] and len(result['args']) == 2
    True
    >>> lambda_func = lambda x: x * 2
    >>> f_4441(lambda_func)['is_lambda']
    True
    """
    spec = inspect.getfullargspec(f)

    return {
        'function_name': f.__name__,
        'is_lambda': isinstance(f, types.LambdaType),
        'args': spec.args,
        'defaults': spec.defaults,
        'annotations': spec.annotations
    }

import unittest
class TestCases(unittest.TestCase):
    def test_regular_function(self):
        def test_func(a, b=1): pass
        result = f_4441(test_func)
        self.assertEqual(result['function_name'], 'test_func')
        self.assertListEqual(result['args'], ['a', 'b'])
        self.assertTupleEqual(result['defaults'], (1,))
    def test_lambda_function(self):
        lambda_func = lambda x, y=2: x + y
        result = f_4441(lambda_func)
        self.assertTrue(result['is_lambda'])
    def test_no_arguments(self):
        def test_func(): pass
        result = f_4441(test_func)
        self.assertEqual(len(result['args']), 0)
    def test_annotations(self):
        def test_func(a: int, b: str = 'hello') -> int: pass
        result = f_4441(test_func)
        self.assertIn('a', result['annotations'])
        self.assertIn('return', result['annotations'])
    def test_defaults_none(self):
        def test_func(a, b=None): pass
        result = f_4441(test_func)
        self.assertIsNone(result['defaults'][0])
