import pprint
def introspection_info(obj):
    return {'type': type(obj), 'attributes': obj.__ne__, 'methods': dir(obj), 'module': __name__}

number_info = introspection_info(42)
pprint.pprint(number_info)