from re import X
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

    def test_with_statement(self):
        opx = Operation('orders', Pool())
        self.op.cte('xq').wrap(
            opx.insert(nom='; drop orders').returning('id')
        ).insert(
            username='; drop customers',
            safe=self.op.safe('(SELECT id FROM xq)')
        )

        xq = 'WITH xq AS (INSERT INTO orders (nom) VALUES ($1) RETURNING id)'
        xq = f'{xq} INSERT INTO customers (username, safe) VALUES ($2, (SELECT id FROM xq))'

        self.assertEqual(xq, self.op.sql)
        self.assertEqual(self.op.parameters, ['; drop customers'])

    def test_and_or_where_statement(self):
        pass

    def test_insert_statement(self):
        pass

    def test_update_statement(self):
        pass

    def test_delete_statement(self):
        pass
