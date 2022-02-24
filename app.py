from invoice_cession_feasibility import GetInvoiceFeasibility

checker = GetInvoiceFeasibility()
response = checker.check_cession_feasibility(
    company_rut='76340335-1',
    invoice_folio='544',
    dte_type='33',
)
print(response)