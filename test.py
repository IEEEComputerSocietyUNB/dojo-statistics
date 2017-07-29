import unittest
import model
import view
import controller

class TestJudge(unittest.TestCase):
    def setUp(self):
        self.model = model.Model()

    def test_can_load_ids(self):
        ids = self.model.getIds()
        self.assertEqual(3, len(ids))


if __name__ == '__main__':
    unittest.main()
