import json
from urllib.parse import urlencode

# بيانات JSON
json_data ={"method":"eth_chainId","params":[],"id":42,"jsonrpc":"2.0"}

# تحويل JSON المتداخل إلى flat dict مناسب للـ x-www-form-urlencoded
def flatten_json(y, prefix=''):
    out = {}
    for key, value in y.items():
        if isinstance(value, dict):
            out.update(flatten_json(value, prefix + key + '['))
        else:
            out[prefix + key + ']' if prefix else key] = value
    return out

# تحويل إلى x-www-form-urlencoded
form_data = urlencode(flatten_json(json_data))
print(form_data)
