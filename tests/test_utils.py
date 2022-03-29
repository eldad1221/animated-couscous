import os
import uuid
import unittest
from awspstore import get_env_as_list, get_parameters


class UtilsTestCase(unittest.TestCase):

    def test_get_env_as_list(self):
        var_name = f'var_{uuid.uuid4()}'
        value = '   a ,B,1,  2  '
        os.environ[var_name] = value
        valid_result = ['a', 'B', '1', '2']
        self.assertEqual(valid_result, get_env_as_list(key=var_name))
        self.assertEqual(valid_result, get_env_as_list(key=f'{uuid.uuid4()}', default=valid_result.copy()))

    def test_get_parameters(self):
        results = get_parameters(path='dev')
        self.assertIsNotNone(results)
        self.assertIsInstance(results, dict)


if __name__ == '__main__':
    unittest.main()
