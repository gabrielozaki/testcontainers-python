import unittest
from unittest.mock import Mock
from psycopg2 import errors

import function_example


class MockTest(unittest.TestCase):
    def test_1(self):
        cursor = Mock()
        function_example.working_function(cursor)
        cursor.close()

    # this test purposely fails
    def test_2(self):
        cursor = Mock()
        # 23503 is the code error for ForeignKeyViolation
        self.assertRaises(errors.lookup('23503'), function_example.broken_function, cursor)
        cursor.close()




