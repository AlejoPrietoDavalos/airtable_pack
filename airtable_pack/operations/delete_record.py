from pyairtable import Table
from pyairtable.formulas import match

def delete_record(table: Table, filter: dict) -> dict:
    formula = match(filter)
    result = table.delete(formula['id'])
    return result
