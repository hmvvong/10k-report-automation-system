# validation
def validate_financials(e):
    errors = []
    if e['Revenues'] - e['CostOfRevenue'] != e['NetIncomeLoss']:
        errors.append("Income Statement mismatch.")
    if e['Assets'] - e['Liabilities'] != e['StockholdersEquity']:
        errors.append("Balance sheet mismatch.")
    return errors

def validate_ixbrl_basic(ixrbl):
    errors = []
    if "<ix:header>" not in ixrbl: errors.append("Missing ix:header.")
    if "<ix:nonNumeric" not in ixrbl: errors.append("Missing nonNumeric.")
    if "<ix:nonFraction" not in ixrbl: errors.append("Missing nonFraction.")
    return errors
