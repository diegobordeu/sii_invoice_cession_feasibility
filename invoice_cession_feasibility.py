import requests
import json
# from sii_cookie import AuthCookie


class GetInvoiceFeasibility:
    endpoint = 'https://www4.sii.cl/registrorechazodtej6ui/services/data/facadeService/consultarDocDteCedible'
    headers = {
        'Content-Type': 'application/json',
    }

    # def __init__(self, auth_cookie: AuthCookie) -> None:
    #     self.auth_cookie = auth_cookie
    #     self.auth_cookie.login_with_rut()

    def check_cession_feasibility(self, company_rut, invoice_folio, dte_type):
        """
        Ask to Sii if is posible to assign any invoice with the SII feasible criteria
        Login strategy: certificate
        """
        self.check_input(company_rut, invoice_folio, dte_type)
        return self.get_invoice_feasibility(
            company_rut, invoice_folio, dte_type,
        )

    def check_input(self, company_rut, invoice_folio, dte_type):
        if not company_rut:
            raise ValueError('company_rut is not defined')
        if not invoice_folio:
            raise ValueError('invoice_folio is not defined')
        if not dte_type:
            raise ValueError('dte_type is not defined')

    def get_invoice_feasibility(self, company_rut, invoice_folio, dte_type):
        payload = {
            'data': {
                'rutEmisor': company_rut.split('-')[0],
                'dvEmisor': company_rut.split('-')[1],
                'tipoDoc': dte_type,
                'folio': invoice_folio,
            },
        }
        json_data = json.dumps(payload)
        req = requests.post(
            self.endpoint,
            data=json_data,
            # cookies=self.auth_cookie.cookies,
            headers=self.headers,
        )
        response = json.loads(req.text)
        return self.extract_response(response)

    def extract_response(self, json_response):
        feasibility = json_response['data']['msgDteCedible']
        return feasibility
