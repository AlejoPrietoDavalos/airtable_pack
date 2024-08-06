from pyairtable import Table
from pyairtable.formulas import match

def update_record(table: Table, filter: dict, update: dict) -> dict:
    formula = match(filter)
    record =table.all(formula=formula)
    if len(record) > 0:
        id_ = record[0]['']
        result = table.update(id_, update)
        return result
    else:
        return []