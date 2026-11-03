import unittest
import uuid

from entities.monster import Monster
from persistence.db import get_connection


class TestMonster(unittest.TestCase):

    def setUp(self):
        self.name = f'Drácula {uuid.uuid4().hex[:8]}'

    def tearDown(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM monster WHERE name = %s', (self.name,))
        connection.commit()
        cursor.close()
        connection.close()

    def test_save_inserts_monster(self):
        Monster(name=self.name, power='Vuelo').save()

        saved = [m for m in Monster.get_all() if m['name'] == self.name]
        self.assertEqual(len(saved), 1)
        self.assertEqual(saved[0]['power'], 'Flight')


if __name__ == '__main__':
    unittest.main()
