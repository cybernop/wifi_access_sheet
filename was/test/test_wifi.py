import os
import unittest

from was import wifi


class TestWifi(unittest.TestCase):
    def test_gen_password(self):
        length = 63
        password = wifi.gen_password(length)
        self.assertEqual(len(password), length)
        self.assertRegex(password, '^[a-zA-Z0-9]*$')

    def test_gen_password_write(self):
        length = 63
        file_name = 'password.txt'
        wifi.gen_password(length, write=True)
        with open(file_name, 'r') as file:
            content = file.read()
        os.remove(file_name)
        self.assertEqual(len(content), length)
        self.assertRegex(content, '^[a-zA-Z0-9]*$')


if __name__ == '__main__':
    unittest.main()
