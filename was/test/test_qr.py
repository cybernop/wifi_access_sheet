import os
import unittest

from was import qr


class TestQr(unittest.TestCase):
    def test_gen_code(self):
        text = 'This is test!'
        file_name = 'foo.svg'
        qr.gen_code(text, file=file_name)
        os.remove(file_name)

    def test_gen_wifi_code(self):
        file_name = 'test_wifi.svg'
        qr.gen_wifi_code(file=file_name, ssid='TestSSID', password='passphrase')
        os.remove(file_name)
