import json
from collections import OrderedDict

def load(filename):
    return json.load(open(filename), object_pairs_hook = OrderedDict)

def save(obj, filename):
    s, c = formatObj(obj, '')
    open(filename, 'w').write(s);

def format(inf, outf):
    save(load(inf), outf)

def formatObj(obj, indent):
    if type(obj) is int or type(obj) is float or type(obj) is bool:
        return str(obj).lower(), False

    elif type(obj) is str:
        if obj == '0':
            return '0', False
        else:
            obj = obj.strip(' \t\n\r')
            obj = obj.replace('\r', '')
            obj = obj.replace('\n', '\\n')
            obj = obj.replace('"', '\\"')
            return '"' + obj + '"', False

    elif type(obj) is list:
        if len(obj) == 0:
            return '[ ]', False
        if len(obj) == 1:
            s, c = formatObj(obj[0], indent)
            return '[ ' + s + ' ]', c

        ret = [ ]
        comp = False
        for o in obj:
            s, c = formatObj(o, indent + '  ')
            ret.append(s)
            comp = comp or c

        s = '[ ' + ', '.join(ret) + ' ]'
        if comp or len(s) > 80:
            s = '[\n  ' + indent + (',\n  ' + indent).join(ret) + '\n' + indent + ']'
        return s, True

    elif type(obj) is dict or type(obj) is OrderedDict:
        if len(obj) == 0:
            return '{ }', False

        ret = [ ]
        comp = False
        items = obj.items()
        if type(obj) is dict:
            items = sorted(items)

        for k, v in items:
            s, c = formatObj(v, indent + '  ')
            s = '"' + k + '": ' + s
            ret.append(s)
            comp = comp or c

        s = '{ ' + ', '.join(ret) + ' }'
        if comp or len(s) > 80:
            s = '{\n  ' + indent + (',\n  ' + indent).join(ret) + '\n' + indent + '}'
        return s, True

    else:
        return '\n!!!!! unkown type ' + str(type(obj)) + ' !!!!!\n', True
