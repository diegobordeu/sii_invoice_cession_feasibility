import json
import requests

class AuthCookieError(Exception):
    pass

class AuthCookie(object):
    """
    """
    raw_rut: str = ''
    rut: str = ''
    rut_dv: str = ''
    cookies: dict = {}

    def __init__(self, rut: str, password: str) -> None:
        self.rut = rut
        self.password = password
        self._check_input()

    def login_with_rut(self) -> None:
        url = 'https://zeusr.sii.cl/cgi_AUT2000/CAutInicio.cgi'
        self._serialize_rut()
        payload = {
            'rut': self.rut,
            'dv': self.rut_dv,
            'referencia': 'https://misiir.sii.cl/cgi_misii/siihome.cgi',
            '411': '',
            'rutcntr': self.rut_thousand_separator(self.raw_rut),
            'clave': self.password,
        }
        r = requests.post(url, data = payload)
        cookies = {}
        for cookie in r.cookies:
            cookies[cookie.name] = cookie.value
        print('Using cookies ------------------>:')
        print(cookies)
        self.cookies = cookies

    def _serialize_rut(self) ->  None:
        self.raw_rut = self.rut
        separate = self.raw_rut.split('-')
        if len(separate) < 2:
            raise ValueError('invalid rut, missing validator')
        self.rut = separate[0]
        self.rut_dv = separate[1]

    def _check_input(self) -> None:
        if not self.rut:
            raise ValueError('rut is not defined in request')
        if not self.password:
            raise ValueError('password is not defined in request')

    def rut_thousand_separator(self, rut: str):
        first_rut = ''
        if('-' in rut):
            first_rut = rut.split('-')[0]
        else:
            first_rut = rut
        final_first_rut = self._place_value(int(first_rut))
        if('-' in rut):
            return(final_first_rut + rut.split('-')[1])
        else:
            return(final_first_rut)

    def _place_value(self, number):
        return(str('{:,}'.format(number).replace(',', '.')))


