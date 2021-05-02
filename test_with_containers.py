import time

import psycopg2
from psycopg2 import errors
import testcontainers.compose
import unittest


import function_example


class TestcontainersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestcontainersTest, cls).setUpClass()
        compose_path = './database'
        cls.compose = testcontainers.compose.DockerCompose(compose_path)
        cls.compose.start()

        # wait for the container be ready
        for i in range(101):
            try:
                cls.connection = psycopg2.connect("dbname=test_database host=localhost user=test_user password=test_password")
            except psycopg2.OperationalError:
                # fails after 100 seconds
                if i == 100:
                    raise psycopg2.OperationalError
                time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        super(TestcontainersTest, cls).tearDownClass()
        cls.compose.stop()

    def test_1(self):
        cursor = self.connection.cursor()
        function_example.working_function(cursor)
        cursor.close()

    def test_2(self):
        cursor = self.connection.cursor()
        # 23503 is the code error for ForeignKeyViolation
        self.assertRaises(errors.lookup('23503'), function_example.broken_function, cursor)
        cursor.close()




