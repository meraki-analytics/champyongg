import os
import re
import json
import inspect
from collections import OrderedDict
import champyongg, champyongg.common

types = {'int': 0, 'float': 0.0, 'dict': {}, 'list': [], 'str': "''"}


def convert(name):
    if len(name) == 1:
        return name.upper()
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


classes = OrderedDict()

def parse_type(obj, name=None):
    if isinstance(obj, champyongg.common.ChampyonGGObject):
        parse_instance(obj, name)
    elif isinstance(obj, list):
        for item in obj:
            parse_type(item, name)
    elif isinstance(obj, dict):
        for key, val in obj.items():
            parse_type(val, name)


def parse_instance(obj, name=None, indent=''):
    cls = name
    if name is not None:
        if name in classes: return
        classes[cls] = None
    lines = ['','']
    lines.append('{indent}class {cls}(champyongg.common.ChampyonGGObject):'.format(indent=indent, cls=cls))
    lines.append('{indent}    def __init__(self, dictionary):'.format(indent=indent))
    other_objs = []
    for name, attr in inspect.getmembers(obj):
        if '__' in name: continue
        if inspect.ismethod(attr): continue
        newname = name.replace('dmg', 'damage')
        if isinstance(attr, champyongg.common.ChampyonGGObject):
            other_objs.append((newname, attr))
            uppercase = newname[0].upper() + newname[1:]
            lines.append("{indent}        self.{notcamel} = {uppercase}(dictionary.get('{name}', {{}}))".format(indent=indent, notcamel=convert(newname), name=name, uppercase=uppercase))
            continue
        default = types[type(attr).__name__]
        lines.append("{indent}        self.{notcamel} = dictionary.get('{name}', {default})".format(indent=indent, notcamel=convert(newname), name=name, default=default))
        parse_type(attr, newname)
    for name, attr in other_objs:
        uppercase = name[0].upper() + name[1:]
        parse_instance(attr, uppercase, indent=indent)
    classes[cls] = lines


def main():
    champyongg.set_api_key(os.environ['CHAMPIONGG_KEY'])
    champyongg.print_calls(True)

    # Change the next two lines for each api call
    starting_class = 'Champion'
    #data = champyongg.get_champions("Annie")
    data = champyongg.get_champions()
    #print(data['Middle']['Lux'].games)

    parse_type(data, starting_class)

    print('import champyongg.common.ChampyonGGObject')
    for cls, lines in classes.items():
        print('\n'.join(lines))


if __name__ == '__main__':
    main()
