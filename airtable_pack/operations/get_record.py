from pyairtable import Table
from pyairtable.formulas import match

def get_record(table: Table, filter: dict) -> dict:
    formula = match(filter)
    result = table.all(formula=formula)
    return result
