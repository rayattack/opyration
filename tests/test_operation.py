from unittest import TestCase

from opyration import Operation
from opyration.interfaces import Pool


SELECT = 'SELECT * FROM customers WHERE username = $1'


class OperationTest(TestCase):
    def setUp(self):
        self.op = Operation('customers', Pool())

    def tearDown(self):
        pass

    def test_select_statement(self):
        self.op.select().where(username='; drop customers')
        self.assertEqual(SELECT, self.op.sql)
        self.assertEqual(self.op.parameters, ['; drop customers'])

    def test_where_statement(self):
        pass

    def test_and_or_where_statement(self):
        pass

    def test_insert_statement(self):
        pass

    def test_update_statement(self):
        pass

    def test_delete_statement(self):
        pass
