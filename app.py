from invoice_cession_feasibility import GetInvoiceFeasibility

checker = GetInvoiceFeasibility()
response = checker.check_cession_feasibility(
    company_rut='xxxxxx-y',
    invoice_folio='xxx',
    dte_type='33', # 33 o 34
)
print(response)