import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        x= "aaaaaaaa"
        self.assertFalse(check_pwd(x))

    # len 7
    def test2(self):
        x= "aaaaaaa"
        self.assertFalse(check_pwd(x))

    # len 21
    def test3(self):
        x= "aaaaaaaaaaaaaaaaaaaaa"
        self.assertFalse(check_pwd(x))

    # no special char
    def test4(self):
        x = "aaaaaaA8"
        self.assertFalse(check_pwd(x))

    # no uppercase
    def test5(self):
        x = "aaaa!aaaaaaa8"
        self.assertFalse(check_pwd(x))

    # no lowercase
    def test6(self):
        x = "!AAAAAAAA8"
        self.assertFalse(check_pwd(x))

    # should work
    def test7(self):
        x = "!aA3fffffff"
        self.assertTrue(check_pwd(x))


if __name__ == '__main__':
    unittest.main()