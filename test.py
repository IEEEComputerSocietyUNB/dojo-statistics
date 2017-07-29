import unittest
import model
import view
import controller
import os

class TestMVC(unittest.TestCase):
    def setUp(self):
        # Creating data inside folder
        tf = 'data-test' # test folder
        admins = [100, 200, 300]
        with open('{0}/admins.csv'.format(tf), 'w+') as fp:
            for admin in admins:
                fp.write('%s\n' % (admin))

        # Starting new model
        self.model = model.Model('data-test')

    def test_can_load_admins(self):
        self.assertEqual(3, len(self.model.admins))

if __name__ == '__main__':
    unittest.main()
