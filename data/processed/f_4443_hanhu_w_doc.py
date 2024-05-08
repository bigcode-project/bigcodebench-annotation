import inspect
import types
import json

def f_658(f):
    """
    Inspects the given function 'f' and returns its specifications as a JSON string. This includes
    the function's name, arguments, default values, annotations in a string format, and a boolean
    indicating if it's a lambda function.

    Parameters:
    f (function): The function to inspect.

    Returns:
    str: A JSON string containing the function's specifications.

    Requirements:
    - inspect
    - types
    - json

    Examples:
    >>> def sample_function(x, y=2): return x + y
    >>> 'sample_function' in f_658(sample_function)
    True
    >>> def sample_function2(x, y=2): return x * y
    >>> 'sample_function2' in f_658(sample_function2)
    True
    """
    spec = inspect.getfullargspec(f)
    annotations = {k: v.__name__ if isinstance(v, type) else str(v) for k, v in spec.annotations.items()}
    info = {
        'function_name': f.__name__,
        'args': spec.args,
        'defaults': spec.defaults,
        'annotations': annotations,
        'is_lambda': isinstance(f, types.LambdaType)
    }
    return json.dumps(info)

import unittest
import json
class TestCases(unittest.TestCase):
    def test_regular_function(self):
        def sample_function(x, y, z=3): pass
        result = json.loads(f_658(sample_function))
        self.assertEqual(result['function_name'], 'sample_function')
        self.assertIn('y', result['args'])
    def test_lambda_function(self):
        lambda_func = lambda x, y=2: x + y
        result = json.loads(f_658(lambda_func))
        self.assertTrue(result['is_lambda'])
        self.assertEqual(result['function_name'], '<lambda>')
    def test_no_arguments(self):
        def no_arg_func(): pass
        result = json.loads(f_658(no_arg_func))
        self.assertEqual(len(result['args']), 0)
    def test_function_with_no_defaults(self):
        def func_no_defaults(x, y): pass
        result = json.loads(f_658(func_no_defaults))
        self.assertIsNone(result['defaults'])
    def test_function_name(self):
        def simple_function(): pass
        result = json.loads(f_658(simple_function))
        self.assertEqual(result['function_name'], 'simple_function')
    
    def test_function_annotations(self):
        def annotated_function(x: int, y: str = 'hello') -> None: pass
        result = json.loads(f_658(annotated_function))
        self.assertDictEqual(result['annotations'], {'x': 'int', 'y': 'str', 'return': 'None'})
