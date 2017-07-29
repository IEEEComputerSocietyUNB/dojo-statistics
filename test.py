import unittest
import model
import view
import controller

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = model.Model('data-test')

    def test_can_load_admins(self):
        self.assertEqual(3, len(self.model.admins))

    def test_can_load_ids(self):
        ids = self.model.getIds()
        self.assertEqual(13, len(ids))

# TODO Implement Controller tests

if __name__ == '__main__':
    unittest.main()
