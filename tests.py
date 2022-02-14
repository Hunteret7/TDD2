import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        x= "aaaaaaaa"
        self.assertFalse(check_pwd(x))

    def test2(self):
        x= "aaaaaaa"
        self.assertFalse(check_pwd(x))

if __name__ == '__main__':
    unittest.main()