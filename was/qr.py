import pyqrcode


def gen_code(text, file):
    qr_code = pyqrcode.create(text, error='H')
    qr_code.svg(file)


def gen_wifi_code(file, ssid, password, type_='WPA2', hidden=False):
    raw_text = 'WIFI:S:{};T:{};P:{};H:{};;'.format(ssid, type_, password, 'true' if hidden else 'false')
    gen_code(raw_text, file)
